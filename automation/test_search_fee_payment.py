from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    TimeoutException
)
import time


def test_search_fee_payment(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    start_date_value = "21/08/2026"
    end_date_value = "31/08/2026"

    branch_value = "RTM,Marol(West),Mumbai-400021"
    department_value = "CSE-2026"
    program_value = "new-btech"
    semester_value = "Sem-3(CSE)"

    amount_value = "10000"

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
    # BRANCH
    # ----------------------------------------------------------

    empty_branch = ""
    space_branch = "     "
    invalid_branch = "Invalid Branch"

    # ----------------------------------------------------------
    # DEPARTMENT
    # ----------------------------------------------------------

    empty_department = ""
    space_department = "     "
    invalid_department = "Invalid Department"

    # ----------------------------------------------------------
    # PROGRAM
    # ----------------------------------------------------------

    empty_program = ""
    space_program = "     "
    invalid_program = "Invalid Program"

    # ----------------------------------------------------------
    # SEMESTER
    # ----------------------------------------------------------

    empty_semester = ""
    space_semester = "     "
    invalid_semester = "Invalid Semester"

    # ----------------------------------------------------------
    # AMOUNT
    # ----------------------------------------------------------

    empty_amount = ""
    space_amount = "     "
    zero_amount = "0"
    negative_amount = "-100"
    decimal_amount = "10000.50"
    alphabet_amount = "abc"
    special_amount = "@10000"
    large_amount = "999999999"
    valid_minimum_amount = "1"

    # ==========================================================
    # MAIN TEST DATA VALIDATION
    # ==========================================================

    assert start_date_value.strip(), \
        "Start date should not be empty"

    assert end_date_value.strip(), \
        "End date should not be empty"

    assert branch_value.strip(), \
        "Branch should not be empty"

    assert department_value.strip(), \
        "Department should not be empty"

    assert program_value.strip(), \
        "Program should not be empty"

    assert semester_value.strip(), \
        "Semester should not be empty"

    assert amount_value.strip(), \
        "Amount should not be empty"

    assert amount_value.isdigit(), \
        "Amount should contain only numbers"

    assert int(amount_value) > 0, \
        "Amount should be greater than zero"

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
        "End date before start date data is incorrect"

    # ----------------------------------------------------------
    # BRANCH EDGE DATA
    # ----------------------------------------------------------

    assert empty_branch == "", \
        "Empty branch data is incorrect"

    assert space_branch.strip() == "", \
        "Space branch data is incorrect"

    assert invalid_branch != branch_value, \
        "Invalid branch should be different"

    # ----------------------------------------------------------
    # DEPARTMENT EDGE DATA
    # ----------------------------------------------------------

    assert empty_department == "", \
        "Empty department data is incorrect"

    assert space_department.strip() == "", \
        "Space department data is incorrect"

    assert invalid_department != department_value, \
        "Invalid department should be different"

    # ----------------------------------------------------------
    # PROGRAM EDGE DATA
    # ----------------------------------------------------------

    assert empty_program == "", \
        "Empty program data is incorrect"

    assert space_program.strip() == "", \
        "Space program data is incorrect"

    assert invalid_program != program_value, \
        "Invalid program should be different"

    # ----------------------------------------------------------
    # SEMESTER EDGE DATA
    # ----------------------------------------------------------

    assert empty_semester == "", \
        "Empty semester data is incorrect"

    assert space_semester.strip() == "", \
        "Space semester data is incorrect"

    assert invalid_semester != semester_value, \
        "Invalid semester should be different"

    # ----------------------------------------------------------
    # AMOUNT EDGE DATA
    # ----------------------------------------------------------

    assert empty_amount == "", \
        "Empty amount data is incorrect"

    assert space_amount.strip() == "", \
        "Space amount data is incorrect"

    assert int(zero_amount) == 0, \
        "Zero amount data is incorrect"

    assert int(negative_amount) < 0, \
        "Negative amount data is incorrect"

    assert float(decimal_amount) > 0, \
        "Decimal amount data is incorrect"

    assert not alphabet_amount.isdigit(), \
        "Alphabet amount data is incorrect"

    assert special_amount != amount_value, \
        "Special amount data is incorrect"

    assert large_amount.isdigit(), \
        "Large amount data is incorrect"

    assert int(valid_minimum_amount) == 1, \
        "Minimum valid amount should be 1"

    # ==========================================================
    # OPEN FEES COLLECTION
    # ==========================================================

    fees_collection_menu = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div//span[normalize-space()='Fees Collection']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fees_collection_menu
    )

    time.sleep(1)

    try:

        fees_collection_menu.click()

    except ElementClickInterceptedException:

        driver.execute_script(
            "arguments[0].click();",
            fees_collection_menu
        )

    time.sleep(1)

    # ==========================================================
    # OPEN Search Fees Payment
    # ==========================================================

    fees_payment = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Search Fees Payment')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fees_payment
    )

    time.sleep(1)

    try:

        fees_payment.click()

    except ElementClickInterceptedException:

        driver.execute_script(
            "arguments[0].click();",
            fees_payment
        )

    time.sleep(3)

    # ==========================================================
    # VERIFY FEES COLLECT PAGE
    # ==========================================================

    assert driver.current_url, \
        "fees payment page was not opened"

        # ==========================================================
    # START DATE
    # ==========================================================

    start_date = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "date_from"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        start_date
    )

    time.sleep(1)

    assert start_date.is_enabled(), \
        "Start date field is disabled"

    # Convert DD/MM/YYYY -> YYYY-MM-DD
    start_date_browser_value = "-".join(
        reversed(start_date_value.split("/"))
    )

    # Set date using JavaScript
    driver.execute_script(
        """
        arguments[0].value = arguments[1];
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """,
        start_date,
        start_date_browser_value
    )

    time.sleep(1)

    # Verify entered date
    actual_start_date = start_date.get_attribute("value")

    assert actual_start_date == start_date_browser_value, \
        (
            f"Start date was not entered correctly. "
            f"Expected: '{start_date_browser_value}', "
            f"Actual: '{actual_start_date}'"
        )

    print(
        "Start date entered successfully:",
        actual_start_date
    )


    # ==========================================================
    # END DATE
    # ==========================================================

    end_date = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "date_to"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        end_date
    )

    time.sleep(1)

    assert end_date.is_enabled(), \
        "End date field is disabled"

    # Convert DD/MM/YYYY -> YYYY-MM-DD
    end_date_browser_value = "-".join(
        reversed(end_date_value.split("/"))
    )

    # Set date using JavaScript
    driver.execute_script(
        """
        arguments[0].value = arguments[1];
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """,
        end_date,
        end_date_browser_value
    )

    time.sleep(1)

    # Verify entered date
    actual_end_date = end_date.get_attribute("value")

    assert actual_end_date == end_date_browser_value, \
        (
            f"End date was not entered correctly. "
            f"Expected: '{end_date_browser_value}', "
            f"Actual: '{actual_end_date}'"
        )

    print(
        "End date entered successfully:",
        actual_end_date
    )
    
    #---STUDENT NAME----
    student_name = driver.find_element(By.NAME,"student_name")
    student_name.send_keys("ghch ccgcgf")
    
    #SEARCH BTN
    search = driver.find_element(By.ID,"feesPaymentSearchButton")
    search.click()

    