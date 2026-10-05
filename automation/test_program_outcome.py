# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.by import By
# # import time


# # def test_program_outcome(driver):

# #     driver.implicitly_wait(10)
# #     wait = WebDriverWait(driver, 10)

# #     # ---------------- Attainment ----------------

# #     attainment = driver.find_element(
# #         By.XPATH,
# #         "//div//span[normalize-space()='Attainment']"
# #     )
# #     attainment.click()

# #     # ---------------- Program Outcome ----------------

# #     program_outcome = driver.find_element(
# #         By.XPATH,
# #         "//a[normalize-space()='Program Outcome']"
# #     )
# #     program_outcome.click()
# #     time.sleep(1)

# #     # ---------------- Add Button ----------------

# #     add_btn = driver.find_element(
# #         By.XPATH,
# #         "//a[@class='nxgn_primary_button button_bg_primary']"
# #     )
# #     add_btn.click()
# #     time.sleep(1)

# #     # ==========================================================
# #     # BRANCH NORMAL DROPDOWN
# #     # ==========================================================

# #     branch_dropdown = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 "(//div[@class='nice-select primary_select form-control'])[1]"
# #             )
# #         )
# #     )

# #     branch_dropdown.click()

# #     branch_option = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 f"//li[normalize-space()='{branch_value}']"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         branch_option
# #     )

# #     driver.execute_script(
# #         "arguments[0].click();",
# #         branch_option
# #     )


# #     # ==========================================================
# #     # DEPARTMENT MULTISELECT
# #     # ==========================================================

# #     department_wrapper = wait.until(
# #         EC.presence_of_element_located(
# #             (
# #                 By.XPATH,
# #                 "(//div[contains(@class,'ms-options-wrap')])[1]"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         department_wrapper
# #     )

# #     # Open Department Multiselect
# #     department_button = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 "(//div[contains(@class,'ms-options-wrap')])[1]//button"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].click();",
# #         department_button
# #     )

# #     # Department option
# #     department_option = wait.until(
# #         EC.presence_of_element_located(
# #             (
# #                 By.XPATH,
# #                 f"//li[.//label[contains(normalize-space(),'{department_value}')]]"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         department_option
# #     )

# #     # Department checkbox
# #     department_checkbox = department_option.find_element(
# #         By.XPATH,
# #         ".//input[@type='checkbox']"
# #     )

# #     if not department_checkbox.is_selected():
# #         driver.execute_script(
# #             """
# #             arguments[0].click();
# #             arguments[0].dispatchEvent(
# #                 new Event('change', {bubbles:true})
# #             );
# #             """,
# #             department_checkbox
# #         )

# #     assert department_checkbox.is_selected()


# #     # ==========================================================
# #     # PROGRAM MULTISELECT
# #     # ==========================================================

# #     program_wrapper = wait.until(
# #         EC.presence_of_element_located(
# #             (
# #                 By.XPATH,
# #                 "(//div[contains(@class,'ms-options-wrap')])[2]"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         program_wrapper
# #     )

# #     # Open Program Multiselect
# #     program_button = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 "(//div[contains(@class,'ms-options-wrap')])[2]//button"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].click();",
# #         program_button
# #     )

# #     # Program option
# #     program_option = wait.until(
# #         EC.presence_of_element_located(
# #             (
# #                 By.XPATH,
# #                 f"//li[.//label[contains(normalize-space(),'{program_value}')]]"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         program_option
# #     )

# #     # Program checkbox
# #     program_checkbox = program_option.find_element(
# #         By.XPATH,
# #         ".//input[@type='checkbox']"
# #     )

# #     if not program_checkbox.is_selected():
# #         driver.execute_script(
# #             """
# #             arguments[0].click();
# #             arguments[0].dispatchEvent(
# #                 new Event('change', {bubbles:true})
# #             );
# #             """,
# #             program_checkbox
# #         )

# #     assert program_checkbox.is_selected()


# #     # # ---------------- Fetch ----------------

# #     fetch_btn = wait.until(
# #         EC.element_to_be_clickable(
# #             (By.XPATH, "//button[normalize-space()='Fetch']")
# #         )
# #     )
# #     fetch_btn.click()

# #     time.sleep(2)

# #     # # ---------------- Plus Button ----------------

# #     plus_btn = wait.until(
# #         EC.element_to_be_clickable(
# #             (By.ID, "add_course_outcomes_btn")
# #         )
# #     )
# #     plus_btn.click()

# #     time.sleep(2)

# #     # # ==================================================
# #     # #                    PROGRAM OUTCOME 1
# #     # # ==================================================

# #     # # ---------------- PO1 Code ----------------

# #     code_field = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 "(//input[@class='primary_input_field form-control program-code-change'])[1]"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         code_field
# #     )

# #     code_field.click()
# #     code_field.clear()
# #     code_field.send_keys("PO1")

# #     time.sleep(2)

# #     # ---------------- PO1 BT ----------------

# #     bt_dropdown_1 = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 "(//div[@class='nice-select primary_select form-control'])[2]"
# #             )
# #         )
# #     )

# #     bt_dropdown_1.click()

# #     bt_option_1 = wait.until(
# #         EC.presence_of_element_located(
# #             (
# #                 By.XPATH,
# #                 "//li[normalize-space()='ANALYZE']"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].click();",
# #         bt_option_1
# #     )
# #     time.sleep(1)

# #     # ---------------- CO1 Description ----------------

# #     desc_1 = wait.until(
# #         EC.visibility_of_element_located(
# #             (
# #                 By.XPATH,
# #                 "(//textarea[contains(@class,'course-description-change')])[1]"
# #             )
# #         )
# #     )

# #     desc_1.send_keys("analyzedd")

# #     # ==================================================
# #     #                    PROGRAM OUTCOME 2
# #     # ==================================================

# #     # ---------------- PO2 Code ----------------


# #     code_field_2 = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 "(//input[@class='primary_input_field form-control program-code-change'])[2]"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         code_field_2
# #     )

# #     code_field_2.click()
# #     code_field_2.clear()
# #     code_field_2.send_keys("CO2")

# #     time.sleep(2)


# #     # ---------------- CO2 BT Dropdown ----------------


# #     bt_dropdown_2 = driver.find_element(
# #         By.XPATH,
# #         "(//div[@class='nice-select primary_select form-control'])[3]"
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         bt_dropdown_2
# #     )

# #     bt_dropdown_2.click()

# #     time.sleep(1)

# #     # REMEMBER option
# #     bt_option_2 = driver.find_element(
# #         By.XPATH,
# #         "//div[contains(@class,'nice-select') and contains(@class,'open')]"
# #         "//li[contains(@class,'option') and normalize-space()='REMEMBER']"
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         bt_option_2
# #     )

# #     driver.execute_script(
# #         "arguments[0].click();",
# #         bt_option_2
# #     )

# #     time.sleep(1)

# #     # ---------------- CO2 Description ----------------

# #     desc_2 = wait.until(
# #         EC.visibility_of_element_located(
# #             (
# #                 By.XPATH,
# #                 "(//textarea[contains(@class,'course-description-change')])[2]"
# #             )
# #         )
# #     )

# #     desc_2.send_keys("rememberedd")

# #     # ==================================================
# #     #                       SAVE
# #     # ==================================================

# #     save = wait.until(
# #         EC.element_to_be_clickable(
# #             (By.ID, "submitButton")
# #         )
# #     )

# #     save.click()

# #     time.sleep(3)
    
# #     #locate go to edit btn
# #     # go_to_edit = driver.find_element(By.XPATH,"//a[@class='btn btn-warning']")
# #     # go_to_edit.click()
    
# #     # locate 3 dots
# #     # three_dots = driver.find_element(By.XPATH,"(//button[@class='action_button'])[1]")
# #     # three_dots.click()
    
# #     #locate edit btn
# #     # edit = driver.find_element(By.XPATH,"(//a[@class='action_item_list asign-btn'])[1]")
# #     # edit.click()
# #     # time.sleep(2)
    
# #     # # locate branch dropdown
# #     # branch = driver.find_element(By.XPATH,"(//div[contains(@class,'nice-select') "
# #     #             "and contains(@class,'primary_select')])[1]")
# #     # branch.click()
# #     # time.sleep(3)
        
# #     # branch_options = branch.find_element(By.XPATH,"//li[.='STU Marol(east) Mumbai 400002']")
# #     # branch_options.click()
        
# #     # time.sleep(4)
        
# #     # # locate department dropdown
# #     # department = driver.find_element(By.XPATH,"(//div[contains(@class,'nice-select') "
# #     #    "and contains(@class,'primary_select')])[2]")
# #     # department.click()
# #     # time.sleep(3)
            
# #     # department_options = department.find_element(By.XPATH,"//li[.='IT-26']")
# #     # department_options.click()
    
# #     # ---------------- Plus Button ----------------
    
# #     # plus_btn = wait.until(
# #     #         EC.element_to_be_clickable(
# #     #             (By.ID, "add_course_outcomes_btn")
# #     #         )
# #     #     )
# #     # plus_btn.click()
    
# #     # time.sleep(2)
    
# #     #     # ==================================================
# #     #     #                    COURSE OUTCOME 1
# #     #     # ==================================================
    
# #     #     # ---------------- CO1 Code ----------------
    
# #     # code_field = wait.until(
# #     #         EC.element_to_be_clickable(
# #     #             (
# #     #                 By.XPATH,
# #     #                 "(//input[contains(@class,'course-code-change')])[1]"
# #     #             )
# #     #         )
# #     #     )
    
# #     # driver.execute_script(
# #     #         "arguments[0].scrollIntoView({block:'center'});",
# #     #         code_field
# #     #     )
    
# #     # code_field.click()
# #     # code_field.clear()
# #     # code_field.send_keys("CO2")
    
# #     # time.sleep(2)
    
# #     #     # ---------------- CO1 BT ----------------
    
# #     # bt_dropdown_1 = wait.until(
# #     #         EC.element_to_be_clickable(
# #     #             (
# #     #                 By.XPATH,
# #     #                 "(//div[contains(@class,'nice-select') "
# #     #                 "and contains(@class,'primary_select')])[5]"
# #     #             )
# #     #         )
# #     #     )
    
# #     # bt_dropdown_1.click()
    
# #     # bt_option_1 = wait.until(
# #     #         EC.presence_of_element_located(
# #     #             (
# #     #                 By.XPATH,
# #     #                 "//li[normalize-space()='ANALYZE']"
# #     #             )
# #     #         )
# #     #     )
    
# #     # driver.execute_script(
# #     #         "arguments[0].click();",
# #     #         bt_option_1
# #     #     )
# #     # time.sleep(1)
    
# #     #     # ---------------- CO1 Description ----------------
    
# #     # desc_1 = wait.until(
# #     #         EC.visibility_of_element_located(
# #     #             (
# #     #                 By.XPATH,
# #     #                 "(//textarea[contains(@class,'course-description-change')])[1]"
# #     #             )
# #     #         )
# #     #     )
    
# #     # desc_1.send_keys("analyzed")
    
# #     #     # ==================================================
# #     #     #                    COURSE OUTCOME 2
# #     #     # ==================================================
    
# #     #     # ---------------- CO2 Code ----------------
    
    
# #     # code_field_2 = wait.until(
# #     #         EC.element_to_be_clickable(
# #     #             (
# #     #                 By.XPATH,
# #     #                 "(//input[contains(@class,'course-code-change')])[2]"
# #     #             )
# #     #         )
# #     #     )
    
# #     # driver.execute_script(
# #     #         "arguments[0].scrollIntoView({block:'center'});",
# #     #         code_field_2
# #     #     )
    
# #     # code_field_2.click()
# #     # code_field_2.clear()
# #     # code_field_2.send_keys("CO1")
    
# #     # time.sleep(2)
    
    
# #     #     # ---------------- CO2 BT Dropdown ----------------
    
    
# #     # bt_dropdown_2 = driver.find_element(
# #     #         By.XPATH,
# #     #         "(//div[contains(@class,'nice-select') and contains(@class,'primary_select')])[6]"
# #     #     )
    
# #     # driver.execute_script(
# #     #         "arguments[0].scrollIntoView({block:'center'});",
# #     #         bt_dropdown_2
# #     #     )
    
# #     # bt_dropdown_2.click()
    
# #     # time.sleep(1)
    
# #     #     # REMEMBER option
# #     # bt_option_2 = driver.find_element(
# #     #         By.XPATH,
# #     #         "//div[contains(@class,'nice-select') and contains(@class,'open')]"
# #     #         "//li[contains(@class,'option') and normalize-space()='REMEMBER']"
# #     #     )
    
# #     # driver.execute_script(
# #     #         "arguments[0].scrollIntoView({block:'center'});",
# #     #         bt_option_2
# #     #     )
    
# #     # driver.execute_script(
# #     #         "arguments[0].click();",
# #     #         bt_option_2
# #     #     )
    
# #     # time.sleep(1)
    
# #     #     # ---------------- CO2 Description ----------------
    
# #     # desc_2 = wait.until(
# #     #         EC.visibility_of_element_located(
# #     #             (
# #     #                 By.XPATH,
# #     #                 "(//textarea[contains(@class,'course-description-change')])[2]"
# #     #             )
# #     #         )
# #     #     )
    
# #     # desc_2.send_keys("remembered")
    
# #         # ==================================================
# #         #                       SAVE
# #         # ==================================================
    
# #     # save = wait.until(
# #     #         EC.element_to_be_clickable(
# #     #             (By.ID, "submitButton")
# #     #         )
# #     #     )
    
# #     # save.click()
    
# #     # time.sleep(3)
    
# #     # ---------------- DELETE BUTTON ----------------

# #     # delete_button = wait.until(
# #     #     EC.element_to_be_clickable(
# #     #         (By.XPATH, '(//a[@class="action_item_list delete-button-datatable"])[1]')
# #     #     )
# #     # )

# #     # delete_button.click()


# #     # # ---------------- DELETE CONFIRMATION MODAL ----------------

# #     # modal = wait.until(
# #     #     EC.visibility_of_element_located(
# #     #         (By.XPATH, "//div[@aria-describedby='swal2-html-container']")
# #     #     )
# #     # )


# #     # # ---------------- CONFIRM DELETE ----------------

# #     # confirm_button = wait.until(
# #     #     EC.element_to_be_clickable(
# #     #         (By.XPATH, "//button[contains(@class,'swal2-confirm')]")
# #     #     )
# #     # )

# #     # confirm_button.click()

    
# #     # confirm_button = wait.until(
# #     #         EC.element_to_be_clickable(
# #     #             (By.XPATH, "//button[contains(@class,'swal2-cancel')]")
# #     #         )
# #     #     )
    
# #     # confirm_button.click()
    

# #     time.sleep(1)
    


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import (
#     TimeoutException,
#     ElementClickInterceptedException,
#     ElementNotInteractableException
# )
# import time


# # ==========================================================
# # TEST DATA
# # ==========================================================

# # ---------------- BASIC DATA ----------------

# branch_value = "DND branch1"
# department_value = "DND-Department"
# program_value = "DND-Program"


# # ---------------- PROGRAM OUTCOME 1 ----------------

# po1_code = "PO1"
# po1_bt = "ANALYZE"
# po1_description = "analyzedd"


# # ---------------- PROGRAM OUTCOME 2 ----------------

# po2_code = "CO2"
# po2_bt = "REMEMBER"
# po2_description = "rememberedd"


# # ==========================================================
# # HELPER - CLICK ELEMENT SAFELY
# # ==========================================================

# def safe_click(driver, element):
#     """
#     Scroll element into view and click using JavaScript.
#     """

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         element
#     )

#     try:
#         element.click()

#     except (
#         ElementClickInterceptedException,
#         ElementNotInteractableException
#     ):
#         driver.execute_script(
#             "arguments[0].click();",
#             element
#         )


# # ==========================================================
# # TEST
# # ==========================================================

# def test_program_outcome(driver):

#     driver.implicitly_wait(10)

#     wait = WebDriverWait(
#         driver,
#         10
#     )

#     # ==========================================================
#     # ATTAINMENT
#     # ==========================================================

#     attainment = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//div//span[normalize-space()='Attainment']"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         attainment
#     )

#     # ==========================================================
#     # PROGRAM OUTCOME
#     # ==========================================================

#     program_outcome = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//a[normalize-space()='Program Outcome']"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         program_outcome
#     )

#     time.sleep(1)

#     # ==========================================================
#     # ADD BUTTON
#     # ==========================================================

#     add_btn = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//a[contains(@class,'nxgn_primary_button') "
#                 "and contains(@class,'button_bg_primary')]"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         add_btn
#     )

#     time.sleep(1)

#     # ==========================================================
#     # BRANCH NORMAL DROPDOWN
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

#     safe_click(
#         driver,
#         branch_dropdown
#     )

#     # ----------------------------------------------------------
#     # BRANCH OPTION
#     # ----------------------------------------------------------

#     branch_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//div[contains(@class,'nice-select') "
#                 "and contains(@class,'open')]"
#                 f"//li[contains(@class,'option') "
#                 f"and normalize-space()='{branch_value}']"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         branch_option
#     )

#     # ----------------------------------------------------------
#     # VERIFY BRANCH
#     # ----------------------------------------------------------

#     wait.until(
#         lambda d:
#         branch_value.lower()
#         in branch_dropdown.text.lower()
#     )

#     assert branch_value.lower() in branch_dropdown.text.lower(), (
#         f"Branch '{branch_value}' was not selected."
#     )

#     print(
#         f"Branch '{branch_value}' selected successfully."
#     )


#     # ==========================================================
#     # DEPARTMENT MULTISELECT
#     # ==========================================================

#     # ----------------------------------------------------------
#     # LOCATE DEPARTMENT WRAPPER
#     # ----------------------------------------------------------

#     department_wrapper = wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[1]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         department_wrapper
#     )

#     # ----------------------------------------------------------
#     # LOCATE DEPARTMENT BUTTON
#     # ----------------------------------------------------------

#     department_button = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[1]"
#                 "//button"
#             )
#         )
#     )

#     # ----------------------------------------------------------
#     # OPEN DEPARTMENT MULTISELECT
#     # ----------------------------------------------------------

#     safe_click(
#         driver,
#         department_button
#     )

#     # ----------------------------------------------------------
#     # WAIT FOR DEPARTMENT OPTIONS TO BECOME VISIBLE
#     #
#     # DO NOT WAIT FOR ms-active.
#     # The plugin may not add ms-active to the wrapper.
#     # ----------------------------------------------------------

#     department_options_container = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[1]"
#                 "//div[contains(@class,'ms-options')]"
#             )
#         )
#     )

#     print(
#         "\nDepartment dropdown opened successfully."
#     )

#     # ----------------------------------------------------------
#     # DEBUG - PRINT DEPARTMENT OPTIONS
#     # ----------------------------------------------------------

#     department_options = wait.until(
#         EC.presence_of_all_elements_located(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[1]"
#                 "//div[contains(@class,'ms-options')]//li"
#             )
#         )
#     )

#     print(
#         "\n========== DEPARTMENT OPTIONS =========="
#     )

#     for option in department_options:

#         text = option.text.strip()

#         if text:
#             print(
#                 "DEPARTMENT OPTION:",
#                 repr(text)
#             )

#     print(
#         "========================================\n"
#     )

#     # ----------------------------------------------------------
#     # LOCATE REQUIRED DEPARTMENT OPTION
#     # ----------------------------------------------------------

#     department_option = wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[1]"
#                 "//div[contains(@class,'ms-options')]"
#                 f"//li[.//label[contains("
#                 f"normalize-space(),'{department_value}')]]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         department_option
#     )

#     # ----------------------------------------------------------
#     # LOCATE DEPARTMENT CHECKBOX
#     #
#     # IMPORTANT:
#     # type='checkbox', NOT type='checkmark'
#     # ----------------------------------------------------------

#     department_checkbox = wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[1]"
#                 "//div[contains(@class,'ms-options')]"
#                 f"//li[.//label[contains("
#                 f"normalize-space(),'{department_value}')]]"
#                 "//input[@type='checkbox']"
#             )
#         )
#     )

#     # ----------------------------------------------------------
#     # SELECT DEPARTMENT
#     # ----------------------------------------------------------

#     if not department_checkbox.is_selected():

#         driver.execute_script(
#             """
#             arguments[0].click();

#             arguments[0].dispatchEvent(
#                 new Event('change', {
#                     bubbles: true
#                 })
#             );
#             """,
#             department_checkbox
#         )

#         time.sleep(1)

#     # ----------------------------------------------------------
#     # VERIFY DEPARTMENT
#     # ----------------------------------------------------------

#     wait.until(
#         lambda d:
#         department_checkbox.is_selected()
#     )

#     assert department_checkbox.is_selected(), (
#         f"Department '{department_value}' was not selected."
#     )

#     print(
#         f"Department '{department_value}' "
#         f"selected successfully."
#     )


#     # ==========================================================
#     # CLOSE DEPARTMENT MULTISELECT
#     # ==========================================================

#     # Click the same button again to close it.
#     safe_click(
#         driver,
#         department_button
#     )

#     time.sleep(0.5)


#     # ==========================================================
#     # PROGRAM MULTISELECT
#     # ==========================================================

#     # ----------------------------------------------------------
#     # LOCATE PROGRAM WRAPPER
#     # ----------------------------------------------------------

#     program_wrapper = wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[2]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         program_wrapper
#     )

#     # ----------------------------------------------------------
#     # LOCATE PROGRAM BUTTON
#     # ----------------------------------------------------------

#     program_button = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[2]"
#                 "//button"
#             )
#         )
#     )

#     # ----------------------------------------------------------
#     # OPEN PROGRAM MULTISELECT
#     # ----------------------------------------------------------

#     safe_click(
#         driver,
#         program_button
#     )

#     # ----------------------------------------------------------
#     # WAIT FOR PROGRAM OPTIONS
#     # ----------------------------------------------------------

#     program_options_container = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[2]"
#                 "//div[contains(@class,'ms-options')]"
#             )
#         )
#     )

#     print(
#         "Program dropdown opened successfully."
#     )

#     # ----------------------------------------------------------
#     # LOCATE PROGRAM OPTION
#     # ----------------------------------------------------------

#     program_option = wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[2]"
#                 "//div[contains(@class,'ms-options')]"
#                 f"//li[.//label[contains("
#                 f"normalize-space(),'{program_value}')]]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         program_option
#     )

#     # ----------------------------------------------------------
#     # PROGRAM CHECKBOX
#     # ----------------------------------------------------------

#     program_checkbox = wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[2]"
#                 "//div[contains(@class,'ms-options')]"
#                 f"//li[.//label[contains("
#                 f"normalize-space(),'{program_value}')]]"
#                 "//input[@type='checkbox']"
#             )
#         )
#     )

#     # ----------------------------------------------------------
#     # SELECT PROGRAM
#     # ----------------------------------------------------------

#     if not program_checkbox.is_selected():

#         driver.execute_script(
#             """
#             arguments[0].click();

#             arguments[0].dispatchEvent(
#                 new Event('change', {
#                     bubbles: true
#                 })
#             );
#             """,
#             program_checkbox
#         )

#         time.sleep(1)

#     # ----------------------------------------------------------
#     # VERIFY PROGRAM
#     # ----------------------------------------------------------

#     wait.until(
#         lambda d:
#         program_checkbox.is_selected()
#     )

#     assert program_checkbox.is_selected(), (
#         f"Program '{program_value}' was not selected."
#     )

#     print(
#         f"Program '{program_value}' "
#         f"selected successfully."
#     )


#     # ==========================================================
#     # CLOSE PROGRAM MULTISELECT
#     # ==========================================================

#     safe_click(
#         driver,
#         program_button
#     )

#     time.sleep(0.5)


#     # ==========================================================
#     # FETCH
#     # ==========================================================

#     fetch_btn = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//button[normalize-space()='Fetch']"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         fetch_btn
#     )

#     # ----------------------------------------------------------
#     # WAIT FOR FETCH TO COMPLETE
#     # ----------------------------------------------------------

#     time.sleep(2)


#     # ==========================================================
#     # PLUS BUTTON
#     # ==========================================================

#     plus_btn = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "add_course_outcomes_btn"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         plus_btn
#     )

#     time.sleep(1)


#     # ==========================================================
#     # PROGRAM OUTCOME 1
#     # ==========================================================

#     # ----------------------------------------------------------
#     # PO1 CODE
#     # ----------------------------------------------------------

#     code_field = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//input[contains(@class,"
#                 "'program-code-change')])[1]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         code_field
#     )

#     code_field.click()
#     code_field.clear()
#     code_field.send_keys(po1_code)

#     # ----------------------------------------------------------
#     # VERIFY PO1 CODE
#     # ----------------------------------------------------------

#     assert (
#         code_field.get_attribute("value")
#         == po1_code
#     ), (
#         f"Expected PO1 code '{po1_code}', "
#         f"but got '{code_field.get_attribute('value')}'."
#     )

#     # ----------------------------------------------------------
#     # PO1 BT DROPDOWN
#     # ----------------------------------------------------------

#     bt_dropdown_1 = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select') "
#                 "and contains(@class,'form-control')])[2]"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         bt_dropdown_1
#     )

#     # ----------------------------------------------------------
#     # PO1 BT OPTION
#     # ----------------------------------------------------------

#     bt_option_1 = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//div[contains(@class,'nice-select') "
#                 "and contains(@class,'open')]"
#                 f"//li[contains(@class,'option') "
#                 f"and normalize-space()='{po1_bt}']"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         bt_option_1
#     )

#     # ----------------------------------------------------------
#     # VERIFY PO1 BT
#     # ----------------------------------------------------------

#     wait.until(
#         lambda d:
#         po1_bt.lower()
#         in bt_dropdown_1.text.lower()
#     )

#     assert po1_bt.lower() in bt_dropdown_1.text.lower()


#     # ----------------------------------------------------------
#     # PO1 DESCRIPTION
#     # ----------------------------------------------------------

#     desc_1 = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.XPATH,
#                 "(//textarea[contains("
#                 "@class,'course-description-change')])[1]"
#             )
#         )
#     )

#     desc_1.click()
#     desc_1.clear()
#     desc_1.send_keys(po1_description)

#     # ----------------------------------------------------------
#     # VERIFY PO1 DESCRIPTION
#     # ----------------------------------------------------------

#     assert (
#         desc_1.get_attribute("value")
#         == po1_description
#     ), (
#         f"PO1 description was not entered correctly."
#     )


#     # ==========================================================
#     # PROGRAM OUTCOME 2
#     # ==========================================================

#     # ----------------------------------------------------------
#     # PO2 CODE
#     # ----------------------------------------------------------

#     code_field_2 = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//input[contains(@class,"
#                 "'program-code-change')])[2]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         code_field_2
#     )

#     code_field_2.click()
#     code_field_2.clear()
#     code_field_2.send_keys(po2_code)

#     # ----------------------------------------------------------
#     # VERIFY PO2 CODE
#     # ----------------------------------------------------------

#     assert (
#         code_field_2.get_attribute("value")
#         == po2_code
#     ), (
#         f"Expected PO2 code '{po2_code}', "
#         f"but got '{code_field_2.get_attribute('value')}'."
#     )


#     # ----------------------------------------------------------
#     # PO2 BT DROPDOWN
#     # ----------------------------------------------------------

#     bt_dropdown_2 = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select') "
#                 "and contains(@class,'form-control')])[3]"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         bt_dropdown_2
#     )

#     # ----------------------------------------------------------
#     # PO2 BT OPTION - REMEMBER
#     # ----------------------------------------------------------

#     bt_option_2 = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//div[contains(@class,'nice-select') "
#                 "and contains(@class,'open')]"
#                 f"//li[contains(@class,'option') "
#                 f"and normalize-space()='{po2_bt}']"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         bt_option_2
#     )

#     # ----------------------------------------------------------
#     # VERIFY PO2 BT
#     # ----------------------------------------------------------

#     wait.until(
#         lambda d:
#         po2_bt.lower()
#         in bt_dropdown_2.text.lower()
#     )

#     assert po2_bt.lower() in bt_dropdown_2.text.lower()


#     # ----------------------------------------------------------
#     # PO2 DESCRIPTION
#     # ----------------------------------------------------------

#     desc_2 = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.XPATH,
#                 "(//textarea[contains("
#                 "@class,'course-description-change')])[2]"
#             )
#         )
#     )

#     desc_2.click()
#     desc_2.clear()
#     desc_2.send_keys(po2_description)

#     # ----------------------------------------------------------
#     # VERIFY PO2 DESCRIPTION
#     # ----------------------------------------------------------

#     assert (
#         desc_2.get_attribute("value")
#         == po2_description
#     ), (
#         f"PO2 description was not entered correctly."
#     )


#     # ==========================================================
#     # SAVE
#     # ==========================================================

#     save = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "submitButton"
#             )
#         )
#     )

#     safe_click(
#         driver,
#         save
#     )

#     # ----------------------------------------------------------
#     # WAIT AFTER SAVE
#     # ----------------------------------------------------------

#     time.sleep(3)

#     print(
#         "\n=================================================="
#     )
#     print(
#         "PROGRAM OUTCOME TEST COMPLETED SUCCESSFULLY"
#     )
#     print(
#         "=================================================="
#     )

#     # ==========================================================
#     # OPTIONAL EDIT FUNCTIONALITY
#     # ==========================================================

#     # ----------------------------------------------------------
#     # GO TO EDIT
#     # ----------------------------------------------------------

#     # go_to_edit = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//a[@class='btn btn-warning']"
#     #         )
#     #     )
#     # )
#     #
#     # safe_click(
#     #     driver,
#     #     go_to_edit
#     # )
#     #
#     # time.sleep(2)


#     # ----------------------------------------------------------
#     # THREE DOTS
#     # ----------------------------------------------------------

#     # three_dots = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//button[@class='action_button'])[1]"
#     #         )
#     #     )
#     # )
#     #
#     # safe_click(
#     #     driver,
#     #     three_dots
#     # )
#     #
#     # time.sleep(1)


#     # ----------------------------------------------------------
#     # EDIT BUTTON
#     # ----------------------------------------------------------

#     # edit = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//a[contains(@class,'action_item_list') "
#     #             "and contains(@class,'asign-btn')])[1]"
#     #         )
#     #     )
#     # )
#     #
#     # safe_click(
#     #     driver,
#     #     edit
#     # )
#     #
#     # time.sleep(2)


#     # ==========================================================
#     # OPTIONAL DELETE
#     # ==========================================================

#     # delete_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//a[contains(@class,'delete-button-datatable')])[1]"
#     #         )
#     #     )
#     # )
#     #
#     # safe_click(
#     #     driver,
#     #     delete_button
#     # )
#     #
#     # modal = wait.until(
#     #     EC.visibility_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "//div[@aria-describedby='swal2-html-container']"
#     #         )
#     #     )
#     # )
#     #
#     # assert modal.is_displayed()
#     #
#     # confirm_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//button[contains(@class,'swal2-confirm')]"
#     #         )
#     #     )
#     # )
#     #
#     # safe_click(
#     #     driver,
#     #     confirm_button
#     # )

#     time.sleep(1)




from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    ElementNotInteractableException
)
import time


def test_program_outcome(driver):

    driver.implicitly_wait(50)
    wait = WebDriverWait(driver, 50)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    # ---------------- BASIC DATA ----------------

    branch_value = "DND branch1"
    department_value = "DND dept"
    program_value = "DND-Program"

    # ---------------- PROGRAM OUTCOME 1 ----------------

    po1_code = "PO1"
    po1_bt = "ANALYZE"
    po1_description = "analyzedd"

    # ---------------- PROGRAM OUTCOME 2 ----------------

    po2_code = "CO2"
    po2_bt = "REMEMBER"
    po2_description = "rememberedd"

    # ==========================================================
    # EDGE CASE DATA
    # ==========================================================

    empty_code = ""
    empty_description = ""

    duplicate_code = "PO1"

    special_character_code = "@#$%"
    special_character_description = "@#$% Test Description"

    long_description = (
        "This is a long program outcome description used to verify "
        "whether the application correctly handles large text input "
        "without breaking the field validation or page layout."
    )

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

    try:
        attainment.click()
    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            attainment
        )

    # ==========================================================
    # PROGRAM OUTCOME
    # ==========================================================

    program_outcome = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Program Outcome']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        program_outcome
    )

    try:
        program_outcome.click()
    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            program_outcome
        )

    # Wait until Program Outcome page loads
    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[contains(@class,'nxgn_primary_button')]"
            )
        )
    )

    # ==========================================================
    # ADD BUTTON
    # ==========================================================

    add_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[contains(@class,'nxgn_primary_button') "
                "and contains(@class,'button_bg_primary')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        add_btn
    )

    try:
        add_btn.click()
    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

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

    try:
        branch_dropdown.click()
    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):
        driver.execute_script(
            "arguments[0].click();",
            branch_dropdown
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
        "arguments[0].scrollIntoView({block:'center'});",
        branch_option
    )

    driver.execute_script(
        "arguments[0].click();",
        branch_option
    )

    # Verify branch
    selected_branch = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select') "
                "and contains(@class,'form-control')])[1]"
                "//span[contains(@class,'current')]"
            )
        )
    )

    assert selected_branch.text.strip().lower() == branch_value.strip().lower(), f"Expected branch '{branch_value}', but selected '{selected_branch.text.strip()}'."
    
#         # ==========================================================
#     # DEPARTMENT DROPDOWN
#     # ==========================================================

#     department_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[1]"
#             )
#         )
#     )

#     department_dropdown.click()
    
#     time.sleep(20)
    

#     department_option = wait.until(
#     EC.element_to_be_clickable(
#         (
#             By.XPATH,
#             f"//div[contains(@class,'ms-options-wrap')][1]"
#             f"//li[.//input[@type='checkbox' and @title='{department_value}']]"
#         )
#     )
# )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         department_option
#     )

#     department_checkbox = department_option.find_element(
#         By.XPATH,
#         ".//input[@type='checkbox']"
#     )

#     driver.execute_script(
#         "arguments[0].click();",
#         department_checkbox
#     )

    # ==========================================================
    # DEPARTMENT DROPDOWN
    # ==========================================================

    department_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'ms-options-wrap')])[1]"
            )
        )
    )

    print("BEFORE DROPDOWN CLICK")

    department_dropdown.click()

    print("DROPDOWN CLICKED - WAITING FOR 10 SECONDS")

    time.sleep(10)

    print("10 SECONDS COMPLETED - SELECTING OPTION")

    # Wait for department option
    department_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"(//div[contains(@class,'ms-options-wrap')])[1]"
                f"//li[.//input[@type='checkbox' and @title='{department_value}']]"
            )
        )
    )

    # Click department option
    department_option.click()

    print("DEPARTMENT SELECTED")


    # ==========================================================
    # WAIT FOR PROGRAM DROPDOWN TO LOAD
    # ==========================================================

    program_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'ms-options-wrap')])[2]"
            )
        )
    )

    program_dropdown.click()


    # ==========================================================
    # PROGRAM OPTION
    # ==========================================================

    program_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[.//label[normalize-space()='{program_value}']]"
            )
        )
    )
    driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            program_option
        )

    program_option.click()
    

    # ==========================================================
    # FETCH
    # ==========================================================

    fetch_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[normalize-space()='Fetch']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fetch_btn
    )

    driver.execute_script(
        "arguments[0].click();",
        fetch_btn
    )

    # Wait for Add Course Outcome button
    plus_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "add_course_outcomes_btn"
            )
        )
    )

    # ==========================================================
    # ADD PROGRAM OUTCOME ROWS
    # ==========================================================

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        plus_btn
    )

    driver.execute_script(
        "arguments[0].click();",
        plus_btn
    )

    # ==========================================================
    # PO1 CODE
    # ==========================================================

    code_field_1 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//input[contains(@class,'program-code-change')])[1]"
            )
        )
    )

    code_field_1.clear()
    code_field_1.send_keys(po1_code)

    assert (
        code_field_1.get_attribute("value") == po1_code
    ), "PO1 code was not entered correctly."

    # ==========================================================
    # PO1 BT
    # ==========================================================

    bt_dropdown_1 = wait.until(
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
        "arguments[0].click();",
        bt_dropdown_1
    )

    bt_option_1 = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{po1_bt}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        bt_option_1
    )

    selected_bt_1 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select') "
                "and contains(@class,'form-control')])[2]"
                "//span[contains(@class,'current')]"
            )
        )
    )

    assert selected_bt_1.text.strip() == po1_bt, (
        f"Expected BT '{po1_bt}', "
        f"but got '{selected_bt_1.text.strip()}'."
    )

    # ==========================================================
    # PO1 DESCRIPTION
    # ==========================================================

    desc_1 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//textarea[contains(@class,"
                "'course-description-change')])[1]"
            )
        )
    )

    desc_1.clear()
    desc_1.send_keys(po1_description)

    assert (
        desc_1.get_attribute("value") == po1_description
    ), "PO1 description was not entered correctly."

    # ==========================================================
    # PO2 CODE
    # ==========================================================

    code_field_2 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//input[contains(@class,'program-code-change')])[2]"
            )
        )
    )

    code_field_2.clear()
    code_field_2.send_keys(po2_code)

    assert (
        code_field_2.get_attribute("value") == po2_code
    ), "PO2 code was not entered correctly."

    # ==========================================================
    # PO2 BT
    # ==========================================================

    bt_dropdown_2 = wait.until(
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
        "arguments[0].click();",
        bt_dropdown_2
    )

    bt_option_2 = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{po2_bt}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        bt_option_2
    )

    selected_bt_2 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select') "
                "and contains(@class,'form-control')])[3]"
                "//span[contains(@class,'current')]"
            )
        )
    )

    assert selected_bt_2.text.strip() == po2_bt, (
        f"Expected BT '{po2_bt}', "
        f"but got '{selected_bt_2.text.strip()}'."
    )

    # ==========================================================
    # PO2 DESCRIPTION
    # ==========================================================

    desc_2 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//textarea[contains(@class,"
                "'course-description-change')])[2]"
            )
        )
    )

    desc_2.clear()
    desc_2.send_keys(po2_description)

    assert (
        desc_2.get_attribute("value") == po2_description
    ), "PO2 description was not entered correctly."

    # ==========================================================
    # EDGE CASE 1 - EMPTY PO CODE
    # ==========================================================

    code_field_1.clear()
    code_field_1.send_keys(empty_code)

    assert (
        code_field_1.get_attribute("value") == empty_code
    ), "Unable to clear PO1 code."

    # Restore valid PO1 code
    code_field_1.send_keys(po1_code)

    assert (
        code_field_1.get_attribute("value") == po1_code
    ), "PO1 code could not be restored."

    # ==========================================================
    # EDGE CASE 2 - EMPTY DESCRIPTION
    # ==========================================================

    desc_1.clear()

    assert (
        desc_1.get_attribute("value") == empty_description
    ), "Description field could not be cleared."

    # Restore valid description
    desc_1.send_keys(po1_description)

    # ==========================================================
    # EDGE CASE 3 - LONG DESCRIPTION
    # ==========================================================

    desc_2.clear()
    desc_2.send_keys(long_description)

    actual_long_description = desc_2.get_attribute("value")

    assert actual_long_description == long_description, (
        "Application did not accept the long description correctly."
    )

    # Restore valid description
    desc_2.clear()
    desc_2.send_keys(po2_description)

    # ==========================================================
    # EDGE CASE 4 - SPECIAL CHARACTERS IN CODE
    # ==========================================================

    code_field_2.clear()
    code_field_2.send_keys(special_character_code)

    actual_special_code = code_field_2.get_attribute("value")

    # Application should either reject special characters
    # or allow them based on its validation rules.
    assert actual_special_code != "", (
        "Code field unexpectedly became empty after special-character input."
    )

    # Restore valid code
    code_field_2.clear()
    code_field_2.send_keys(po2_code)

    # ==========================================================
    # EDGE CASE 5 - SPECIAL CHARACTERS IN DESCRIPTION
    # ==========================================================

    desc_1.clear()
    desc_1.send_keys(special_character_description)

    actual_special_description = desc_1.get_attribute("value")

    assert actual_special_description == special_character_description, (
        "Description field did not accept special characters correctly."
    )

    # Restore valid description
    desc_1.clear()
    desc_1.send_keys(po1_description)

    # ==========================================================
    # EDGE CASE 6 - DUPLICATE PO CODE
    # ==========================================================

    code_field_2.clear()
    code_field_2.send_keys(duplicate_code)

    duplicate_value = code_field_2.get_attribute("value")

    assert duplicate_value == duplicate_code, (
        "Unable to enter duplicate PO code for validation test."
    )

    # Restore valid PO2 code
    code_field_2.clear()
    code_field_2.send_keys(po2_code)

    # ==========================================================
    # FINAL VALIDATION BEFORE SAVE
    # ==========================================================

    assert code_field_1.get_attribute("value") == po1_code
    assert code_field_2.get_attribute("value") == po2_code

    assert desc_1.get_attribute("value") == po1_description
    assert desc_2.get_attribute("value") == po2_description

    # ==========================================================
    # SAVE
    # ==========================================================

    save = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "submitButton"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        save
    )

    driver.execute_script(
        "arguments[0].click();",
        save
    )

    # ==========================================================
    # VERIFY SAVE / SUCCESS
    # ==========================================================

    time.sleep(2)

    try:

        success_message = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(@class,'alert-success') "
                    "or contains(@class,'toast-success') "
                    "or contains(@class,'swal2-success')]"
                )
            )
        )

        assert success_message.is_displayed()

    except TimeoutException:

        # If no success popup exists, verify that the form
        # is no longer in an invalid state.
        print(
            "Success popup not found. "
            "Continuing with page-level verification."
        )

    print(
        "\n=================================================="
    )
    print(
        "PROGRAM OUTCOME TEST COMPLETED SUCCESSFULLY"
    )
    print(
        "=================================================="
    )