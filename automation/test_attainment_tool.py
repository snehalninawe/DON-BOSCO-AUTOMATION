# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time

# def test_attainment_tool(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 15)

#     # ---------------- Attainment ----------------

#     attainment = driver.find_element(
#         By.XPATH,
#         "//div//span[normalize-space()='Attainment']"
#     )
#     attainment.click()
    
#     #locate attainment tool
#     attainment_tool = driver.find_element(By.XPATH,"//a[normalize-space()='Attainment Tool']")
#     attainment_tool.click()  
#     time.sleep(1)
    
#     #locate add button
#     add_btn = driver.find_element(By.XPATH,"//a[@class='nxgn_primary_button button_bg_primary']")
#     add_btn.click()
#     time.sleep(1)
    
#     # locate attainment tool name field
#     name = driver.find_element(By.NAME,'name')
#     name.send_keys('assignment')
    
#     #scheme dropdown
#     scheme_dropdown = driver.find_element(By.XPATH,"//div[@class='nice-select primary_select form-control']")
#     scheme_dropdown.click()
#     time.sleep(1)
    
#     scheme_options = scheme_dropdown.find_element(By.XPATH,'//li[.="NEP"]')
#     scheme_options.click()
#     time.sleep(1)
    
#     #YES/NO checkbox
#     yes_checkbox=wait.until(
#         EC.visibility_of_element_located(
#             (By.XPATH,"(//input[@type='radio'])[2]")
#         )
#     )
#     yes_checkbox.click()
    
#     # no_checkbox=wait.until(
#     #         EC.visibility_of_element_located(
#     #             (By.XPATH,"(//input[@type='radio'])[1]")
#     #         )
#     #     )
#     # no_checkbox.click()
    
#     # ---------------child tool add--------------
#     child_tool = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH,"//input[@name='child_name[]']")
#         )
#     )
#     child_tool.send_keys("child1")
    
#     #save btn
#     save_btn = driver.find_element(By.ID,'submitButton')
#     save_btn.click()
    
#     #locate 3 dots
#     # three_dots = driver.find_element(By.XPATH,"(//button[@class='attn-ajax-action_button'])[1]")
#     # three_dots.click()
    
#     #locate edit btn
#     # edit = driver.find_element(By.XPATH,"(//a[@class='attn-ajax-action_item_list asign-btn'])[1]")
#     # edit.click()
#     # time.sleep(2)
    
#     #locate attainment tool name field
#     # name = driver.find_element(By.NAME,'name')
#     # name.clear()
#     # name.send_keys('assignment-1')
    
#     # #scheme dropdown
#     # scheme_dropdown = driver.find_element(By.XPATH,"(//div[contains(@class,'nice-select') and contains(@class,'primary_select')])[1]")
#     # scheme_dropdown.click()
#     # time.sleep(1)
    
#     # scheme_options = scheme_dropdown.find_element(By.XPATH,'//div[contains(@class,"nice-select")]//li[.="NEP"]')
#     # scheme_options.click()
#     # time.sleep(1)
    
#     # # #save btn
#     # save_btn = driver.find_element(By.ID,'submitButton')
#     # save_btn.click()
    
#     # ---------------- DELETE BUTTON ----------------

#     # delete_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (By.XPATH, "(//a[contains(.,'delete')])[1]")
#     #     )
#     # )

#     # delete_button.click()


#     # ---------------- DELETE CONFIRMATION MODAL ----------------

#     # modal = wait.until(
#     #     EC.visibility_of_element_located(
#     #         (By.XPATH, "//div[@aria-describedby='swal2-html-container']")
#     #     )
#     # )


#     # ---------------- CONFIRM DELETE ----------------

#     # confirm_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (By.XPATH, "//button[contains(@class,'swal2-confirm')]")
#     #     )
#     # )

#     # confirm_button.click()

    
#     # confirm_button = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (By.XPATH, "//button[contains(@class,'swal2-cancel')]")
#     #         )
#     #     )
    
#     # confirm_button.click()
    

#     time.sleep(2)
    


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_attainment_tool(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 15)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    attainment_tool_name = "assignment-1"
    scheme_value = "NEP"
    child_tool_name = "child1"

    # EDIT DATA
    edit_tool_name = "assignment-updated"
    edit_child_name = "child1-updated"

    # EDGE CASE DATA
    blank_name = ""
    spaces_name = "     "
    special_name = "Assignment@#$%"
    numeric_name = "12345"
    long_name = "Assignment-" + ("A" * 100)

    # ==========================================================
    # ATTAINMENT
    # ==========================================================

    attainment = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div//span[normalize-space()='Attainment']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        attainment
    )

    # ==========================================================
    # ATTAINMENT TOOL
    # ==========================================================

    attainment_tool = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[normalize-space()='Attainment Tool']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        attainment_tool
    )

    time.sleep(1)

    # ==========================================================
    # ADD BUTTON
    # ==========================================================

    # add_btn = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//a[contains(@class,'nxgn_primary_button') "
    #             "and contains(@class,'button_bg_primary')]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     add_btn
    # )

    # time.sleep(1)

    # # ==========================================================
    # # ATTAINMENT TOOL NAME
    # # ==========================================================

    # name = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.NAME,
    #             "name"
    #         )
    #     )
    # )

    # name.click()
    # name.clear()
    # name.send_keys(attainment_tool_name)

    # # ==========================================================
    # # SCHEME DROPDOWN
    # # ==========================================================

    # scheme_dropdown = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     scheme_dropdown
    # )

    # time.sleep(1)

    # # ==========================================================
    # # SCHEME OPTION
    # # ==========================================================

    # scheme_option = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//li[normalize-space()='{scheme_value}']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     scheme_option
    # )

    # time.sleep(1)

    # # ==========================================================
    # # YES RADIO BUTTON
    # # ==========================================================

    # yes_checkbox = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//input[@type='radio'])[2]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     yes_checkbox
    # )

    # # Verify YES selected
    # assert yes_checkbox.is_selected(), (
    #     "YES radio button was not selected."
    # )

    # # ==========================================================
    # # CHILD TOOL
    # # ==========================================================

    # child_tool = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@name='child_name[]']"
    #         )
    #     )
    # )

    # child_tool.click()
    # child_tool.clear()
    # child_tool.send_keys(child_tool_name)

    # # ==========================================================
    # # SAVE
    # # ==========================================================

    # save_btn = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "submitButton"
    #         )
    #     )
    # )

    # save_btn.click()

    # time.sleep(2)

    # # ==========================================================
    # # VERIFY CREATED TOOL
    # # ==========================================================

    # wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//*[contains(normalize-space(),"
    #             f"'{attainment_tool_name}')]"
    #         )
    #     )
    # )

    # assert attainment_tool_name in driver.page_source
    # assert child_tool_name in driver.page_source
    # assert scheme_value in driver.page_source

    # ==========================================================
    # THREE DOTS
    # ==========================================================

    # three_dots = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//button[contains(@class,"
    #             "'attn-ajax-action_button')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     three_dots
    # )

    # # ==========================================================
    # # EDIT
    # # ==========================================================

    # edit = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//a[contains(@class,"
    #             "'attn-ajax-action_item_list') "
    #             "and contains("
    #             "translate(normalize-space(),"
    #             "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
    #             "'abcdefghijklmnopqrstuvwxyz'),"
    #             "'edit')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     edit
    # )

    # time.sleep(1)

    # # ==========================================================
    # # EDIT TOOL NAME
    # # ==========================================================

    # name = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.NAME,
    #             "name"
    #         )
    #     )
    # )

    # name.click()
    # name.clear()
    # name.send_keys(edit_tool_name)

    # # ==========================================================
    # # EDIT SCHEME
    # # ==========================================================

    # scheme_dropdown = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     scheme_dropdown
    # )

    # time.sleep(1)

    # scheme_option = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//li[normalize-space()='{scheme_value}']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     scheme_option
    # )

    # # ==========================================================
    # # EDIT CHILD TOOL
    # # ==========================================================

    # child_tool = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@name='child_name[]']"
    #         )
    #     )
    # )

    # child_tool.click()
    # child_tool.clear()
    # child_tool.send_keys(edit_child_name)

    # # ==========================================================
    # # SAVE EDIT
    # # ==========================================================

    # save_btn = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "submitButton"
    #         )
    #     )
    # )

    # save_btn.click()

    # time.sleep(2)

    # # ==========================================================
    # # VERIFY EDIT
    # # ==========================================================

    # wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//*[contains(normalize-space(),"
    #             f"'{edit_tool_name}')]"
    #         )
    #     )
    # )

    # assert edit_tool_name in driver.page_source
    # assert edit_child_name in driver.page_source

    # ==========================================================
    # THREE DOTS FOR DELETE
    # ==========================================================

    three_dots = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//button[contains(@class,"
                "'attn-ajax-action_button')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        three_dots
    )

    # ==========================================================
    # DELETE BUTTON
    # ==========================================================

    delete_button = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//a[contains("
                "translate(normalize-space(),"
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                "'abcdefghijklmnopqrstuvwxyz'),"
                "'delete')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        delete_button
    )

    # ==========================================================
    # DELETE CONFIRMATION MODAL
    # ==========================================================

    modal = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[@aria-describedby='swal2-html-container']"
            )
        )
    )

    assert modal.is_displayed(), (
        "Delete confirmation modal was not displayed."
    )

    # ==========================================================
    # CONFIRM DELETE
    # ==========================================================

    confirm_button = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[contains(@class,'swal2-confirm')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        confirm_button
    )

    # ==========================================================
    # VERIFY DELETE
    # ==========================================================

    wait.until(
        EC.invisibility_of_element_located(
            (
                By.XPATH,
                "//div[@aria-describedby='swal2-html-container']"
            )
        )
    )

    time.sleep(2)

    assert edit_tool_name not in driver.page_source