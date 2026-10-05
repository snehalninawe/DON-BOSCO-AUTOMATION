from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    TimeoutException
)
import time


def test_login_permission(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    role_value = "Teacher"

    # ==========================================================
    # EDGE CASE DATA
    # ==========================================================

    # ----------------------------------------------------------
    # ROLE
    # ----------------------------------------------------------

    empty_role = ""
    space_role = "     "
    invalid_role = "Invalid Role"
    numeric_role = "123456"
    special_role = "@@@###"
    long_role = "A" * 256

    # ==========================================================
    # MAIN TEST DATA VALIDATION
    # ==========================================================

    assert role_value.strip(), \
        "Role should not be empty"

    # ==========================================================
    # EDGE DATA VALIDATION
    # ==========================================================

    assert empty_role == "", \
        "Empty role data is incorrect"

    assert space_role.strip() == "", \
        "Space role data is incorrect"

    assert invalid_role != role_value, \
        "Invalid role should be different"

    assert numeric_role != role_value, \
        "Numeric role should be different"

    assert special_role != role_value, \
        "Special character role should be different"

    assert len(long_role) == 256, \
        "Long role data is incorrect"

    # ==========================================================
    # OPEN ROLE & PERMISSION
    # ==========================================================

    role_permission_menu = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div//span[normalize-space()='Role & Permission']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        role_permission_menu
    )

    time.sleep(0.5)

    try:
        role_permission_menu.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            role_permission_menu
        )

    # ==========================================================
    # OPEN LOGIN PERMISSION
    # ==========================================================

    login_permission = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(normalize-space(),'Login Permission')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        login_permission
    )

    time.sleep(0.5)

    try:
        login_permission.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            login_permission
        )

    # ==========================================================
    # VERIFY LOGIN PERMISSION PAGE
    # ==========================================================

    select_role = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select') "
                "and contains(@class,'form-control')])[1]"
            )
        )
    )

    assert select_role.is_displayed(), \
        "Login Permission page was not opened"

    # ==========================================================
    # SELECT ROLE DROPDOWN
    # ==========================================================

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        select_role
    )

    time.sleep(0.5)

    try:
        select_role.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            select_role
        )

    # ==========================================================
    # VERIFY DROPDOWN IS OPEN
    # ==========================================================

    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
            )
        )
    )

    # ==========================================================
    # VERIFY ROLE OPTION EXISTS
    # ==========================================================

    role_option = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{role_value}']"
            )
        )
    )

    assert role_option.is_displayed(), \
        f"Role '{role_value}' is not displayed in dropdown"

    # ==========================================================
    # SELECT ROLE
    # ==========================================================

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        role_option
    )

    time.sleep(0.5)

    try:
        role_option.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            role_option
        )

    # ==========================================================
    # VERIFY ROLE SELECTION
    # ==========================================================

    selected_role = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')]"
                f"//li[contains(@class,'selected') "
                f"and normalize-space()='{role_value}']"
            )
        )
    )

    actual_role = selected_role.text.strip()

    assert actual_role.lower() == role_value.lower(), \
        (
            f"Role was not selected correctly. "
            f"Expected: '{role_value}', "
            f"Actual: '{actual_role}'"
        )

    assert actual_role.strip(), \
        "Selected role should not be empty"

    # ==========================================================
    # SEARCH BUTTON
    # ==========================================================

    search = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(@class,'primary-btn') "
                "and contains(@class,'small') "
                "and contains(@class,'fix-gr-bg')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        search
    )

    time.sleep(0.5)

    assert search.is_enabled(), \
        "Search button should be enabled"

    try:
        search.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            search
        )

    # ==========================================================
    # VERIFY SEARCH RESULT
    # ==========================================================

    try:

        search_result = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//table//tbody//tr"
                )
            )
        )

        assert search_result.is_displayed(), \
            f"Search result for role '{role_value}' is not displayed"

    except TimeoutException:

        assert False, \
            f"No search result found for role '{role_value}'"

    # ==========================================================
    # VERIFY ROLE IN SEARCH RESULT
    # ==========================================================

    role_in_result = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//table//tbody//tr"
                f"[contains(normalize-space(),'{role_value}')]"
            )
        )
    )

    assert role_in_result.is_displayed(), \
        f"Role '{role_value}' was not found in search result"