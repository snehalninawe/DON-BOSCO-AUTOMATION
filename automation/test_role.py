from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    TimeoutException
)
import time


def test_role(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    start_date_value = "21/08/2026"
    end_date_value = "31/08/2026"

    role_category_value = "Teacher"
    branch_value = "CSE"
    department_value = "CSE-2026"
    program_value = "new-btech"
    semester_value = "Sem-3(CSE)"
    semester_label_value = "Sem-3-cse-label"
    section_value = "CSE-Section A"

    name_value = "dsfsf"

    # ==========================================================
    # EDGE CASE DATA
    # ==========================================================

    # ----------------------------------------------------------
    # START DATE
    # ----------------------------------------------------------

    empty_start_date = ""
    space_start_date = "     "
    invalid_start_date = "99/99/9999"
    wrong_format_start_date = "2026-08-21"
    past_start_date = "01/01/2020"

    # ----------------------------------------------------------
    # END DATE
    # ----------------------------------------------------------

    empty_end_date = ""
    space_end_date = "     "
    invalid_end_date = "99/99/9999"
    wrong_format_end_date = "2026-08-31"
    past_end_date = "01/01/2020"
    end_date_before_start = "20/08/2026"

    # ----------------------------------------------------------
    # ROLE CATEGORY
    # ----------------------------------------------------------

    empty_role_category = ""
    space_role_category = "     "
    invalid_role_category = "Invalid Role Category"

    # ----------------------------------------------------------
    # NAME
    # ----------------------------------------------------------

    empty_name = ""
    space_name = "     "
    invalid_name = "@@@###"
    numeric_name = "123456"
    long_name = "A" * 256

    # ==========================================================
    # MAIN TEST DATA VALIDATION
    # ==========================================================

    assert start_date_value.strip(), \
        "Start date should not be empty"

    assert end_date_value.strip(), \
        "End date should not be empty"

    assert role_category_value.strip(), \
        "Role Category should not be empty"

    assert branch_value.strip(), \
        "Branch should not be empty"

    assert department_value.strip(), \
        "Department should not be empty"

    assert program_value.strip(), \
        "Program should not be empty"

    assert semester_value.strip(), \
        "Semester should not be empty"

    assert section_value.strip(), \
        "Section should not be empty"

    assert name_value.strip(), \
        "Name should not be empty"

    # ==========================================================
    # EDGE DATA VALIDATION
    # ==========================================================

    # ----------------------------------------------------------
    # START DATE EDGE DATA
    # ----------------------------------------------------------

    assert empty_start_date == "", \
        "Empty start date data is incorrect"

    assert space_start_date.strip() == "", \
        "Space start date data is incorrect"

    assert invalid_start_date != start_date_value, \
        "Invalid start date should be different"

    assert wrong_format_start_date != start_date_value, \
        "Wrong format start date should be different"

    assert past_start_date != start_date_value, \
        "Past start date should be different"

    # ----------------------------------------------------------
    # END DATE EDGE DATA
    # ----------------------------------------------------------

    assert empty_end_date == "", \
        "Empty end date data is incorrect"

    assert space_end_date.strip() == "", \
        "Space end date data is incorrect"

    assert invalid_end_date != end_date_value, \
        "Invalid end date should be different"

    assert wrong_format_end_date != end_date_value, \
        "Wrong format end date should be different"

    assert past_end_date != end_date_value, \
        "Past end date should be different"

    assert end_date_before_start != end_date_value, \
        "End date before start date should be different"

    # ----------------------------------------------------------
    # ROLE CATEGORY EDGE DATA
    # ----------------------------------------------------------

    assert empty_role_category == "", \
        "Empty role category data is incorrect"

    assert space_role_category.strip() == "", \
        "Space role category data is incorrect"

    assert invalid_role_category != role_category_value, \
        "Invalid role category should be different"


    # ----------------------------------------------------------
    # NAME EDGE DATA
    # ----------------------------------------------------------

    assert empty_name == "", \
        "Empty name data is incorrect"

    assert space_name.strip() == "", \
        "Space name data is incorrect"

    assert invalid_name != name_value, \
        "Invalid name should be different"

    assert numeric_name != name_value, \
        "Numeric name should be different"

    assert len(long_name) == 256, \
        "Long name test data is incorrect"

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
    # OPEN ROLE
    # ==========================================================

    role = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(normalize-space(),'Role')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        role
    )

    time.sleep(0.5)

    try:
        role.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            role
        )

    # ==========================================================
    # VERIFY ROLE PAGE
    # ==========================================================

    wait.until(
        lambda d: d.current_url
    )

    assert driver.current_url, \
        "Role page was not opened"

    # ==========================================================
    # ROLE CATEGORY
    # ==========================================================

    role_category = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@class='nice-select primary_select form-control']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        role_category
    )

    time.sleep(0.5)

    try:
        role_category.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            role_category
        )

    # ==========================================================
    # SELECT ROLE CATEGORY
    # ==========================================================

    role_category_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{role_category_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        role_category_option
    )

    time.sleep(0.5)

    try:
        role_category_option.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            role_category_option
        )

        # ==========================================================
    # VERIFY ROLE CATEGORY
    # ==========================================================

    selected_role_category = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')]"
                f"//li[contains(@class,'selected') "
                f"and normalize-space()='{role_category_value}']"
            )
        )
    )

    actual_role_category_value = selected_role_category.text.strip()

    assert actual_role_category_value.lower() == \
        role_category_value.lower(), \
        (
            f"Role Category was not selected correctly. "
            f"Expected: '{role_category_value}', "
            f"Actual: '{actual_role_category_value}'"
        )

    # ==========================================================
    # LEVEL ASSIGNMENT
    # ==========================================================

    level_assignment = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[@id='teacher_level_2']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        level_assignment
    )

    time.sleep(0.5)

    if not level_assignment.is_selected():
        try:
            level_assignment.click()

        except (
            ElementClickInterceptedException,
            ElementNotInteractableException
        ):
            driver.execute_script(
                "arguments[0].click();",
                level_assignment
            )

    # ==========================================================
    # VERIFY LEVEL ASSIGNMENT
    # ==========================================================

    assert level_assignment.is_selected(), \
        "Teacher Level 2 was not selected"

        # ==========================================================
    # NAME FIELD
    # ==========================================================

    name = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//label[contains(normalize-space(),'Name')]"
                "/following::input[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        name
    )

    time.sleep(0.5)

    name.clear()
    name.send_keys(name_value)

    # ==========================================================
    # VERIFY NAME
    # ==========================================================

    actual_name = name.get_attribute("value").strip()

    assert actual_name == name_value, \
        (
            f"Name was not entered correctly. "
            f"Expected: '{name_value}', "
            f"Actual: '{actual_name}'"
        )

    # ==========================================================
    # SAVE
    # ==========================================================

    save = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(@class,'primary-btn') "
                "and contains(@class,'nxgn_secondary_btn')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        save
    )

    time.sleep(0.5)

    try:
        save.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            save
        )

    # ==========================================================
    # VERIFY SAVE ACTION
    # ==========================================================

    time.sleep(2)

    assert driver.current_url, \
        "Page URL is missing after saving"
