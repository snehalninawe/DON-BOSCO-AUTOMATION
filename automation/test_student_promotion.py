# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import ElementClickInterceptedException
# import time


# def test_subject(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 20)

#     # ==========================================================
#     # TEST DATA
#     # ==========================================================

#     branch_value = "RTM,Marol(West),Mumbai-400021"
#     department_value = "CSE-2026"
#     program_value = "new-btech"
#     semester_value = "Sem-3(CSE)"
#     target_section_value = "CSE-Section A"

#     student_checkbox_id = "student_record_3357"

#     # ==========================================================
#     # TEST DATA VALIDATION
#     # ==========================================================

#     assert branch_value.strip(), \
#         "Branch value should not be empty"

#     assert department_value.strip(), \
#         "Department value should not be empty"

#     assert program_value.strip(), \
#         "Program value should not be empty"

#     assert semester_value.strip(), \
#         "Semester value should not be empty"

#     assert target_section_value.strip(), \
#         "Target section should not be empty"

#     # ==========================================================
#     # OPEN STUDENT INFO
#     # ==========================================================

#     student_info_menu = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//div//span[normalize-space()='Student Info']"
#             )
#         )
#     )

#     student_info_menu.click()

#     time.sleep(1)

#     # ==========================================================
#     # OPEN STUDENT PROMOTION
#     # ==========================================================

#     student_add_modify = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//li[contains(.,'Student Promotion')])[2]"
#             )
#         )
#     )

#     student_add_modify.click()

#     time.sleep(2)

#     # ==========================================================
#     # BRANCH
#     # ==========================================================

#     branch_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select') "
#                 "and contains(@class,'form-control')])[1]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         branch_dropdown
#     )

#     time.sleep(1)

#     branch_dropdown.click()

#     time.sleep(1)

#     branch_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//div[contains(@class,'nice-select') "
#                 f"and contains(@class,'open')]"
#                 f"//li[normalize-space()='{branch_value}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         branch_option
#     )

#     branch_option.click()

#     time.sleep(1)

#     actual_branch = branch_dropdown.text.strip()

#     assert actual_branch.lower() == branch_value.lower(), \
#         (
#             f"Branch was not selected correctly. "
#             f"Expected: '{branch_value}', "
#             f"Actual: '{actual_branch}'"
#         )

#     # ==========================================================
#     # DEPARTMENT
#     # ==========================================================

#     department_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select') "
#                 "and contains(@class,'form-control')])[2]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         department_dropdown
#     )

#     time.sleep(1)

#     department_dropdown.click()

#     time.sleep(1)

#     department_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//div[contains(@class,'nice-select') "
#                 f"and contains(@class,'open')]"
#                 f"//li[normalize-space()='{department_value}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         department_option
#     )

#     department_option.click()

#     time.sleep(1)

#     actual_department = department_dropdown.text.strip()

#     assert actual_department.lower() == department_value.lower(), \
#         (
#             f"Department was not selected correctly. "
#             f"Expected: '{department_value}', "
#             f"Actual: '{actual_department}'"
#         )

#     # ==========================================================
#     # PROGRAM
#     # ==========================================================

#     program_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select') "
#                 "and contains(@class,'form-control')])[3]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         program_dropdown
#     )

#     time.sleep(1)

#     program_dropdown.click()

#     time.sleep(1)

#     program_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//div[contains(@class,'nice-select') "
#                 f"and contains(@class,'open')]"
#                 f"//li[normalize-space(translate("
#                 f".,"
#                 f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
#                 f"'abcdefghijklmnopqrstuvwxyz'"
#                 f"))='{program_value.lower()}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         program_option
#     )

#     time.sleep(1)

#     program_option.click()

#     time.sleep(1)

#     actual_program = program_dropdown.text.strip()

#     assert actual_program.lower() == program_value.lower(), \
#         (
#             f"Program was not selected correctly. "
#             f"Expected: '{program_value}', "
#             f"Actual: '{actual_program}'"
#         )

#     # ==========================================================
#     # SEMESTER
#     # ==========================================================

#     semester_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select') "
#                 "and contains(@class,'form-control')])[4]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         semester_dropdown
#     )

#     time.sleep(1)

#     semester_dropdown.click()

#     time.sleep(1)

#     semester_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//div[contains(@class,'nice-select') "
#                 f"and contains(@class,'open')]"
#                 f"//li[normalize-space()='{semester_value}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         semester_option
#     )

#     semester_option.click()

#     time.sleep(1)

#     actual_semester = semester_dropdown.text.strip()

#     assert actual_semester.lower() == semester_value.lower(), \
#         (
#             f"Semester was not selected correctly. "
#             f"Expected: '{semester_value}', "
#             f"Actual: '{actual_semester}'"
#         )

#         # ==========================================================
#     # SEARCH STUDENT
#     # ==========================================================

#     search = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "promotionSearchButton"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         search
#     )

#     time.sleep(1)

#     search.click()

#     time.sleep(3)

#     # ==========================================================
#     # SCROLL TO BOTTOM
#     # ==========================================================

#     driver.execute_script(
#         "window.scrollTo(0, document.body.scrollHeight);"
#     )

#     time.sleep(1)

#         # ==========================================================
#     # SELECT STUDENT CHECKBOX
#     # ==========================================================

#     student_checkbox = wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.ID,
#                 student_checkbox_id
#             )
#         )
#     )

#     # Scroll to checkbox
#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         student_checkbox
#     )

#     time.sleep(1)

#     # Check current status
#     print(
#         "Checkbox found:",
#         student_checkbox.get_attribute("id")
#     )

#     print(
#         "Checkbox selected:",
#         student_checkbox.is_selected()
#     )

#     # ==========================================================
#     # CLICK CHECKBOX
#     # ==========================================================

#     if not student_checkbox.is_selected():

#         driver.execute_script(
#             """
#             arguments[0].click();
#             """,
#             student_checkbox
#         )

#         time.sleep(1)

#     # ==========================================================
#     # VERIFY CHECKBOX
#     # ==========================================================

#     student_checkbox = wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.ID,
#                 student_checkbox_id
#             )
#         )
#     )

#     assert student_checkbox.is_selected(), \
#         "Student checkbox was not selected"

#     print(
#         "Student checkbox selected successfully"
#     )

#     # ==========================================================
#     # OPEN PROMOTION MODAL
#     # ==========================================================

#     promote_student = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "openPromotionModalButton"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         promote_student
#     )

#     time.sleep(1)

#     try:
#         promote_student.click()

#     except ElementClickInterceptedException:

#         driver.execute_script(
#             "arguments[0].click();",
#             promote_student
#         )

#     time.sleep(2)

#     # ==========================================================
#     # VERIFY PROMOTION MODAL
#     # ==========================================================

#     promotion_modal = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.XPATH,
#                 "//div[contains(@class,'modal') "
#                 "and contains(@class,'show')]"
#             )
#         )
#     )

#     assert promotion_modal.is_displayed(), \
#         "Student promotion modal was not displayed"
        
#     driver.execute_script(
#             "window.scrollTo(0, document.body.scrollHeight);"
#         )
    
#     time.sleep(1)

#     # ==========================================================
#     # TARGET SECTION
#     # ==========================================================

#     target_section_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//div[@class='nice-select primary_select form-control w-100']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         target_section_dropdown
#     )

#     time.sleep(1)

#     target_section_dropdown.click()

#     time.sleep(1)

#     # ==========================================================
#     # TARGET SECTION OPTION
#     # ==========================================================

#     target_section_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//div[contains(@class,'nice-select') "
#                 f"and contains(@class,'open')]"
#                 f"//li[normalize-space(translate("
#                 f".,"
#                 f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
#                 f"'abcdefghijklmnopqrstuvwxyz'"
#                 f"))='{target_section_value.lower()}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         target_section_option
#     )

#     time.sleep(1)

#     target_section_option.click()

#     time.sleep(1)

#     # ==========================================================
#     # VERIFY TARGET SECTION
#     # ==========================================================

#     actual_target_section = target_section_dropdown.text.strip()

#     assert actual_target_section.lower() == target_section_value.lower(), \
#         (
#             f"Target section was not selected correctly. "
#             f"Expected: '{target_section_value}', "
#             f"Actual: '{actual_target_section}'"
#         )

#     # ==========================================================
#     # PROMOTE SELECTED STUDENT
#     # ==========================================================

#     submit_promotion = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "submitStudentPromotionButton"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         submit_promotion
#     )

#     time.sleep(1)

#     try:
#         submit_promotion.click()

#     except ElementClickInterceptedException:

#         driver.execute_script(
#             "arguments[0].click();",
#             submit_promotion
#         )

#     time.sleep(3)

#     # ==========================================================
#     # VERIFY PROMOTION SUCCESS
#     # ==========================================================

#     success_message = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.XPATH,
#                 "//*[contains(@class,'alert-success') "
#                 "or contains(@class,'swal2-success') "
#                 "or contains(@class,'toast-success')]"
#             )
#         )
#     )

#     assert success_message.is_displayed(), \
#         "Student promotion success message was not displayed"

#     print(
#         "Student selected and promoted successfully"
#     )



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from excel_reader import get_all_data
from excel_report import create_report
import time


def test_student_promotion(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ---------------------------------------------------------
    # Read Student Promotion test data from Excel
    # ---------------------------------------------------------

    data_list = get_all_data("Student promotion")
    results = []

    for data in data_list:

        test_case = str(
            data.get("Test Case") or data.get("Test Case ID") or ""
        ).strip()

        test_data = str(
            data.get("Test Data") or data.get("Test Case Title") or ""
        ).strip()

        validation_value = str(
            data.get("Validation") or data.get("Expected Result") or ""
        ).strip()

        retry_test = str(
            data.get("Retry Test") or ""
        ).strip().upper()

        branch_value = str(data.get("Branch") or "").strip()
        department_value = str(data.get("Department") or "").strip()
        program_value = str(data.get("Program") or "").strip()
        semester_value = str(data.get("Semester") or "").strip()

        target_section_value = str(
            data.get("Section") or data.get("Target Section") or ""
        ).strip()

        student_checkbox_id = str(
            data.get("Student Checkbox ID") or "student_record_3357"
        ).strip()

        case_text = (
            test_case + " " + test_data + " " + validation_value
        ).lower()

        max_attempts = 3 if retry_test == "YES" else 1
        passed = False

        for attempt in range(max_attempts):

            try:

                print(
                    f"\nRunning: {test_case} | {test_data} | "
                    f"Attempt {attempt + 1}/{max_attempts}"
                )

                # -------------------------------------------------
                # Navigate to Student Promotion
                # -------------------------------------------------

                student_info_menu = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div//span[normalize-space()='Student Info']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();", student_info_menu
                )

                time.sleep(1)

                promotion_menu = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//li[contains(.,'Student Promotion')])[2]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();", promotion_menu
                )

                time.sleep(2)

                wait.until(
                    EC.presence_of_element_located(
                        (By.ID, "promotionSearchButton")
                    )
                )

                # -------------------------------------------------
                # PROM-001: Open Student Promotion
                # -------------------------------------------------

                if (
                    "prom-001" in case_text
                    or "open student promotion" in case_text
                ):

                    assert driver.find_element(
                        By.ID, "promotionSearchButton"
                    ).is_displayed(), (
                        "Student Promotion page did not open."
                    )

                else:

                    # -------------------------------------------------
                    # Select Branch
                    # -------------------------------------------------

                    dropdowns = wait.until(
                        lambda d: (
                            d.find_elements(
                                By.CSS_SELECTOR,
                                "div.nice-select.primary_select.form-control"
                            )
                            if len(
                                d.find_elements(
                                    By.CSS_SELECTOR,
                                    "div.nice-select.primary_select.form-control"
                                )
                            ) >= 4
                            else False
                        )
                    )

                    if branch_value:
                        driver.execute_script(
                            "arguments[0].click();", dropdowns[0]
                        )

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
                            "arguments[0].click();", branch_option
                        )

                    # -------------------------------------------------
                    # Select Department
                    # -------------------------------------------------

                    dropdowns = driver.find_elements(
                        By.CSS_SELECTOR,
                        "div.nice-select.primary_select.form-control"
                    )

                    if department_value:
                        driver.execute_script(
                            "arguments[0].click();", dropdowns[1]
                        )

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
                            "arguments[0].click();", department_option
                        )

                    # -------------------------------------------------
                    # Select Program
                    # -------------------------------------------------

                    dropdowns = driver.find_elements(
                        By.CSS_SELECTOR,
                        "div.nice-select.primary_select.form-control"
                    )

                    if program_value:
                        driver.execute_script(
                            "arguments[0].click();", dropdowns[2]
                        )

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
                            "arguments[0].click();", program_option
                        )

                    # -------------------------------------------------
                    # Select Semester
                    # -------------------------------------------------

                    dropdowns = driver.find_elements(
                        By.CSS_SELECTOR,
                        "div.nice-select.primary_select.form-control"
                    )

                    if semester_value:
                        driver.execute_script(
                            "arguments[0].click();", dropdowns[3]
                        )

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
                            "arguments[0].click();", semester_option
                        )

                    # -------------------------------------------------
                    # PROM-002: Select Valid Academic Filters
                    # -------------------------------------------------

                    if (
                        "prom-002" in case_text
                        or "valid academic filters" in case_text
                        or "select valid academic" in case_text
                    ):

                        dropdowns = driver.find_elements(
                            By.CSS_SELECTOR,
                            "div.nice-select.primary_select.form-control"
                        )

                        assert len(dropdowns) >= 4, (
                            "Academic filter dropdowns were not found."
                        )

                    # -------------------------------------------------
                    # PROM-003: Verify Dependent Dropdowns
                    # -------------------------------------------------

                    elif (
                        "prom-003" in case_text
                        or "dependent academic" in case_text
                    ):

                        dropdowns = driver.find_elements(
                            By.CSS_SELECTOR,
                            "div.nice-select.primary_select.form-control"
                        )

                        assert len(dropdowns) >= 4, (
                            "Expected academic dropdowns were not displayed."
                        )

                        print("Academic dropdown controls are available.")

                    # -------------------------------------------------
                    # PROM-005 to PROM-008: Missing Required Filters
                    # -------------------------------------------------

                    elif any(
                        case_id in case_text
                        for case_id in [
                            "prom-005", "prom-006",
                            "prom-007", "prom-008"
                        ]
                    ):

                        # Leave the corresponding Excel field blank.
                        # This test assumes the page does not automatically
                        # populate a default value for that field.

                        search_button = wait.until(
                            EC.element_to_be_clickable(
                                (By.ID, "promotionSearchButton")
                            )
                        )

                        driver.execute_script(
                            "arguments[0].click();", search_button
                        )

                        time.sleep(2)

                        error_elements = driver.find_elements(
                            By.XPATH,
                            "//*[contains(@class,'invalid-feedback') "
                            "or contains(@class,'text-danger') "
                            "or contains(@class,'alert-danger') "
                            "or @role='alert']"
                        )

                        visible_errors = []

                        for error in error_elements:
                            if error.is_displayed() and error.text.strip():
                                visible_errors.append(error.text.strip())

                        assert visible_errors, (
                            "No validation message was displayed for "
                            "the missing academic filter."
                        )

                    # -------------------------------------------------
                    # Search Students
                    # -------------------------------------------------

                    if (
                        "prom-004" in case_text
                        or "search students with valid" in case_text
                        or "prom-009" in case_text
                        or "no matching students" in case_text
                        or "prom-010" in case_text
                        or "select a student checkbox" in case_text
                        or "prom-011" in case_text
                        or "verify selected checkbox" in case_text
                        or "prom-012" in case_text
                        or "deselect a selected student" in case_text
                        or "prom-013" in case_text
                        or "open promotion modal after" in case_text
                        or "prom-014" in case_text
                        or "without selecting a student" in case_text
                        or "prom-015" in case_text
                        or "select valid target section" in case_text
                        or "prom-016" in case_text
                        or "submit promotion with valid" in case_text
                        or "prom-017" in case_text
                        or "without selecting target section" in case_text
                        or "prom-018" in case_text
                        or "verify promotion success" in case_text
                        or "prom-019" in case_text
                        or "selected target section is used" in case_text
                        or "prom-020" in case_text
                        or "results after promotion" in case_text
                        or "prom-021" in case_text
                        or "modal before submission" in case_text
                    ):

                        search_button = wait.until(
                            EC.element_to_be_clickable(
                                (By.ID, "promotionSearchButton")
                            )
                        )

                        driver.execute_script(
                            "arguments[0].click();", search_button
                        )

                        time.sleep(2)

                    # -------------------------------------------------
                    # PROM-004: Search with Valid Filters
                    # -------------------------------------------------

                    if (
                        "prom-004" in case_text
                        or "search students with valid" in case_text
                    ):

                        rows = driver.find_elements(
                            By.XPATH, "//table//tbody/tr"
                        )

                        empty_messages = driver.find_elements(
                            By.XPATH,
                            "//*[contains(translate(normalize-space(.),"
                            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                            "'abcdefghijklmnopqrstuvwxyz'),'no records') "
                            "or contains(translate(normalize-space(.),"
                            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                            "'abcdefghijklmnopqrstuvwxyz'),'no data')]"
                        )

                        visible_empty_messages = [
                            element for element in empty_messages
                            if element.is_displayed() and element.text.strip()
                        ]

                        assert rows or visible_empty_messages, (
                            "Neither student rows nor an empty-result "
                            "message was displayed."
                        )

                    # -------------------------------------------------
                    # PROM-009: No Matching Students
                    # -------------------------------------------------

                    elif (
                        "prom-009" in case_text
                        or "no matching students" in case_text
                    ):

                        checkbox_elements = driver.find_elements(
                            By.ID, student_checkbox_id
                        )

                        assert not checkbox_elements, (
                            "A matching student checkbox was displayed."
                        )

                        empty_messages = driver.find_elements(
                            By.XPATH,
                            "//*[contains(translate(normalize-space(.),"
                            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                            "'abcdefghijklmnopqrstuvwxyz'),'no records') "
                            "or contains(translate(normalize-space(.),"
                            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                            "'abcdefghijklmnopqrstuvwxyz'),'no data')]"
                        )

                        assert any(
                            element.is_displayed() and element.text.strip()
                            for element in empty_messages
                        ), "No explicit empty-result message was found."

                    # -------------------------------------------------
                    # PROM-010 to PROM-012: Student Checkbox
                    # -------------------------------------------------

                    elif any(
                        case_id in case_text
                        for case_id in [
                            "prom-010", "prom-011", "prom-012"
                        ]
                    ):

                        checkbox = wait.until(
                            EC.presence_of_element_located(
                                (By.ID, student_checkbox_id)
                            )
                        )

                        if "prom-012" in case_text or (
                            "deselect a selected student" in case_text
                        ):

                            if not checkbox.is_selected():
                                driver.execute_script(
                                    "arguments[0].click();", checkbox
                                )

                            checkbox = wait.until(
                                EC.presence_of_element_located(
                                    (By.ID, student_checkbox_id)
                                )
                            )

                            assert checkbox.is_selected(), (
                                "Student checkbox could not be selected."
                            )

                            driver.execute_script(
                                "arguments[0].click();", checkbox
                            )

                            checkbox = wait.until(
                                EC.presence_of_element_located(
                                    (By.ID, student_checkbox_id)
                                )
                            )

                            assert not checkbox.is_selected(), (
                                "Student checkbox was not deselected."
                            )

                        else:

                            if not checkbox.is_selected():
                                driver.execute_script(
                                    "arguments[0].click();", checkbox
                                )

                            checkbox = wait.until(
                                EC.presence_of_element_located(
                                    (By.ID, student_checkbox_id)
                                )
                            )

                            assert checkbox.is_selected(), (
                                "Student checkbox was not selected."
                            )

                    # -------------------------------------------------
                    # PROM-013 to PROM-021: Open Promotion Modal
                    # -------------------------------------------------

                    elif any(
                        case_id in case_text
                        for case_id in [
                            "prom-013", "prom-014", "prom-015",
                            "prom-016", "prom-017", "prom-018",
                            "prom-019", "prom-021"
                        ]
                    ):

                        if not (
                            "prom-014" in case_text
                            or "without selecting a student" in case_text
                        ):

                            checkbox = wait.until(
                                EC.presence_of_element_located(
                                    (By.ID, student_checkbox_id)
                                )
                            )

                            if not checkbox.is_selected():
                                driver.execute_script(
                                    "arguments[0].click();", checkbox
                                )

                        else:

                            checkbox = wait.until(
                                EC.presence_of_element_located(
                                    (By.ID, student_checkbox_id)
                                )
                            )

                            if checkbox.is_selected():
                                driver.execute_script(
                                    "arguments[0].click();", checkbox
                                )

                        promotion_button = wait.until(
                            EC.element_to_be_clickable(
                                (By.ID, "openPromotionModalButton")
                            )
                        )

                        driver.execute_script(
                            "arguments[0].click();", promotion_button
                        )

                        try:
                            modal = WebDriverWait(driver, 5).until(
                                EC.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        "//div[contains(@class,'modal') "
                                        "and contains(@class,'show')]"
                                    )
                                )
                            )
                        except TimeoutException:
                            modal = None

                        # PROM-013: Modal opens after selecting student
                        if (
                            "prom-013" in case_text
                            or "open promotion modal after" in case_text
                        ):

                            assert modal is not None, (
                                "Promotion modal did not open."
                            )

                        # PROM-014: Promotion without student
                        elif (
                            "prom-014" in case_text
                            or "without selecting a student" in case_text
                        ):

                            if modal is not None:
                                error_elements = driver.find_elements(
                                    By.XPATH,
                                    "//*[contains(@class,'invalid-feedback') "
                                    "or contains(@class,'text-danger') "
                                    "or contains(@class,'alert-danger') "
                                    "or @role='alert']"
                                )

                                visible_errors = [
                                    element.text.strip()
                                    for element in error_elements
                                    if element.is_displayed()
                                    and element.text.strip()
                                ]

                                assert visible_errors or not modal.is_displayed(), (
                                    "Promotion was not blocked when no "
                                    "student was selected."
                                )

                        else:

                            assert modal is not None, (
                                "Promotion modal did not open."
                            )

                            # -----------------------------------------
                            # PROM-021: Verify modal before submission
                            # -----------------------------------------

                            if (
                                "prom-021" in case_text
                                or "modal before submission" in case_text
                            ):

                                section_dropdown = modal.find_element(
                                    By.XPATH,
                                    ".//div[contains(@class,'nice-select') "
                                    "and contains(@class,'primary_select')]"
                                )

                                assert section_dropdown.is_displayed(), (
                                    "Target Section dropdown was not displayed."
                                )

                            else:

                                # -----------------------------------------
                                # Select Target Section
                                # -----------------------------------------

                                section_dropdown = modal.find_element(
                                    By.XPATH,
                                    ".//div[contains(@class,'nice-select') "
                                    "and contains(@class,'primary_select')]"
                                )

                                if (
                                    "prom-017" not in case_text
                                    and "without selecting target section"
                                    not in case_text
                                ):

                                    driver.execute_script(
                                        "arguments[0].click();",
                                        section_dropdown
                                    )

                                    section_option = wait.until(
                                        EC.element_to_be_clickable(
                                            (
                                                By.XPATH,
                                                "//div[contains(@class,'nice-select') "
                                                "and contains(@class,'open')]"
                                                f"//li[normalize-space()="
                                                f"'{target_section_value}']"
                                            )
                                        )
                                    )

                                    driver.execute_script(
                                        "arguments[0].click();",
                                        section_option
                                    )

                                    section_dropdown = modal.find_element(
                                        By.XPATH,
                                        ".//div[contains(@class,'nice-select') "
                                        "and contains(@class,'primary_select')]"
                                    )

                                    assert (
                                        section_dropdown.text.strip().lower()
                                        == target_section_value.lower()
                                    ), "Target Section selection did not match."

                                # -----------------------------------------
                                # PROM-015: Select valid target section
                                # -----------------------------------------

                                if (
                                    "prom-015" in case_text
                                    or "select valid target section"
                                    in case_text
                                ):
                                    assert target_section_value, (
                                        "Target Section is missing in Excel."
                                    )

                                # -----------------------------------------
                                # Submit promotion for PROM-016 to PROM-019
                                # -----------------------------------------

                                elif any(
                                    case_id in case_text
                                    for case_id in [
                                        "prom-016", "prom-017",
                                        "prom-018", "prom-019"
                                    ]
                                ):

                                    submit_button = wait.until(
                                        EC.element_to_be_clickable(
                                            (
                                                By.ID,
                                                "submitStudentPromotionButton"
                                            )
                                        )
                                    )

                                    driver.execute_script(
                                        "arguments[0].click();",
                                        submit_button
                                    )

                                    time.sleep(2)

                                    success_elements = driver.find_elements(
                                        By.XPATH,
                                        "//*[contains(@class,'alert-success') "
                                        "or contains(@class,'swal2-success') "
                                        "or contains(@class,'toast-success')]"
                                    )

                                    visible_success = [
                                        element for element in success_elements
                                        if element.is_displayed()
                                        and element.text.strip()
                                    ]

                                    # PROM-017 expects submission to be blocked
                                    if (
                                        "prom-017" in case_text
                                        or "without selecting target section"
                                        in case_text
                                    ):

                                        modal_elements = driver.find_elements(
                                            By.XPATH,
                                            "//div[contains(@class,'modal') "
                                            "and contains(@class,'show')]"
                                        )

                                        modal_still_open = any(
                                            element.is_displayed()
                                            for element in modal_elements
                                        )

                                        error_elements = driver.find_elements(
                                            By.XPATH,
                                            "//*[contains(@class,'invalid-feedback') "
                                            "or contains(@class,'text-danger') "
                                            "or contains(@class,'alert-danger') "
                                            "or @role='alert']"
                                        )

                                        visible_errors = [
                                            element.text.strip()
                                            for element in error_elements
                                            if element.is_displayed()
                                            and element.text.strip()
                                        ]

                                        assert (
                                            visible_errors or modal_still_open
                                        ), (
                                            "Submission was not blocked when "
                                            "Target Section was blank."
                                        )

                                    else:

                                        assert visible_success, (
                                            "Promotion success message "
                                            "was not displayed."
                                        )

                                        # PROM-019 needs an additional check
                                        # of the student's actual assigned
                                        # section after promotion.
                                        if "prom-019" in case_text:
                                            raise AssertionError(
                                                "Add the actual student-section "
                                                "verification locator to complete "
                                                "PROM-019."
                                            )

                    # -------------------------------------------------
                    # PROM-020: Verify Results After Promotion
                    # -------------------------------------------------

                    elif (
                        "prom-020" in case_text
                        or "results after promotion" in case_text
                    ):

                        driver.refresh()

                        wait.until(
                            EC.presence_of_element_located(
                                (By.ID, "promotionSearchButton")
                            )
                        )

                        # Reopen Student Promotion after refresh
                        student_info_menu = wait.until(
                            EC.element_to_be_clickable(
                                (
                                    By.XPATH,
                                    "//div//span[normalize-space()='Student Info']"
                                )
                            )
                        )

                        driver.execute_script(
                            "arguments[0].click();", student_info_menu
                        )

                        time.sleep(1)

                        promotion_menu = wait.until(
                            EC.element_to_be_clickable(
                                (
                                    By.XPATH,
                                    "(//li[contains(.,'Student Promotion')])[2]"
                                )
                            )
                        )

                        driver.execute_script(
                            "arguments[0].click();", promotion_menu
                        )

                        time.sleep(2)

                        dropdowns = driver.find_elements(
                            By.CSS_SELECTOR,
                            "div.nice-select.primary_select.form-control"
                        )

                        if branch_value:
                            driver.execute_script(
                                "arguments[0].click();", dropdowns[0]
                            )

                            option = wait.until(
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
                                "arguments[0].click();", option
                            )

                        dropdowns = driver.find_elements(
                            By.CSS_SELECTOR,
                            "div.nice-select.primary_select.form-control"
                        )

                        if department_value:
                            driver.execute_script(
                                "arguments[0].click();", dropdowns[1]
                            )

                            option = wait.until(
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
                                "arguments[0].click();", option
                            )

                        dropdowns = driver.find_elements(
                            By.CSS_SELECTOR,
                            "div.nice-select.primary_select.form-control"
                        )

                        if program_value:
                            driver.execute_script(
                                "arguments[0].click();", dropdowns[2]
                            )

                            option = wait.until(
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
                                "arguments[0].click();", option
                            )

                        dropdowns = driver.find_elements(
                            By.CSS_SELECTOR,
                            "div.nice-select.primary_select.form-control"
                        )

                        if semester_value:
                            driver.execute_script(
                                "arguments[0].click();", dropdowns[3]
                            )

                            option = wait.until(
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
                                "arguments[0].click();", option
                            )

                        search_button = wait.until(
                            EC.element_to_be_clickable(
                                (By.ID, "promotionSearchButton")
                            )
                        )

                        driver.execute_script(
                            "arguments[0].click();", search_button
                        )

                        time.sleep(2)

                        rows = driver.find_elements(
                            By.XPATH, "//table//tbody/tr"
                        )

                        empty_messages = driver.find_elements(
                            By.XPATH,
                            "//*[contains(translate(normalize-space(.),"
                            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                            "'abcdefghijklmnopqrstuvwxyz'),'no records') "
                            "or contains(translate(normalize-space(.),"
                            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                            "'abcdefghijklmnopqrstuvwxyz'),'no data')]"
                        )

                        assert rows or any(
                            element.is_displayed()
                            and element.text.strip()
                            for element in empty_messages
                        ), (
                            "Search results or an empty state were not "
                            "displayed after refresh."
                        )

                    # -------------------------------------------------
                    # Unknown test case
                    # -------------------------------------------------

                    elif not any(
                        case_id in case_text
                        for case_id in [
                            "prom-002", "valid academic filters",
                            "select valid academic", "prom-003",
                            "dependent academic", "prom-005",
                            "prom-006", "prom-007", "prom-008",
                            "prom-009", "no matching students",
                            "prom-010", "select a student checkbox",
                            "prom-011", "verify selected checkbox",
                            "prom-012", "deselect a selected student",
                            "prom-013", "open promotion modal after",
                            "prom-014", "without selecting a student",
                            "prom-015", "select valid target section",
                            "prom-016", "submit promotion with valid",
                            "prom-017", "without selecting target section",
                            "prom-018", "verify promotion success",
                            "prom-019", "selected target section is used",
                            "prom-020", "results after promotion",
                            "prom-021", "modal before submission"
                        ]
                    ):

                        raise AssertionError(
                            "Test case was not recognized. Check the Excel "
                            f"Test Case ID or title: {test_case} | {test_data}"
                        )

                # -------------------------------------------------
                # Test Passed
                # -------------------------------------------------

                print(f"PASS - {test_case} | {test_data}")

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

            # -----------------------------------------------------
            # Retry / Failure
            # -----------------------------------------------------

            except Exception as e:

                print(
                    f"Attempt {attempt + 1} failed: {str(e)}"
                )

                if attempt < max_attempts - 1:

                    print(f"Retrying {test_case}...")
                    time.sleep(2)

                    try:
                        driver.refresh()
                        time.sleep(2)
                    except Exception:
                        pass

                    continue

                results.append({
                    "Test Case": test_case,
                    "Test Data": test_data,
                    "Validation": validation_value,
                    "Retry Test": retry_test,
                    "Attempt": attempt + 1,
                    "Status": "FAIL",
                    "Error": str(e)
                })

                print(f"FAIL - {test_case}: {str(e)}")

        # ---------------------------------------------------------
        # Row completed
        # ---------------------------------------------------------

        if passed:
            print(f"Completed: {test_case}")

    # -------------------------------------------------------------
    # Create Excel Report
    # -------------------------------------------------------------

    create_report(results)

    print("\n====================================")
    print("Student Promotion Test Execution Completed")
    print("Excel Report Generated Successfully")
    print("====================================")
