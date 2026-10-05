from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time


def test_subject(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "RTM,Marol(West),Mumbai-400021"
    department_value = "CSE-2026"
    program_value = "new-btech"
    semester_value = "Sem-3(CSE)"
    target_section_value = "CSE-Section A"

    student_checkbox_id = "student_record_3357"

    # ==========================================================
    # TEST DATA VALIDATION
    # ==========================================================

    assert branch_value.strip(), \
        "Branch value should not be empty"

    assert department_value.strip(), \
        "Department value should not be empty"

    assert program_value.strip(), \
        "Program value should not be empty"

    assert semester_value.strip(), \
        "Semester value should not be empty"

    assert target_section_value.strip(), \
        "Target section should not be empty"

    # ==========================================================
    # OPEN STUDENT INFO
    # ==========================================================

    student_info_menu = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div//span[normalize-space()='Student Info']"
            )
        )
    )

    student_info_menu.click()

    time.sleep(1)

    # ==========================================================
    # OPEN STUDENT PROMOTION
    # ==========================================================

    student_add_modify = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Student Promotion')])[2]"
            )
        )
    )

    student_add_modify.click()

    time.sleep(2)

    # ==========================================================
    # BRANCH
    # ==========================================================

    branch_dropdown = wait.until(
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
        branch_dropdown
    )

    time.sleep(1)

    branch_dropdown.click()

    time.sleep(1)

    branch_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//div[contains(@class,'nice-select') "
                f"and contains(@class,'open')]"
                f"//li[normalize-space()='{branch_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        branch_option
    )

    branch_option.click()

    time.sleep(1)

    actual_branch = branch_dropdown.text.strip()

    assert actual_branch.lower() == branch_value.lower(), \
        (
            f"Branch was not selected correctly. "
            f"Expected: '{branch_value}', "
            f"Actual: '{actual_branch}'"
        )

    # ==========================================================
    # DEPARTMENT
    # ==========================================================

    department_dropdown = wait.until(
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
        department_dropdown
    )

    time.sleep(1)

    department_dropdown.click()

    time.sleep(1)

    department_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//div[contains(@class,'nice-select') "
                f"and contains(@class,'open')]"
                f"//li[normalize-space()='{department_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        department_option
    )

    department_option.click()

    time.sleep(1)

    actual_department = department_dropdown.text.strip()

    assert actual_department.lower() == department_value.lower(), \
        (
            f"Department was not selected correctly. "
            f"Expected: '{department_value}', "
            f"Actual: '{actual_department}'"
        )

    # ==========================================================
    # PROGRAM
    # ==========================================================

    program_dropdown = wait.until(
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
        program_dropdown
    )

    time.sleep(1)

    program_dropdown.click()

    time.sleep(1)

    program_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//div[contains(@class,'nice-select') "
                f"and contains(@class,'open')]"
                f"//li[normalize-space(translate("
                f".,"
                f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                f"'abcdefghijklmnopqrstuvwxyz'"
                f"))='{program_value.lower()}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        program_option
    )

    time.sleep(1)

    program_option.click()

    time.sleep(1)

    actual_program = program_dropdown.text.strip()

    assert actual_program.lower() == program_value.lower(), \
        (
            f"Program was not selected correctly. "
            f"Expected: '{program_value}', "
            f"Actual: '{actual_program}'"
        )

    # ==========================================================
    # SEMESTER
    # ==========================================================

    semester_dropdown = wait.until(
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
        semester_dropdown
    )

    time.sleep(1)

    semester_dropdown.click()

    time.sleep(1)

    semester_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//div[contains(@class,'nice-select') "
                f"and contains(@class,'open')]"
                f"//li[normalize-space()='{semester_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester_option
    )

    semester_option.click()

    time.sleep(1)

    actual_semester = semester_dropdown.text.strip()

    assert actual_semester.lower() == semester_value.lower(), \
        (
            f"Semester was not selected correctly. "
            f"Expected: '{semester_value}', "
            f"Actual: '{actual_semester}'"
        )

        # ==========================================================
    # SEARCH STUDENT
    # ==========================================================

    search = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "promotionSearchButton"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        search
    )

    time.sleep(1)

    search.click()

    time.sleep(3)

    # ==========================================================
    # SCROLL TO BOTTOM
    # ==========================================================

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(1)

        # ==========================================================
    # SELECT STUDENT CHECKBOX
    # ==========================================================

    student_checkbox = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                student_checkbox_id
            )
        )
    )

    # Scroll to checkbox
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        student_checkbox
    )

    time.sleep(1)

    # Check current status
    print(
        "Checkbox found:",
        student_checkbox.get_attribute("id")
    )

    print(
        "Checkbox selected:",
        student_checkbox.is_selected()
    )

    # ==========================================================
    # CLICK CHECKBOX
    # ==========================================================

    if not student_checkbox.is_selected():

        driver.execute_script(
            """
            arguments[0].click();
            """,
            student_checkbox
        )

        time.sleep(1)

    # ==========================================================
    # VERIFY CHECKBOX
    # ==========================================================

    student_checkbox = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                student_checkbox_id
            )
        )
    )

    assert student_checkbox.is_selected(), \
        "Student checkbox was not selected"

    print(
        "Student checkbox selected successfully"
    )

    # ==========================================================
    # OPEN PROMOTION MODAL
    # ==========================================================

    promote_student = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "openPromotionModalButton"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        promote_student
    )

    time.sleep(1)

    try:
        promote_student.click()

    except ElementClickInterceptedException:

        driver.execute_script(
            "arguments[0].click();",
            promote_student
        )

    time.sleep(2)

    # ==========================================================
    # VERIFY PROMOTION MODAL
    # ==========================================================

    promotion_modal = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'modal') "
                "and contains(@class,'show')]"
            )
        )
    )

    assert promotion_modal.is_displayed(), \
        "Student promotion modal was not displayed"
        
    driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
    
    time.sleep(1)

    # ==========================================================
    # TARGET SECTION
    # ==========================================================

    target_section_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@class='nice-select primary_select form-control w-100']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        target_section_dropdown
    )

    time.sleep(1)

    target_section_dropdown.click()

    time.sleep(1)

    # ==========================================================
    # TARGET SECTION OPTION
    # ==========================================================

    target_section_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//div[contains(@class,'nice-select') "
                f"and contains(@class,'open')]"
                f"//li[normalize-space(translate("
                f".,"
                f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                f"'abcdefghijklmnopqrstuvwxyz'"
                f"))='{target_section_value.lower()}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        target_section_option
    )

    time.sleep(1)

    target_section_option.click()

    time.sleep(1)

    # ==========================================================
    # VERIFY TARGET SECTION
    # ==========================================================

    actual_target_section = target_section_dropdown.text.strip()

    assert actual_target_section.lower() == target_section_value.lower(), \
        (
            f"Target section was not selected correctly. "
            f"Expected: '{target_section_value}', "
            f"Actual: '{actual_target_section}'"
        )

    # ==========================================================
    # PROMOTE SELECTED STUDENT
    # ==========================================================

    submit_promotion = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "submitStudentPromotionButton"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        submit_promotion
    )

    time.sleep(1)

    try:
        submit_promotion.click()

    except ElementClickInterceptedException:

        driver.execute_script(
            "arguments[0].click();",
            submit_promotion
        )

    time.sleep(3)

    # ==========================================================
    # VERIFY PROMOTION SUCCESS
    # ==========================================================

    success_message = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(@class,'alert-success') "
                "or contains(@class,'swal2-success') "
                "or contains(@class,'toast-success')]"
            )
        )
    )

    assert success_message.is_displayed(), \
        "Student promotion success message was not displayed"

    print(
        "Student selected and promoted successfully"
    )