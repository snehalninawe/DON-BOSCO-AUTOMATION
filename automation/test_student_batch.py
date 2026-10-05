# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# import time




# # ==========================================================
# # TEST DATA
# # ==========================================================

# branch_value = "STU Marol(east) Mumbai 400002"
# department_value = "IT-26"
# program_value = "New-IT"
# semester_value = "Sem-3-IT"
# subject_type_value = "Practical"
# subject = 'SUB'


# def test_batch_assignment(driver):

#     wait = WebDriverWait(driver, 15)

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

#     # ==========================================================
#     # OPEN Batch ASSIGNMENT
#     # ==========================================================

#     batch_assignment = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//li[contains(.,'Student Batch')])[2]"
#             )
#         )
#     )

#     batch_assignment.click()

#     # ==========================================================
#     # ADD BUTTON
#     # ==========================================================

#     add_button = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "attnAjaxAddRowsBtn"
#             )
#         )
#     )

#     add_button.click()

#     # ==========================================================
#     # BRANCH DROPDOWN
#     # ==========================================================

#     branch = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[@class='nice-select primary_select form-control'])[1]"
#             )
#         )
#     )

#     branch.click()

#     branch_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[normalize-space()='{branch_value}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         branch_option
#     )
#     driver.execute_script(
#             "arguments[0].click();",
#             branch_option
#         )

#     # branch_option.click()

#     # ==========================================================
#     # DEPARTMENT DROPDOWN
#     # ==========================================================

#     department = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[@class='nice-select primary_select form-control'])[2]"
#             )
#         )
#     )

#     department.click()

#     department_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[normalize-space()='{department_value}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         department_option
#     )

#     department_option.click()

#     # ==========================================================
#     # PROGRAM DROPDOWN
#     # ==========================================================

#     program = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[@class='nice-select primary_select form-control'])[3]"
#             )
#         )
#     )

#     program.click()

#     program_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[normalize-space()='{program_value}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         program_option
#     )

#     program_option.click()

#     # ==========================================================
#     # SEMESTER DROPDOWN
#     # ==========================================================

#     semester = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[@class='nice-select primary_select form-control'])[4]"
#             )
#         )
#     )

#     semester.click()

#     semester_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[normalize-space()='{semester_value}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         semester_option
#     )

#     semester_option.click()

#     # ==========================================================
#     # SUBJECT TYPE DROPDOWN
#     # ==========================================================

#     subject_type = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[@class='nice-select primary_select form-control'])[5]"
#             )
#         )
#     )

#     subject_type.click()

#     subject_type_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[normalize-space()='{subject_type_value}']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         subject_type_option
#     )

#     subject_type_option.click()
    
#     # ==========================================================
#         # SUBJECT DROPDOWN
#         # ==========================================================
    
#     subject = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     "(//div[@class='nice-select primary_select form-control'])[5]"
#                 )
#             )
#         )
    
#     subject.click()
    
#     subject_option = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     f"//li[normalize-space()='{subject}']"
#                 )
#             )
#         )
    
#     driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});",
#             subject_option
#         )
    
#     subject_option.click()

#     # ==========================================================
# # FETCH
# # ==========================================================

#     fetch = wait.until(
#     EC.element_to_be_clickable(
#         (
#             By.ID,
#             "fetchBatchBtn"
#         )
#     )
# )

#     fetch.click()

# # ==========================================================
# # WAIT FOR FETCH RESULTS
# # ==========================================================

#     driver.execute_script(
#     "window.scrollTo(0, document.body.scrollHeight);"
# )

# # ==========================================================
# # BATCH FIELDS
# # ==========================================================

#     time.sleep(2)  # Wait for the page to load completely

#     batch_fields = wait.until(
#     EC.element_to_be_clickable(
#         (
#             By.ID,
#             "batch_title"
#         )
#     )
# )
#     batch_fields.send_keys("BATCH-1")

#     # ==========================================================
#     # ASSIGNMENT TYPE
#     # ==========================================================

#     assignment_type = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[@class='nice-select primary_select form-control'])[6]"
#             )
#         )
#     )

#     assignment_type.click()

#     assignment_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//li[.='Student wise']"
#             )
#         )
#     )
    
#     driver.execute_script(
#         "arguments[0].click();",
#         assignment_option
#     )

#    #student name dropdown
#     student_name_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//div[@class='ms-options-wrap ms-active']"
#             )
#         )
#     )
    
#     driver.execute_script(
#         "arguments[0].click();",
#         student_name_dropdown
#     )
    
#     student_name_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//li[contains(normalize-space(), 'Ananya Patel')]"
#             )
#         )
#     )
    
#     driver.execute_script(
#         "arguments[0].click();",
#         student_name_option
#     )

#     # ==========================================================
#     # SAVE
#     # ==========================================================

#     save_button = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "saveBtn"
#             )
#         )
#     )

#     save_button.click()
    
#     #modal-confirmation popup
#     modal_confirmation = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//div[@aria-describedby='swal2-html-container']"
#             )
#         )
#     )
    
#     #confirm button
#     # confirm_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//button[@class='swal2-confirm swal2-styled']"
#     #         )
#     #     )
#     # )
#     # confirm_button.click()
    
#     #not-confirm button
#     not_confirm_button = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//button[@class='swal2-cancel swal2-styled']"
#             )
#         )
#     )
#     not_confirm_button.click()

#     time.sleep(2)  


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


# ==========================================================
# TEST DATA
# ==========================================================

branch_value = "STU Marol(east) Mumbai 400002"
department_value = "IT-26"
program_value = "New-IT"
semester_value = "Sem-3-IT"
subject_type_value = "Practical"
subject_value = "SUB"

batch_name = "BATCH-1"
assignment_type_value = "Student wise"
student_name_value = "Ananya Patel"


def test_batch_assignment(driver):

    wait = WebDriverWait(driver, 15)

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

    # ==========================================================
    # OPEN STUDENT BATCH
    # ==========================================================

    batch_assignment = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Student Batch')])[2]"
            )
        )
    )

    batch_assignment.click()

    # ==========================================================
    # ADD BUTTON
    # ==========================================================

    add_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "attnAjaxAddRowsBtn"
            )
        )
    )

    add_button.click()

    # ==========================================================
    # BRANCH
    # ==========================================================

    branch_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[1]"
            )
        )
    )

    branch_dropdown.click()

    branch_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{branch_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        branch_option
    )

    driver.execute_script(
        "arguments[0].click();",
        branch_option
    )

    # ==========================================================
    # DEPARTMENT
    # ==========================================================

    department_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[2]"
            )
        )
    )

    department_dropdown.click()

    department_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{department_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        department_option
    )

    department_option.click()

    # ==========================================================
    # PROGRAM
    # ==========================================================

    program_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[3]"
            )
        )
    )

    program_dropdown.click()

    program_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{program_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        program_option
    )

    program_option.click()

    # ==========================================================
    # SEMESTER
    # ==========================================================

    semester_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[4]"
            )
        )
    )

    semester_dropdown.click()

    semester_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{semester_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester_option
    )

    semester_option.click()

    # ==========================================================
    # SUBJECT TYPE
    # ==========================================================

    subject_type_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[5]"
            )
        )
    )

    subject_type_dropdown.click()

    subject_type_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{subject_type_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        subject_type_option
    )

    subject_type_option.click()
    # ==========================================================
    # SUBJECT MULTI-SELECT
    # ==========================================================

    subject_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'ms-options-wrap')])[1]"
            )
        )
    )

    subject_dropdown.click()

    subject_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[contains(normalize-space(),'{subject_value}')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        subject_option
    )

    subject_option.click()

    # ==========================================================
    # FETCH
    # ==========================================================

    fetch_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "fetchBatchBtn"
            )
        )
    )

    fetch_button.click()

    # ==========================================================
    # WAIT FOR BATCH FIELD
    # ==========================================================

    batch_field = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "batch_title"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        batch_field
    )

    batch_field.clear()
    batch_field.send_keys(batch_name)

    # Verify batch name
    assert batch_field.get_attribute("value") == batch_name

    # ==========================================================
    # ASSIGNMENT TYPE
    # ==========================================================

    assignment_type_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[6]"
            )
        )
    )

    assignment_type_dropdown.click()

    assignment_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{assignment_type_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        assignment_option
    )

    assignment_option.click()

        # ==========================================================
    # STUDENT NAME MULTI-SELECT
    # ==========================================================

    student_name_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'ms-options-wrap')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        student_name_dropdown
    )

    student_name_dropdown.click()

    # ==========================================================
    # SELECT STUDENT
    # ==========================================================

    student_name_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[contains(normalize-space(),'{student_name_value}')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        student_name_option
    )

    student_name_option.click()

    # ==========================================================
    # VERIFY STUDENT SELECTED
    # ==========================================================

    selected_student = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[contains(normalize-space(),'{student_name_value}')]"
            )
        )
    )

    assert student_name_value.lower() in selected_student.text.lower()
    # ==========================================================
    # SAVE
    # ==========================================================

    save_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "submitButton"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        save_button
    )

    save_button.click()

    # ==========================================================
    # CONFIRMATION POPUP
    # ==========================================================

    # modal_confirmation = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//div[@aria-describedby='swal2-html-container']"
    #         )
    #     )
    # )

    # # Verify popup is displayed
    # assert modal_confirmation.is_displayed()

    # # ==========================================================
    # # CANCEL CONFIRMATION
    # # ==========================================================

    # not_confirm_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//button[contains(@class,'swal2-cancel')]"
    #         )
    #     )
    # )

    # not_confirm_button.click()

    # # ==========================================================
    # # VERIFY POPUP CLOSED
    # # ==========================================================

    # wait.until(
    #     EC.invisibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//div[@aria-describedby='swal2-html-container']"
    #         )
    #     )
    # )