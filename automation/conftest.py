import os
import time
from pathlib import Path
from datetime import datetime

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


# Find .env in the current folder or any parent folder
current_folder = Path(__file__).resolve().parent

env_path = next(
    (
        folder / ".env"
        for folder in [current_folder, *current_folder.parents]
        if (folder / ".env").is_file()
    ),
    None
)

if env_path is None:
    raise FileNotFoundError(
        "Could not find .env file in the current or parent folders."
    )

load_dotenv(env_path, override=True)

print("ENV file found:", env_path.is_file())
print("Username loaded:", bool(os.getenv("WEB_USERNAME")))
print("Password loaded:", bool(os.getenv("WEB_PASSWORD")))


# Screenshot folder
SCREENSHOT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "screenshots"
)


# def save_screenshot(driver, name):
#     try:
#         os.makedirs(SCREENSHOT_DIR, exist_ok=True)

#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"{name}_{timestamp}.png"

#         screenshot_path = os.path.join(
#             SCREENSHOT_DIR,
#             filename
#         )

#         driver.save_screenshot(screenshot_path)
#         print(f"Screenshot saved: {screenshot_path}")

#     except Exception as error:
#         print(f"Could not save screenshot: {error}")


def save_screenshot(driver, name):
    try:
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"{name}_{timestamp}.png"

        screenshot_path = os.path.abspath(
            os.path.join(SCREENSHOT_DIR, filename)
        )

        if driver.save_screenshot(screenshot_path):
            print(f"Screenshot saved: {screenshot_path}")
            return screenshot_path

    except Exception as error:
        print(f"Could not save screenshot: {error}")

    return ""


# # Capture a screenshot when a test fails
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     if report.failed:
#         driver = item.funcargs.get("driver")

#         if driver:
#             save_screenshot(driver, "test_failure")




# Store pytest results for the web Excel report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Keep the latest report for each test phase
    setattr(item, f"rep_{report.when}", report)

    # Store every test execution attempt (not setup/teardown)
    if report.when == "call":
        if not hasattr(item, "web_attempt_reports"):
            item.web_attempt_reports = []

        item.web_attempt_reports.append(report)

        # Capture a screenshot when an attempt fails
        if report.failed:
            driver = item.funcargs.get("driver")
            screenshot_path = ""

            if driver:
                screenshot_path = save_screenshot(
                    driver,
                    f"{item.name}_attempt_{len(item.web_attempt_reports)}"
                )

            report.screenshot_path = screenshot_path




# Collect results and generate the web Excel report at the end
def pytest_sessionfinish(session, exitstatus):
    try:
        from excel_report import create_report

        results = []

        for item in session.items:
            # Get all retry attempts collected by pytest_runtest_makereport
            attempt_reports = getattr(item, "web_attempt_reports", [])

            setup_report = getattr(item, "rep_setup", None)

            # Handle tests that failed during setup
            if not attempt_reports and setup_report and setup_report.failed:
                attempt_reports = [setup_report]

            if not attempt_reports:
                continue

            final_status = (
                "PASS" if attempt_reports[-1].passed else "FAIL"
            )

            for attempt_number, report in enumerate(
                attempt_reports, start=1
            ):
                status = "PASS" if report.passed else "FAIL"

                error_details = (
                    str(report.longrepr) if report.failed else ""
                )

                actual_result = (
                    "Test completed successfully."
                    if report.passed
                    else "Test failed. See Error Details."
                )

                screenshot_path = getattr(
                    report, "screenshot_path", ""
                )

                results.append({
                    "Module": item.module.__name__,
                    "Test Case": item.name,
                    "Test Data": "Program Outcome",
                    "Attempt": attempt_number,
                    "Status": status,
                    "Expected Result": (
                        "Program Outcome form should accept valid data "
                        "and save successfully."
                    ),
                    "Actual Result": actual_result,
                    "Error Details": error_details,
                    "Screenshot Path": screenshot_path,
                    "Execution Time (seconds)": round(
                        report.duration, 2
                    ),
                    "Final Status": final_status
                })

        if results:
            create_report(results)
        else:
            print("No web test results available for the Excel report.")

    except Exception as error:
        print(f"Could not generate web Excel report: {error}")


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        # Read credentials from .env
        username_value = os.getenv("WEB_USERNAME")
        password_value = os.getenv("WEB_PASSWORD")

        if not username_value or not password_value:
            raise ValueError(
                "WEB_USERNAME or WEB_PASSWORD is missing. "
                "Please check your .env file."
            )

        # Open the login page
        driver.get("https://devops.evolutionco.in/nextgen/")

        # Enter username
        username = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.NAME, "email")
            )
        )
        username.send_keys(username_value)

        # Enter password
        password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.NAME, "password")
            )
        )
        password.send_keys(password_value)

        # Click Login
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@type='submit']")
            )
        )
        login_button.click()

        # Wait for the session dropdown
        dropdown_locator = (
            By.XPATH,
            "((//div[@class='nice-select nice_Select bgLess mb-0 infix_session'])[1])"
        )

        try:
            dropdown = WebDriverWait(driver, 25).until(
                EC.element_to_be_clickable(dropdown_locator)
            )

        except Exception:
            print("Login/session dropdown was not found.")
            print("Current page:", driver.current_url)
            save_screenshot(driver, "login_or_session_error")
            raise

        # Open the session dropdown
        dropdown.click()

        # Select the required session
        option_locator = (
            By.XPATH,
            "//li[normalize-space()='2026-2027 test2']"
        )

        try:
            option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )
            option.click()

        except Exception:
            print("The requested session option was not found.")
            save_screenshot(driver, "session_selection_error")
            raise

        time.sleep(2)

        # Give the logged-in browser to the test
        yield driver
        
        
    finally:
        driver.quit()