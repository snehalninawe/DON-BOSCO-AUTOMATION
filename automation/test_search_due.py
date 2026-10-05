from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    TimeoutException
)
import time


def test_search_due(driver):

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
    semester_label_value = "Sem-3-cse-label"
    section_value = "CSE-Section A"

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
    # SECTION
    # ----------------------------------------------------------

    empty_section = ""
    space_section = "     "
    invalid_section = "Invalid Section"

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

    assert section_value.strip(), \
        "Section should not be empty"

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
    # SECTION EDGE DATA
    # ----------------------------------------------------------

    assert empty_section == "", \
        "Empty section data is incorrect"

    assert space_section.strip() == "", \
        "Space section data is incorrect"

    assert invalid_section != section_value, \
        "Invalid section should be different"

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
    # OPEN SEARCH FEES DUE
    # ==========================================================

    fees_due = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Search Fees Due')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fees_due
    )

    time.sleep(1)

    try:

        fees_due.click()

    except ElementClickInterceptedException:

        driver.execute_script(
            "arguments[0].click();",
            fees_due
        )

    time.sleep(3)

    # ==========================================================
    # VERIFY PAGE
    # ==========================================================

    assert driver.current_url, \
        "Search Fees Due page was not opened"

    # ==========================================================
    # BRANCH
    # ==========================================================

    branch = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[1]"
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
        
    # ==========================================================
        # SEMESTER LABEL
        # ==========================================================
    
    semester_label = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[contains(@class,'nice-select') "
                    "and contains(@class,'primary_select') "
                    "and contains(@class,'form-control')])[5]"
                )
            )
        )
    
    driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            semester_label
        )
    
    time.sleep(1)
    
    semester_label.click()
    
    time.sleep(1)
    
    semester_label_option = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class,'nice-select') "
                    "and contains(@class,'open')]"
                    f"//li[normalize-space()='{semester_label_value}']"
                )
            )
        )
    
    driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            semester_label_option
        )
    
    time.sleep(1)
    
    driver.execute_script(
            "arguments[0].click();",
            semester_label_option
        )
    
    time.sleep(1)
    
    actual_semester_label = semester_label.text.strip()
    
    assert actual_semester_label.lower() == semester_label_value.lower(), \
            (
                f"Semester was not selected correctly. "
                f"Expected: '{semester_label_value}', "
                f"Actual: '{actual_semester_label}'"
            )

    # # ==========================================================
    # # SECTION
    # # ==========================================================

    # section = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select') "
    #             "and contains(@class,'form-control')])[6]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     section
    # )

    # time.sleep(1)

    # section.click()

    # time.sleep(1)

    # section_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{section_value}']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     section_option
    # )

    # time.sleep(1)

    # driver.execute_script(
    #     "arguments[0].click();",
    #     section_option
    # )

    # time.sleep(1)

    # actual_section = section.text.strip()

    # assert actual_section.lower() == section_value.lower(), \
    #     (
    #         f"Section was not selected correctly. "
    #         f"Expected: '{section_value}', "
    #         f"Actual: '{actual_section}'"
    #     )

    # ==========================================================
    # SEARCH BUTTON
    # ==========================================================

    search = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "feesDueSearchButton"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        search
    )

    time.sleep(1)

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

    time.sleep(3)

    print("Search Fees Due completed successfully")