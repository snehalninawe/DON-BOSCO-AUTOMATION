from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    TimeoutException
)
import time


def test_fee_collect(driver):

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
    # OPEN FEES COLLECT
    # ==========================================================

    fees_collect = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Fees Collect')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fees_collect
    )

    time.sleep(1)

    try:

        fees_collect.click()

    except ElementClickInterceptedException:

        driver.execute_script(
            "arguments[0].click();",
            fees_collect
        )

    time.sleep(3)

    # ==========================================================
    # VERIFY FEES COLLECT PAGE
    # ==========================================================

    assert driver.current_url, \
        "Fees Collect page was not opened"

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
    # ==========================================================
    # BRANCH
    # ==========================================================

    branch = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select') "
                "and contains(@class,'form-control')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        branch
    )

    time.sleep(1)

    branch.click()

    time.sleep(1)

    branch_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{branch_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        branch_option
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        branch_option
    )

    time.sleep(1)

    actual_branch = branch.text.strip()

    assert actual_branch.lower() == branch_value.lower(), \
        (
            f"Branch was not selected correctly. "
            f"Expected: '{branch_value}', "
            f"Actual: '{actual_branch}'"
        )

    # ==========================================================
    # DEPARTMENT
    # ==========================================================

    department = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select') "
                "and contains(@class,'form-control')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        department
    )

    time.sleep(1)

    department.click()

    time.sleep(1)

    department_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{department_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        department_option
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        department_option
    )

    time.sleep(1)

    actual_department = department.text.strip()

    assert actual_department.lower() == department_value.lower(), \
        (
            f"Department was not selected correctly. "
            f"Expected: '{department_value}', "
            f"Actual: '{actual_department}'"
        )

    # ==========================================================
    # PROGRAM
    # ==========================================================

    program = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select') "
                "and contains(@class,'form-control')])[3]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        program
    )

    time.sleep(1)

    program.click()

    time.sleep(1)

    program_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{program_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        program_option
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        program_option
    )

    time.sleep(1)

    actual_program = program.text.strip()

    assert actual_program.lower() == program_value.lower(), \
        (
            f"Program was not selected correctly. "
            f"Expected: '{program_value}', "
            f"Actual: '{actual_program}'"
        )

    # ==========================================================
    # SEMESTER
    # ==========================================================

    semester = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select') "
                "and contains(@class,'form-control')])[4]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester
    )

    time.sleep(1)

    semester.click()

    time.sleep(1)

    semester_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{semester_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester_option
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        semester_option
    )

    time.sleep(1)

    actual_semester = semester.text.strip()

    assert actual_semester.lower() == semester_value.lower(), \
        (
            f"Semester was not selected correctly. "
            f"Expected: '{semester_value}', "
            f"Actual: '{actual_semester}'"
        )
    
    #SEARCH BTN
    search = driver.find_element(By.ID,"feesCollectSearchButton")
    search.click()

    # # ==========================================================
    # # COLLECT FEES BUTTON
    # # ==========================================================

    # collect_fees_btn = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//a[contains(@class,'primary-btn') "
    #             "and contains(@class,'fix-gr-bg')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     collect_fees_btn
    # )

    # time.sleep(1)

    # wait.until(
    #     EC.visibility_of(
    #         collect_fees_btn
    #     )
    # )

    # try:

    #     collect_fees_btn.click()

    # except (
    #     ElementClickInterceptedException,
    #     ElementNotInteractableException
    # ):

    #     driver.execute_script(
    #         "arguments[0].click();",
    #         collect_fees_btn
    #     )

    # time.sleep(3)

    # # ==========================================================
    # # ADD FEES BUTTON
    # # ==========================================================

    # add_fees = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.ID,
    #             "feesCollectAddButton"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     add_fees
    # )

    # time.sleep(1)

    # wait.until(
    #     EC.visibility_of(
    #         add_fees
    #     )
    # )

    # try:

    #     add_fees.click()

    # except (
    #     ElementClickInterceptedException,
    #     ElementNotInteractableException
    # ):

    #     driver.execute_script(
    #         "arguments[0].click();",
    #         add_fees
    #     )

    # time.sleep(2)

    # # ==========================================================
    # # VERIFY AMOUNT FIELD
    # # ==========================================================

    # amount = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.ID,
    #             "amount"
    #         )
    #     )
    # )

    # assert amount.is_displayed(), \
    #     "Amount field is not displayed"

    # assert amount.is_enabled(), \
    #     "Amount field is disabled"

    # # ==========================================================
    # # ENTER AMOUNT
    # # ==========================================================

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     amount
    # )

    # time.sleep(1)

    # amount.clear()

    # amount.send_keys(
    #     amount_value
    # )

    # time.sleep(1)

    # # ==========================================================
    # # VERIFY AMOUNT
    # # ==========================================================

    # actual_amount = amount.get_attribute("value")

    # assert actual_amount == amount_value, \
    #     (
    #         f"Amount was not entered correctly. "
    #         f"Expected: '{amount_value}', "
    #         f"Actual: '{actual_amount}'"
    #     )

    # print(
    #     "Amount entered successfully:",
    #     actual_amount
    # )

    # # ==========================================================
    # # SAVE
    # # ==========================================================

    # save = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.ID,
    #             "saveFeesButton"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     save
    # )

    # time.sleep(1)

    # wait.until(
    #     EC.visibility_of(
    #         save
    #     )
    # )

    # try:

    #     wait.until(
    #         EC.element_to_be_clickable(
    #             (
    #                 By.ID,
    #                 "saveFeesButton"
    #             )
    #         )
    #     ).click()

    # except (
    #     ElementClickInterceptedException,
    #     ElementNotInteractableException
    # ):

    #     driver.execute_script(
    #         "arguments[0].click();",
    #         save
    #     )

    # time.sleep(3)

    # # ==========================================================
    # # VERIFY SUCCESS MESSAGE
    # # ==========================================================

    # try:

    #     success_message = wait.until(
    #         EC.visibility_of_element_located(
    #             (
    #                 By.XPATH,
    #                 "//*[contains(@class,'alert-success') "
    #                 "or contains(@class,'toast-success') "
    #                 "or contains(@class,'swal2-success')]"
    #             )
    #         )
    #     )

    #     assert success_message.is_displayed(), \
    #         "Fee collection success message was not displayed"

    #     print(
    #         "Fee collected successfully"
    #     )

    # except TimeoutException:

    #     # ======================================================
    #     # CHECK VALIDATION / ERROR MESSAGE
    #     # ======================================================

    #     error_messages = driver.find_elements(
    #         By.XPATH,
    #         "//*[contains(@class,'alert-danger') "
    #         "or contains(@class,'toast-error') "
    #         "or contains(@class,'invalid-feedback') "
    #         "or contains(@class,'error')]"
    #     )

    #     visible_error_found = False

    #     for error in error_messages:

    #         if error.is_displayed():

    #             visible_error_found = True

    #             print(
    #                 "Fee collection error:",
    #                 error.text
    #             )

    #     assert visible_error_found is False, \
    #         "Fee collection failed with an error message"

    #     raise AssertionError(
    #         "Fee collection success message was not displayed"
    #     )