# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time

# def test_attainment_criteria(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 15)

#     # ---------------- Attainment ----------------

#     attainment = driver.find_element(
#         By.XPATH,
#         "//div//span[normalize-space()='Attainment']"
#     )
#     attainment.click()
    
#     #locate attainment tool
#     attainment_criteria = driver.find_element(By.XPATH,"//a[normalize-space()='Attainment Criteria']")
#     attainment_criteria.click()  
#     time.sleep(1)
    
#     #locate add button
#     # add_btn = driver.find_element(By.XPATH,"//a[@class='nxgn_primary_button button_bg_primary']")
#     # add_btn.click()
#     # time.sleep(1)
    
#     # # locate branch dropdown
#     # branch = driver.find_element(By.XPATH,"(//div[@class='nice-select primary_select form-control'])[1]")
#     # branch.click()
#     # time.sleep(3)
    
#     # branch_options = branch.find_element(By.XPATH,"//li[.='AI Timetable Branch']")
#     # branch_options.click()
    
#     # time.sleep(4)
    
#     # # locate department dropdown
#     # department = driver.find_element(By.XPATH,"(//div[@class='nice-select primary_select form-control'])[2]")
#     # department.click()
#     # time.sleep(3)
        
#     # department_options = department.find_element(By.XPATH,"//li[.='AI DEPT 1']")
#     # department_options.click()
    
    
#     # #status dropdown
#     # status_dropdown = driver.find_element(By.XPATH,"(//div[@class='nice-select primary_select form-control'])[3]")
#     # status_dropdown.click()
#     # time.sleep(1)
    
#     # status_options = status_dropdown.find_element(By.XPATH,'//li[.="Active"]')
#     # status_options.click()
#     # time.sleep(1)
    
#     # #-------Common threshold score------
#     # score = driver.find_element(By.XPATH,"//input[@id='threshold_percentage']")
#     # score.send_keys("75")
    
#     # #level 1 field
#     # level1 = wait.until(
#     #     EC.visibility_of_element_located(
#     #         (By.XPATH,"//input[@id='level_1_percentage']")
#     #     )
#     # )
#     # level1.send_keys("50")
    
#     # #level 2 field
#     # level2 = wait.until(
#     #         EC.visibility_of_element_located(
#     #             (By.XPATH,"//input[@id='level_2_percentage']")
#     #         )
#     #     )
#     # level2.send_keys("60")
    
#     # #level 3 field
#     # level3 = wait.until(
#     #         EC.visibility_of_element_located(
#     #             (By.XPATH,"//input[@id='level_3_percentage']")
#     #         )
#     #     )
#     # level3.send_keys("70")
    
#     #back btn
#     # back_btn = driver.find_element(By.XPATH,"//a[@class='primary-btn tr-bg']")
#     # back_btn.click()
    
#     #save btn
#     # save_btn = driver.find_element(By.ID,'submitButton')
#     # save_btn.click()
    
#     #locate 3 dots
#     three_dots = driver.find_element(By.XPATH,"(//button[@class='attn-ajax-action_button'])[1]")
#     three_dots.click()
    
#     #locate edit btn
#     # edit = driver.find_element(By.XPATH,'(//a[@class="attn-ajax-action_item_list asign-btn"])[1]')
#     # edit.click()
#     # time.sleep(2)
    
#     # # locate branch dropdown
#     # branch = driver.find_element(By.XPATH,"(//div[contains(@class,'nice-select') "
#     #             "and contains(@class,'primary_select')])[1]")
#     # branch.click()
#     # time.sleep(3)
        
#     # branch_options = branch.find_element(By.XPATH,"//li[.='AI Timetable Branch']")
#     # branch_options.click()
        
#     # time.sleep(4)
        
#     #     # locate department dropdown
#     # department = driver.find_element(By.XPATH,"(//div[contains(@class,'nice-select') "
#     #    "and contains(@class,'primary_select')])[2]")
#     # department.click()
#     # time.sleep(3)
            
#     # department_options = department.find_element(By.XPATH,"//li[.='AI DEPT 1']")
#     # department_options.click()
        
        
#     #     #status dropdown
#     # status_dropdown = driver.find_element(By.XPATH,"(//div[contains(@class,'nice-select') "
#     #                             "and contains(@class,'primary_select')])[3]")
#     # status_dropdown.click()
#     # time.sleep(1)
        
#     # status_options = status_dropdown.find_element(By.XPATH,'//li[.="Active"]')
#     # status_options.click()
#     # time.sleep(1)
        
#     #  #-------Common threshold score------
#     # score = driver.find_element(By.XPATH,"//input[@id='threshold_percentage']")
#     # score.send_keys("75")
        
#     #     #level 1 field
#     # level1 = wait.until(
#     #         EC.visibility_of_element_located(
#     #             (By.XPATH,"//input[@id='level_1_percentage']")
#     #         )
#     #     )
#     # level1.clear()
#     # level1.send_keys("55")
        
#     #     #level 2 field
#     # level2 = wait.until(
#     #             EC.visibility_of_element_located(
#     #                 (By.XPATH,"//input[@id='level_2_percentage']")
#     #             )
#     #         )
#     # level2.clear()
#     # level2.send_keys("66")
        
#     #     #level 3 field
#     # level3 = wait.until(
#     #             EC.visibility_of_element_located(
#     #                 (By.XPATH,"//input[@id='level_3_percentage']")
#     #             )
#     #         )
#     # level3.clear()
#     # level3.send_keys("70")
        
#     #     #back btn
#     #     # back_btn = driver.find_element(By.XPATH,"//a[@class='primary-btn tr-bg']")
#     #     # back_btn.click()
        
#     #     # save btn
#     # save_btn = driver.find_element(By.ID,'submitButton')
#     # save_btn.click()
    
#     # ---------------- DELETE BUTTON ----------------

#     delete_button = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH, '(//a[@class="attn-ajax-action_item_list attn-ajax-delete-button-datatable delete-button-datatable"])[1]')
#         )
#     )

#     delete_button.click()


#     # ---------------- DELETE CONFIRMATION MODAL ----------------

#     modal = wait.until(
#         EC.visibility_of_element_located(
#             (By.XPATH, "//div[@aria-describedby='swal2-html-container']")
#         )
#     )


#     # ---------------- CONFIRM DELETE ----------------

#     confirm_button = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//button[contains(@class,'swal2-confirm')]")
#         )
#     )

#     confirm_button.click()

    
#     # confirm_button = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (By.XPATH, "//button[contains(@class,'swal2-cancel')]")
#     #         )
#     #     )
    
#     # confirm_button.click()
    

#     # time.sleep(2)
    


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


def test_attainment_criteria(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 15)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "AI Timetable Branch"
    department_value = "AI DEPT 1"
    status_value = "Active"

    threshold_value = "75"
    level1_value = "50"
    level2_value = "60"
    level3_value = "70"

    # EDIT DATA
    edit_threshold_value = "80"
    edit_level1_value = "55"
    edit_level2_value = "65"
    edit_level3_value = "75"

    # EDGE CASE DATA
    threshold_zero = "0"
    threshold_max = "100"
    threshold_negative = "-10"
    threshold_decimal = "75.50"
    level1_invalid = "101"
    level2_invalid = "-5"
    level3_invalid = "abc"

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

    attainment.click()

    # ==========================================================
    # ATTAINMENT CRITERIA
    # ==========================================================

    attainment_criteria = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Attainment Criteria']"
            )
        )
    )

    attainment_criteria.click()

    # ==========================================================
    # ADD BUTTON
    # ==========================================================

#     add_btn = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//a[contains(@class,'nxgn_primary_button') "
#                 "and contains(@class,'button_bg_primary')]"
#             )
#         )
#     )

#     add_btn.click()

#     # ==========================================================
#     # BRANCH DROPDOWN
#     # ==========================================================

#     branch = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select')])[1]"
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

#     branch_option.click()

#     # ==========================================================
#     # DEPARTMENT DROPDOWN
#     # ==========================================================

#     department = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select')])[2]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].click();",
#         department
#     )

#     department_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[normalize-space()='{department_value}']"
#             )
#         )
#     )

#     driver.execute_script(
#     "arguments[0].click();",
#     department_option
# )

#     # ==========================================================
#     # STATUS DROPDOWN
#     # ==========================================================

#     status_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select')])[3]"
#             )
#         )
#     )

#     status_dropdown.click()

#     status_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[normalize-space()='{status_value}']"
#             )
#         )
#     )

#     status_option.click()

#     # ==========================================================
#     # COMMON THRESHOLD SCORE
#     # ==========================================================

#     score = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.ID,
#                 "threshold_percentage"
#             )
#         )
#     )

#     score.click()
#     score.clear()
#     score.send_keys(threshold_value)

#     # ==========================================================
#     # LEVEL 1
#     # ==========================================================

#     level1 = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.ID,
#                 "level_1_percentage"
#             )
#         )
#     )

#     level1.click()
#     level1.clear()
#     level1.send_keys(level1_value)

#     # ==========================================================
#     # LEVEL 2
#     # ==========================================================

#     level2 = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.ID,
#                 "level_2_percentage"
#             )
#         )
#     )

#     level2.click()
#     level2.clear()
#     level2.send_keys(level2_value)

#     # ==========================================================
#     # LEVEL 3
#     # ==========================================================

#     level3 = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.ID,
#                 "level_3_percentage"
#             )
#         )
#     )

#     level3.click()
#     level3.clear()
#     level3.send_keys(level3_value)

#     # ==========================================================
#     # SAVE
#     # ==========================================================

#     save_btn = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "submitButton"
#             )
#         )
#     )

#     save_btn.click()

#     # ==========================================================
#     # VERIFY CREATED DATA
#     # ==========================================================

#     wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.XPATH,
#                 f"//*[contains(normalize-space(),'{branch_value}')]"
#             )
#         )
#     )

#     assert branch_value in driver.page_source
#     assert department_value in driver.page_source
#     assert threshold_value in driver.page_source

    # ==========================================================
    # EDGE CASE - THRESHOLD 0
    # ==========================================================

    # add_btn = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//a[contains(@class,'nxgn_primary_button') "
    #             "and contains(@class,'button_bg_primary')]"
    #         )
    #     )
    # )

    # add_btn.click()

    # branch = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[1]"
    #         )
    #     )
    # )

    # branch.click()

    # wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             f"//li[normalize-space()='{branch_value}']"
    #         )
    #     )
    # ).click()

    # department = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[2]"
    #         )
    #     )
    # )

    # department.click()

    # wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             f"//li[normalize-space()='{department_value}']"
    #         )
    #     )
    # ).click()

    # status_dropdown = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[3]"
    #         )
    #     )
    # )

    # status_dropdown.click()

    # wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             f"//li[normalize-space()='{status_value}']"
    #         )
    #     )
    # ).click()

    # score = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.ID,
    #             "threshold_percentage"
    #         )
    #     )
    # )

    # score.clear()
    # score.send_keys(threshold_zero)

    # level1 = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.ID,
    #             "level_1_percentage"
    #         )
    #     )
    # )

    # level1.clear()
    # level1.send_keys("0")

    # level2 = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.ID,
    #             "level_2_percentage"
    #         )
    #     )
    # )

    # level2.clear()
    # level2.send_keys("0")

    # level3 = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.ID,
    #             "level_3_percentage"
    #         )
    #     )
    # )

    # level3.clear()
    # level3.send_keys("0")

    # save_btn = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "submitButton"
    #         )
    #     )
    # )

    # save_btn.click()

    # time.sleep(1)

    # ==========================================================
    # THREE DOTS
    # ==========================================================

    three_dots = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//button[contains(@class,'attn-ajax-action_button')])[1]"
            )
        )
    )

    three_dots.click()

    # ==========================================================
    # EDIT
    # ==========================================================

    edit = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[contains(@class,'attn-ajax-action_item_list') "
                "and contains("
                "translate(normalize-space(),"
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                "'abcdefghijklmnopqrstuvwxyz'),"
                "'edit')])[1]"
            )
        )
    )

    edit.click()

    # ==========================================================
    # EDIT THRESHOLD
    # ==========================================================

    score = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "threshold_percentage"
            )
        )
    )

    score.clear()
    score.send_keys(edit_threshold_value)

    # ==========================================================
    # EDIT LEVEL 1
    # ==========================================================

    level1 = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "level_1_percentage"
            )
        )
    )

    level1.clear()
    level1.send_keys(edit_level1_value)

    # ==========================================================
    # EDIT LEVEL 2
    # ==========================================================

    level2 = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "level_2_percentage"
            )
        )
    )

    level2.clear()
    level2.send_keys(edit_level2_value)

    # ==========================================================
    # EDIT LEVEL 3
    # ==========================================================

    level3 = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "level_3_percentage"
            )
        )
    )

    level3.clear()
    level3.send_keys(edit_level3_value)

    # ==========================================================
    # SAVE EDIT
    # ==========================================================

    save_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "submitButton"
            )
        )
    )

    save_btn.click()

    time.sleep(1)

    # ==========================================================
    # VERIFY EDIT
    # ==========================================================

    assert edit_threshold_value in driver.page_source
    assert edit_level1_value in driver.page_source
    assert edit_level2_value in driver.page_source
    assert edit_level3_value in driver.page_source

    # ==========================================================
    # THREE DOTS FOR DELETE
    # ==========================================================

    # three_dots = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//button[contains(@class,'attn-ajax-action_button')])[1]"
    #         )
    #     )
    # )

    # three_dots.click()

    # # ==========================================================
    # # DELETE
    # # ==========================================================

    # delete_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//a[contains(@class,"
    #             "'attn-ajax-delete-button-datatable') "
    #             "and contains(@class,'delete-button-datatable')])[1]"
    #         )
    #     )
    # )

    # delete_button.click()

    # # ==========================================================
    # # DELETE CONFIRMATION
    # # ==========================================================

    # modal = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//div[@aria-describedby='swal2-html-container']"
    #         )
    #     )
    # )

    # assert modal.is_displayed()

    # # ==========================================================
    # # CONFIRM DELETE
    # # ==========================================================

    # confirm_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//button[contains(@class,'swal2-confirm')]"
    #         )
    #     )
    # )

    # confirm_button.click()

    # # ==========================================================
    # # VERIFY DELETE
    # # ==========================================================

    # wait.until(
    #     EC.invisibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//div[@aria-describedby='swal2-html-container']"
    #         )
    #     )
    # )

    # time.sleep(2)