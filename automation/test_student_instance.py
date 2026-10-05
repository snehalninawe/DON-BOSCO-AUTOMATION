# from concurrent.futures import wait
# from time import time

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


# def test_student_instance(driver):

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
#     # OPEN STUDENT INSTANCE
#     # ==========================================================

#     student_instance = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//li[contains(.,'Student Instance')])[2]"
#             )
#         )
#     )

#     student_instance.click()

#     # ==========================================================
#     # ADD BUTTON
#     # ==========================================================

#     add_btn = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "attnAjaxAddRowsBtn"
#             )
#         )
#     )
    
#     add_btn.click()

#     # ==========================================================
#     # BRANCH DROPDOWN 
#     # ==========================================================

#     branch = driver.find_element(
#             By.XPATH,
#             "(//div[@class='nice-select primary_select form-control'])[1]"
#         )
#     branch.click()
#     time.sleep(2)
    
#     branch_options = wait.until(
#             EC.presence_of_element_located(
#                 (
#                     By.XPATH,
#                     "//li[normalize-space()='STU Marol(east) Mumbai 400002']"
#                 )
#             )
#         )
    
#     driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});",
#             branch_options
#         )
    
#     driver.execute_script(
#             "arguments[0].click();",
#             branch_options
#         )
    
#     time.sleep(2)
    
#     # ==========================================================
#         # DEPARTMENT DROPDOWN 
#         # ==========================================================
    
#     department = driver.find_element(
#                 By.XPATH,
#                 "(//div[@class='nice-select primary_select form-control'])[2]"
#             )
#     department.click()
#     time.sleep(2)
        
#     department_options = wait.until(
#                 EC.presence_of_element_located(
#                     (
#                         By.XPATH,
#                         "//li[normalize-space()='CSE-2026']"
#                     )
#                 )
#             )
        
#     driver.execute_script(
#                 "arguments[0].scrollIntoView({block:'center'});",
#                 department_options
#             )
        
#     driver.execute_script(
#                 "arguments[0].click();",
#                 department_options
#             )
        
#     time.sleep(2)
    
#      # ==========================================================
#             # PROGRAM DROPDOWN 
#             # ==========================================================
        
#     program = driver.find_element(
#                     By.XPATH,
#                     "(//div[@class='nice-select primary_select form-control'])[3]"
#                 )
#     program.click()
#     time.sleep(2)
            
#     program_options = wait.until(
#                     EC.presence_of_element_located(
#                         (
#                             By.XPATH,
#                             "//li[normalize-space()='new-btech']"
#                         )
#                     )
#                 )
            
#     driver.execute_script(
#                     "arguments[0].scrollIntoView({block:'center'});",
#                     program_options
#                 )
            
#     driver.execute_script(
#                     "arguments[0].click();",
#                     program_options
#                 )
            
#     time.sleep(2)
    
#     # ==========================================================
#                 # SEMESTER DROPDOWN 
#                 # ==========================================================
            
#     semester = driver.find_element(
#                         By.XPATH,
#                         "(//div[@class='nice-select primary_select form-control'])[4]"
#                     )
#     semester.click()
#     time.sleep(2)
                
#     semester_options = wait.until(
#                         EC.presence_of_element_located(
#                             (
#                                 By.XPATH,
#                                 "//li[normalize-space()='Sem-3(CSE)']"
#                             )
#                         )
#                     )
                
#     driver.execute_script(
#                         "arguments[0].scrollIntoView({block:'center'});",
#                         semester_options
#                     )
                
#     driver.execute_script(
#                         "arguments[0].click();",
#                         semester_options
#                     )
                
#     time.sleep(2)
    
#     # ==========================================================
#                     # SEMESTER LABEL DROPDOWN 
#                     # ==========================================================
                
#     semester_label = driver.find_element(
#                             By.XPATH,
#                             "(//div[@class='nice-select primary_select form-control'])[5]"
#                         )
#     semester_label.click()
#     time.sleep(2)
                    
#     semester_label_options = wait.until(
#                             EC.presence_of_element_located(
#                                 (
#                                     By.XPATH,
#                                     "//li[normalize-space()='Sem-3-cse-label']"
#                                 )
#                             )
#                         )
                    
#     driver.execute_script(
#                             "arguments[0].scrollIntoView({block:'center'});",
#                             semester_label_options
#                         )
                    
#     driver.execute_script(
#                             "arguments[0].click();",
#                             semester_label_options
#                         )
                    
#     time.sleep(2)
    
#     # ==========================================================
#                         # Academic department DROPDOWN 
#                         # ==========================================================
                    
#     academic_department = driver.find_element(
#                                 By.XPATH,
#                                 "(//div[@class='nice-select primary_select form-control'])[6]"
#                             )
#     academic_department.click()
#     time.sleep(2)
                        
#     academic_department_options = wait.until(
#                                 EC.presence_of_element_located(
#                                     (
#                                         By.XPATH,
#                                         "//li[normalize-space()='Basic Sciences and Humanities']"
#                                     )
#                                 )
#                             )
                        
#     driver.execute_script(
#                                 "arguments[0].scrollIntoView({block:'center'});",
#                                 academic_department_options
#                             )
                        
#     driver.execute_script(
#                                 "arguments[0].click();",
#                                 academic_department_options
#                             )
                        
#     time.sleep(2)
    
#     # ==========================================================
#         # ADMISSION DATE
#         # ==========================================================
    
#     admission_date = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     "(//input[@placeholder='Select Date'])[1]"
#                 )
#             )
#         )
    
#     admission_date.click()
    
#     time.sleep(1)
    
#     admission_day = admission_date_value.split("/")[0]
    
#     date = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     f"//td[contains(@class,'day') "
#                     f"and normalize-space()='{admission_day}' "
#                     f"and not(contains(@class,'old')) "
#                     f"and not(contains(@class,'new'))]"
#                 )
#             )
#         )
    
#     date.click()
    
#     time.sleep(1)
    
#     #GENERATE BUTTON
#     generate_button = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "generateAdmissionNumberBtn"
#             )
#         )
#     )
    
#     generate_button.click()
    
#     #First Name
#     first_name = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.NAME,
#                 "first_name"
#             )
#         )
#     )
#     first_name.send_keys("TestFirstName")
    
#     #Last Name
#     last_name = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.NAME,
#                 "last_name"
#             )
#         )
#     )
#     last_name.send_keys("TestLastName")
    
#     #email
#     email = wait.until( 
                       
#         EC.element_to_be_clickable(
#             (
#                 By.NAME,
#                 "email_address"
#             )
#         )
#     )
#     email.send_keys("testemail@example.com")
    
#     # ==========================================================
#                             # STUDENT CATEGORY DROPDOWN 
#                             # ==========================================================
                        
#     student_category = driver.find_element(
#                                     By.XPATH,
#                                     "//div[@class='nice-select primary_select form-control feedback_input_types open']"
#                                 )
#     student_category.click()
#     time.sleep(2)
                            
#     student_category_options = wait.until(
#                                     EC.presence_of_element_located(
#                                         (
#                                             By.XPATH,
#                                             "//li[normalize-space()='General']"
#                                         )
#                                     )
#                                 )
                            
#     driver.execute_script(
#                                     "arguments[0].scrollIntoView({block:'center'});",
#                                     student_category_options
#                                 )
                            
#     driver.execute_script(
#                                     "arguments[0].click();",
#                                     student_category_options
#                                 )
                            
#     time.sleep(2)
    
#     #Phone Number
#     phone_number = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.NAME,
#                 "phone_number"
#             )
#         )
#     )
#     phone_number.send_keys("1234567890")
    
#     #save button
#     save_button = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "submitButton"
#             )
#         )
#     )
#     save_button.click()

    

#     # ==========================================================
#     # DELETE BUTTON
#     # ==========================================================

#     # delete_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//a[contains(@class,'delete-button-datatable')])[1]"
#     #         )
#     #     )
#     # )

#     # delete_button.click()

#     # ==========================================================
#     # DELETE CONFIRMATION POPUP
#     # ==========================================================

#     # confirmation_popup = wait.until(
#     #     EC.visibility_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "//div[@aria-describedby='swal2-html-container']"
#     #         )
#     #     )
#     # )

#     # # ==========================================================
#     # # CANCEL DELETE
#     # # ==========================================================

#     # cancel_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//button[contains(@class,'swal2-cancel')]"
#     #         )
#     #     )
#     # )

#     # cancel_button.click()

#     # ==========================================================
#     # CONFIRM DELETE
#     # ==========================================================

#     # confirm_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//button[contains(@class,'swal2-confirm')]"
#     #         )
#     #     )
#     # )
#     #
#     # confirm_button.click()



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# ==========================================================
# TEST DATA
# ==========================================================

branch_value = "RTM,Marol(West),Mumbai-400021"
department_value = "CSE-2026"
program_value = "new-btech"
semester_value = "Sem-3(CSE)"
semester_label_value = "Sem-3-cse-label"
academic_department_value = "Basic Sciences and Humanities"

# admission_date_value = "20/08/2026"

first_name_value = "TestFirstName"
last_name_value = "TestLastName"
email_value = "testemail@example.com"
student_category_value = "General"
phone_number_value = "1234567890"


def test_student_instance(driver):

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
    # OPEN STUDENT INSTANCE
    # ==========================================================

    student_instance = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Student Instance')])[2]"
            )
        )
    )

    student_instance.click()

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
    # BRANCH DROPDOWN
    # ==========================================================

    branch = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[1]"
            )
        )
    )

    branch.click()

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

    # branch_option.click()

    # ==========================================================
    # DEPARTMENT DROPDOWN
    # ==========================================================

    department = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[2]"
            )
        )
    )

    department.click()

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
    # PROGRAM DROPDOWN
    # ==========================================================

    program = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[3]"
            )
        )
    )

    program.click()

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
    # SEMESTER DROPDOWN
    # ==========================================================

    semester = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[4]"
            )
        )
    )

    semester.click()

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
    # SEMESTER LABEL DROPDOWN
    # ==========================================================

    semester_label = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[5]"
            )
        )
    )

    semester_label.click()

    semester_label_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{semester_label_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester_label_option
    )

    semester_label_option.click()

    # ==========================================================
    # ACADEMIC DEPARTMENT DROPDOWN
    # ==========================================================

    academic_department = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[6]"
            )
        )
    )

    academic_department.click()

    academic_department_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{academic_department_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        academic_department_option
    )

    academic_department_option.click()

    #     # ==========================================================
    # # ADMISSION DATE
    # # ==========================================================

    # admission_date = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "admission_date"
    #         )
    #     )
    # )

    # admission_date.click()

    # admission_day = admission_date_value.split("/")[0]

    # date = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             f"//td[contains(@class,'day') "
    #             f"and normalize-space()='{admission_day}' "
    #             f"and not(contains(@class,'old')) "
    #             f"and not(contains(@class,'new'))]"
    #         )
    #     )
    # )

    # date.click()

    # ==========================================================
    # GENERATE ADMISSION NUMBER
    # ==========================================================

    generate_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "generateAdmissionNumberBtn"
            )
        )
    )

    generate_button.click()

    # ==========================================================
    # FIRST NAME
    # ==========================================================

    first_name = wait.until(
        EC.element_to_be_clickable(
            (
                By.NAME,
                "first_name"
            )
        )
    )

    first_name.send_keys(first_name_value)

    # ==========================================================
    # LAST NAME
    # ==========================================================

    last_name = wait.until(
        EC.element_to_be_clickable(
            (
                By.NAME,
                "last_name"
            )
        )
    )

    last_name.send_keys(last_name_value)

    # ==========================================================
    # EMAIL
    # ==========================================================

    email = wait.until(
        EC.element_to_be_clickable(
            (
                By.NAME,
                "email_address"
            )
        )
    )

    email.send_keys(email_value)

    # ==========================================================
    # STUDENT CATEGORY
    # ==========================================================

    student_category = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@class='nice-select primary_select form-control feedback_input_types']"
            )
        )
    )

    student_category.click()

    student_category_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{student_category_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        student_category_option
    )

    student_category_option.click()

    # ==========================================================
    # PHONE NUMBER
    # ==========================================================

    phone_number = wait.until(
        EC.element_to_be_clickable(
            (
                By.NAME,
                "phone_number"
            )
        )
    )

    phone_number.send_keys(phone_number_value)

    # ==========================================================
    # SAVE BUTTON
    # ==========================================================

    save_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "submitButton"
            )
        )
    )

    save_button.click()

    # ==========================================================
    # VERIFY SUCCESS
    # ==========================================================

    # Change this XPath according to your application's
    # actual success message.

    # success_message = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//*[contains(text(),'successfully')]"
    #         )
    #     )
    # )

    # assert success_message.is_displayed()

    # ==========================================================
    # DELETE BUTTON
    # ==========================================================

    # delete_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//a[contains(@class,'delete-button-datatable')])[1]"
    #         )
    #     )
    # )
    #
    # delete_button.click()

    # ==========================================================
    # DELETE CONFIRMATION POPUP
    # ==========================================================

    # confirmation_popup = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//div[@aria-describedby='swal2-html-container']"
    #         )
    #     )
    # )

    # ==========================================================
    # CANCEL DELETE
    # ==========================================================

    # cancel_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//button[contains(@class,'swal2-cancel')]"
    #         )
    #     )
    # )
    #
    # cancel_button.click()

    # ==========================================================
    # CONFIRM DELETE
    # ==========================================================

    # confirm_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//button[contains(@class,'swal2-confirm')]"
    #         )
    #     )
    # )
    #
    # confirm_button.click()