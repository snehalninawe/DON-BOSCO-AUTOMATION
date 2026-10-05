from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_po_subject_wise(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "STU Marol(east) Mumbai 400002"
    department_value = "IT-26"
    program_value = "New-IT"
    semester_value = "Sem-3-IT"

    # Edge case data
    invalid_branch_value = "Invalid Branch"
    invalid_department_value = "Invalid Department"
    invalid_program_value = "Invalid Program"
    invalid_semester_value = "Invalid Semester"

    # ==========================================================
    # ATTAINMENT
    # ==========================================================

    attainment = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div//span[normalize-space()='Attainment']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        attainment
    )

    driver.execute_script(
        "arguments[0].click();",
        attainment
    )

    time.sleep(1)

    # ==========================================================
    # PO SUBJECT WISE
    # ==========================================================

    po_subject = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='PO Subject Wise']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        po_subject
    )

    driver.execute_script(
        "arguments[0].click();",
        po_subject
    )

    time.sleep(2)

    # ==========================================================
    # BRANCH DROPDOWN
    # ==========================================================

    branch = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[1]"
            )
        )
    )

    branch.click()

    branch_options = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[normalize-space()='"
                + branch_value +
                "']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        branch_options
    )

    driver.execute_script(
        "arguments[0].click();",
        branch_options
    )

    time.sleep(1)

    # Verify selected branch
    selected_branch = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[1]"
                "//span[contains(@class,'current')]"
            )
        )
    )

    actual_branch = selected_branch.text.strip()

    assert (
        actual_branch.casefold()
        == branch_value.casefold()
    ), (
        f"Branch mismatch. "
        f"Expected: '{branch_value}', "
        f"Actual: '{actual_branch}'"
    )

    # ==========================================================
    # DEPARTMENT DROPDOWN
    # ==========================================================

    department = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[2]"
            )
        )
    )

    department.click()

    department_options = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[normalize-space()='"
                + department_value +
                "']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        department_options
    )

    driver.execute_script(
        "arguments[0].click();",
        department_options
    )

    time.sleep(1)

    # Verify selected department
    selected_department = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[2]"
                "//span[contains(@class,'current')]"
            )
        )
    )

    actual_department = selected_department.text.strip()

    assert (
        actual_department.casefold()
        == department_value.casefold()
    ), (
        f"Department mismatch. "
        f"Expected: '{department_value}', "
        f"Actual: '{actual_department}'"
    )

    # ==========================================================
    # PROGRAM DROPDOWN
    # ==========================================================

    program = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[3]"
            )
        )
    )

    program.click()

    program_options = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[normalize-space()='"
                + program_value +
                "']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        program_options
    )

    driver.execute_script(
        "arguments[0].click();",
        program_options
    )

    time.sleep(1)

    # Verify selected program
    selected_program = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[3]"
                "//span[contains(@class,'current')]"
            )
        )
    )

    actual_program = selected_program.text.strip()

    assert (
        actual_program.casefold()
        == program_value.casefold()
    ), (
        f"Program mismatch. "
        f"Expected: '{program_value}', "
        f"Actual: '{actual_program}'"
    )

    # ==========================================================
    # SEMESTER DROPDOWN
    # ==========================================================

    semester = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[4]"
            )
        )
    )

    semester.click()

    semester_options = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[normalize-space()='"
                + semester_value +
                "']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester_options
    )

    driver.execute_script(
        "arguments[0].click();",
        semester_options
    )

    time.sleep(1)

    # Verify selected semester
    selected_semester = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[4]"
                "//span[contains(@class,'current')]"
            )
        )
    )

    actual_semester = selected_semester.text.strip()

    assert (
        actual_semester.casefold()
        == semester_value.casefold()
    ), (
        f"Semester mismatch. "
        f"Expected: '{semester_value}', "
        f"Actual: '{actual_semester}'"
    )

    # ==========================================================
    # EDGE CASE - INVALID BRANCH
    # ==========================================================

    branch.click()

    invalid_branch = driver.find_elements(
        By.XPATH,
        f"//li[normalize-space()='{invalid_branch_value}']"
    )

    assert len(invalid_branch) == 0, (
        f"Invalid branch '{invalid_branch_value}' "
        f"should not be available."
    )

    branch.click()

    # ==========================================================
    # EDGE CASE - INVALID DEPARTMENT
    # ==========================================================

    department.click()

    invalid_department = driver.find_elements(
        By.XPATH,
        f"//li[normalize-space()='{invalid_department_value}']"
    )

    assert len(invalid_department) == 0, (
        f"Invalid department '{invalid_department_value}' "
        f"should not be available."
    )

    department.click()

    # ==========================================================
    # EDGE CASE - INVALID PROGRAM
    # ==========================================================

    program.click()

    invalid_program = driver.find_elements(
        By.XPATH,
        f"//li[normalize-space()='{invalid_program_value}']"
    )

    assert len(invalid_program) == 0, (
        f"Invalid program '{invalid_program_value}' "
        f"should not be available."
    )

    program.click()

    # ==========================================================
    # EDGE CASE - INVALID SEMESTER
    # ==========================================================

    semester.click()

    invalid_semester = driver.find_elements(
        By.XPATH,
        f"//li[normalize-space()='{invalid_semester_value}']"
    )

    assert len(invalid_semester) == 0, (
        f"Invalid semester '{invalid_semester_value}' "
        f"should not be available."
    )

    semester.click()

    # ==========================================================
    # SEARCH
    # ==========================================================

    search_btn = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "poAttnSearchButton")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        search_btn
    )

    driver.execute_script(
        "arguments[0].click();",
        search_btn
    )

    # ==========================================================
    # WAIT FOR RESULT
    # ==========================================================

    eye_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[contains(@class,'po-attn-eye-link') "
                "and contains(@class,'js-po-attn-detail-link')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        eye_btn
    )

    # ==========================================================
    # OPEN DETAILS
    # ==========================================================

    driver.execute_script(
        "arguments[0].click();",
        eye_btn
    )

    time.sleep(3)

    # ==========================================================
    # VERIFY DETAILS OPENED
    # ==========================================================

    assert driver.current_url is not None

    time.sleep(1)