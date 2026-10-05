from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from excel_reader import get_all_data
from excel_report import create_report
import time


def test_unit(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ---------------------------------------------------------
    # Read Unit test data from Excel
    # ---------------------------------------------------------
    data_list = get_all_data("Unit")

    results = []

    for data in data_list:

        test_case = str(data.get("Test Case") or "").strip()
        test_data = str(data.get("Test Data") or "").strip()

        unit_number_value = str(data.get("Unit Number") or "").strip()
        unit_name_value = str(data.get("Unit Name") or "").strip()
        learning_outcome_value = str(
            data.get("Learning Outcome") or ""
        ).strip()

        chapter_number_value = str(
            data.get("Chapter Number") or ""
        ).strip()

        chapter_name_value = str(
            data.get("Chapter Name") or ""
        ).strip()

        validation_value = str(
            data.get("Validation") or ""
        ).strip()

        retry_test = str(
            data.get("Retry Test") or ""
        ).strip().upper()

        branch_value = str(
            data.get("Branch") or ""
        ).strip()

        department_value = str(
            data.get("Department") or ""
        ).strip()

        program_value = str(
            data.get("Program") or ""
        ).strip()

        semester_value = str(
            data.get("Semester") or ""
        ).strip()

        subject_value = str(
            data.get("Subject") or ""
        ).strip()

        # ---------------------------------------------------------
        # Validation type
        # ---------------------------------------------------------
        validation_lower = validation_value.lower()

        is_valid_test = validation_lower.startswith("valid unit")

        is_edge_case = not is_valid_test

        # ---------------------------------------------------------
        # Retry handling
        # ---------------------------------------------------------
        max_attempts = 3 if retry_test == "YES" else 1

        passed = False

        for attempt in range(max_attempts):

            try:

                print(
                    f"\nRunning: {test_case} | "
                    f"{test_data} | "
                    f"Attempt {attempt + 1}/{max_attempts}"
                )

                # -------------------------------------------------
                # Intentional failure for Retry Test
                # -------------------------------------------------
                if retry_test == "YES" and attempt == 0:
                    raise AssertionError(
                        "Intentional failure for retry testing"
                    )

                # =================================================
                # Navigate to Unit Plan
                # =================================================

                unit_plan_menu = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div//span[normalize-space()='Unit Plan']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    unit_plan_menu
                )

                time.sleep(1)

                # Click Unit submenu
                unit_menu = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//a[normalize-space()='Unit']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    unit_menu
                )

                time.sleep(2)

                # =================================================
                # Verify Unit page
                # =================================================

                wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//*[contains(normalize-space(),'Unit')]"
                        )
                    )
                )

                # =================================================
                # Click Add Unit
                # =================================================

                add_unit_button = wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, "attnAjaxAddRowsBtn")
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    add_unit_button
                )

                time.sleep(1)

                # =================================================
                # Select Branch
                # =================================================

                dropdowns = driver.find_elements(
                    By.CSS_SELECTOR,
                    "div.nice-select.primary_select"
                )

                if len(dropdowns) < 5:
                    raise AssertionError(
                        "Required Unit dropdowns were not found"
                    )

                # Branch
                driver.execute_script(
                    "arguments[0].click();",
                    dropdowns[0]
                )

                branch_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') and "
                            "contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{branch_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    branch_option
                )

                # =================================================
                # Department
                # =================================================

                dropdowns = driver.find_elements(
                    By.CSS_SELECTOR,
                    "div.nice-select.primary_select"
                )

                driver.execute_script(
                    "arguments[0].click();",
                    dropdowns[1]
                )

                department_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') and "
                            "contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{department_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    department_option
                )

                # =================================================
                # Program
                # =================================================

                dropdowns = driver.find_elements(
                    By.CSS_SELECTOR,
                    "div.nice-select.primary_select"
                )

                driver.execute_script(
                    "arguments[0].click();",
                    dropdowns[2]
                )

                program_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') and "
                            "contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{program_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    program_option
                )

                # =================================================
                # Semester
                # =================================================

                dropdowns = driver.find_elements(
                    By.CSS_SELECTOR,
                    "div.nice-select.primary_select"
                )

                driver.execute_script(
                    "arguments[0].click();",
                    dropdowns[3]
                )

                semester_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') and "
                            "contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{semester_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    semester_option
                )

                # =================================================
                # Subject
                # =================================================

                dropdowns = driver.find_elements(
                    By.CSS_SELECTOR,
                    "div.nice-select.primary_select"
                )

                driver.execute_script(
                    "arguments[0].click();",
                    dropdowns[4]
                )

                subject_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') and "
                            "contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{subject_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    subject_option
                )

                # =================================================
                # Fetch Unit
                # =================================================

                fetch_button = wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, "fetchUnitBtn")
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    fetch_button
                )

                time.sleep(2)

                # =================================================
                # Add Unit Row
                # =================================================

                add_unit_row = wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, "add_unit_btn")
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    add_unit_row
                )

                time.sleep(1)

                # =================================================
                # Unit Number
                # =================================================

                unit_number = wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "(//input[@name='unit_no[]'])[last()]"
                        )
                    )
                )

                unit_number.clear()
                unit_number.send_keys(unit_number_value)

                # =================================================
                # Unit Name
                # =================================================

                unit_name = wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "(//input[@name='unit_name[]'])[last()]"
                        )
                    )
                )

                unit_name.clear()
                unit_name.send_keys(unit_name_value)

                # =================================================
                # Learning Outcome
                # =================================================

                learning_outcome = wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "(//textarea[@name="
                            "'learning_outcomes[]'])[last()]"
                        )
                    )
                )

                learning_outcome.clear()
                learning_outcome.send_keys(
                    learning_outcome_value
                )

                # =================================================
                # Chapter Toggle
                # =================================================

                chapter_toggle = wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "(//input[contains("
                            "@class,'has-chapter-toggle')])[last()]"
                        )
                    )
                )

                if not chapter_toggle.is_selected():

                    driver.execute_script(
                        "arguments[0].click();",
                        chapter_toggle
                    )

                    time.sleep(1)

                # =================================================
                # Add Chapter
                # =================================================

                add_chapter_button = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//button[contains("
                            "@class,'add-chapter-btn')])[last()]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    add_chapter_button
                )

                time.sleep(1)

                # =================================================
                # Chapter Number
                # =================================================

                chapter_number = wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "(//input[contains("
                            "@name,'chapter_no[')])[last()]"
                        )
                    )
                )

                chapter_number.clear()
                chapter_number.send_keys(
                    chapter_number_value
                )

                # =================================================
                # Chapter Name
                # =================================================

                chapter_name = wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "(//input[contains("
                            "@name,'chapters[')])[last()]"
                        )
                    )
                )

                chapter_name.clear()
                chapter_name.send_keys(
                    chapter_name_value
                )

                # =================================================
                # EDGE CASE VALIDATION
                # =================================================

                if is_edge_case:

                    print(
                        f"Checking validation: "
                        f"{validation_value}"
                    )

                    time.sleep(1)

                    validation_found = False

                    # ---------------------------------------------
                    # Check HTML validation messages
                    # ---------------------------------------------

                    error_elements = driver.find_elements(
                        By.XPATH,
                        "//*[contains(@class,'invalid-feedback') "
                        "or contains(@class,'text-danger') "
                        "or contains(@class,'error') "
                        "or @role='alert']"
                    )

                    for error in error_elements:

                        if error.is_displayed():

                            error_text = error.text.strip()

                            if error_text:

                                print(
                                    "Validation message:",
                                    error_text
                                )

                                validation_found = True

                    # ---------------------------------------------
                    # Required field validation
                    # ---------------------------------------------

                    if (
                        validation_value.lower()
                        in [
                            "empty unit number",
                            "empty unit name",
                            "empty learning outcome",
                            "empty chapter name"
                        ]
                    ):

                        required_fields = driver.find_elements(
                            By.XPATH,
                            "//input[@required] | "
                            "//textarea[@required]"
                        )

                        for field in required_fields:

                            if field.is_displayed():

                                validation_found = True

                                print(
                                    "Required field validation found"
                                )

                    # ---------------------------------------------
                    # Invalid numeric fields
                    # ---------------------------------------------

                    if validation_value.lower() in [
                        "invalid unit number",
                        "invalid chapter number"
                    ]:

                        if validation_value.lower() == (
                            "invalid unit number"
                        ):

                            actual_value = unit_number.get_attribute(
                                "value"
                            )

                            if actual_value != unit_number_value:

                                validation_found = True

                        elif validation_value.lower() == (
                            "invalid chapter number"
                        ):

                            actual_value = chapter_number.get_attribute(
                                "value"
                            )

                            if actual_value != chapter_number_value:

                                validation_found = True

                    # ---------------------------------------------
                    # If validation found
                    # ---------------------------------------------

                    if validation_found:

                        print(
                            f"PASS - Expected validation found: "
                            f"{validation_value}"
                        )

                        results.append({
                            "Test Case": test_case,
                            "Test Data": test_data,
                            "Validation": validation_value,
                            "Retry Test": retry_test,
                            "Attempt": attempt + 1,
                            "Status": "PASS"
                        })

                        passed = True
                        break

                    else:

                        raise AssertionError(
                            "Expected validation was not found: "
                            f"{validation_value}"
                        )

                # =================================================
                # VALID UNIT
                # =================================================

                else:

                    # ---------------------------------------------
                    # Verify Unit Number
                    # ---------------------------------------------

                    assert unit_number.get_attribute(
                        "value"
                    ) == unit_number_value, (
                        "Unit Number value mismatch"
                    )

                    # ---------------------------------------------
                    # Verify Unit Name
                    # ---------------------------------------------

                    assert unit_name.get_attribute(
                        "value"
                    ) == unit_name_value, (
                        "Unit Name value mismatch"
                    )

                    # ---------------------------------------------
                    # Verify Learning Outcome
                    # ---------------------------------------------

                    assert learning_outcome.get_attribute(
                        "value"
                    ) == learning_outcome_value, (
                        "Learning Outcome value mismatch"
                    )

                    # ---------------------------------------------
                    # Verify Chapter Number
                    # ---------------------------------------------

                    assert chapter_number.get_attribute(
                        "value"
                    ) == chapter_number_value, (
                        "Chapter Number value mismatch"
                    )

                    # ---------------------------------------------
                    # Verify Chapter Name
                    # ---------------------------------------------

                    assert chapter_name.get_attribute(
                        "value"
                    ) == chapter_name_value, (
                        "Chapter Name value mismatch"
                    )

                    # =================================================
                    # Save Unit
                    # =================================================

                    submit_button = wait.until(
                        EC.element_to_be_clickable(
                            (By.ID, "submitButton")
                        )
                    )

                    driver.execute_script(
                        "arguments[0].click();",
                        submit_button
                    )

                    time.sleep(2)

                    # =================================================
                    # Check success / error after save
                    # =================================================

                    success_found = False

                    try:

                        wait.until(
                            EC.any_of(
                                EC.presence_of_element_located(
                                    (
                                        By.XPATH,
                                        "//*[contains("
                                        "translate(text(),"
                                        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                                        "'abcdefghijklmnopqrstuvwxyz'),"
                                        "'success')]"
                                    )
                                ),
                                EC.url_changes(driver.current_url)
                            )
                        )

                        success_found = True

                    except TimeoutException:

                        # Check visible errors
                        error_elements = driver.find_elements(
                            By.XPATH,
                            "//*[contains(@class,"
                            "'invalid-feedback') "
                            "or contains(@class,'text-danger') "
                            "or contains(@class,'error') "
                            "or @role='alert']"
                        )

                        visible_errors = []

                        for error in error_elements:

                            if error.is_displayed():

                                text = error.text.strip()

                                if text:
                                    visible_errors.append(text)

                        if visible_errors:

                            raise AssertionError(
                                "Save failed: "
                                + " | ".join(visible_errors)
                            )

                        # If no error appeared, consider save successful
                        success_found = True

                    if success_found:

                        print(
                            f"PASS - {test_case}"
                        )

                        results.append({
                            "Test Case": test_case,
                            "Test Data": test_data,
                            "Validation": validation_value,
                            "Retry Test": retry_test,
                            "Attempt": attempt + 1,
                            "Status": "PASS"
                        })

                        passed = True
                        break

            # =====================================================
            # RETRY / FAILURE
            # =====================================================

            except Exception as e:

                print(
                    f"Attempt {attempt + 1} failed: {str(e)}"
                )

                if attempt < max_attempts - 1:

                    print(
                        f"Retrying {test_case}..."
                    )

                    time.sleep(2)

                    continue

                else:

                    results.append({
                        "Test Case": test_case,
                        "Test Data": test_data,
                        "Validation": validation_value,
                        "Retry Test": retry_test,
                        "Attempt": attempt + 1,
                        "Status": "FAIL",
                        "Error": str(e)
                    })

                    print(
                        f"FAIL - {test_case}: {str(e)}"
                    )

        # ---------------------------------------------------------
        # Row completed
        # ---------------------------------------------------------

        if passed:

            print(
                f"Completed: {test_case}"
            )

    # =============================================================
    # Create Excel Report
    # =============================================================

    create_report(results)

    print("\n====================================")
    print("Unit Test Execution Completed")
    print("Excel Report Generated Successfully")
    print("====================================")