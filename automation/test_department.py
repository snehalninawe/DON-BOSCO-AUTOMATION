# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.common.by import By
# import time



# def test_department(driver):
#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 20)
    
#     #locate university
#     university = driver.find_element(
#     By.XPATH,
#     "//div//span[normalize-space()='University']")
#     university.click()
#     # driver.execute_script("arguments[0].click();", university)
    
#     time.sleep(2)
      
    
#     #locate department
#     department = driver.find_element(By.XPATH,"//a[normalize-space()='Department']")
#     department.click()  
#     time.sleep(2)
    
#     # #locate add button
#     # add_button = driver.find_element(By.XPATH,"//a[contains(@class,'nxgn_primary_button button_bg_primary')]")
#     # add_button.click()
    
    
#     # #locate branch dropdown
#     # branch_dropdown = driver.find_element(By.XPATH,"(//div[@class='nice-select primary_select form-control'])[1]")
#     # branch_dropdown.click()
#     # time.sleep(1)
    
#     # options = branch_dropdown.find_element(By.XPATH, "//li[.='STU Marol(east) Mumbai 400002']")
#     # options.click()
    
#     # #locate dean dropdown
#     # dean_dropdown = driver.find_element(By.XPATH,"(//div[@class='nice-select primary_select form-control'])[2]")
#     # dean_dropdown.click()
#     # time.sleep(1)
        
#     # options = dean_dropdown.find_element(By.XPATH, "//li[.='abc abc (Admin)']")
#     # options.click()
    
#     # #locate department name field
#     # department_name = driver.find_element(By.XPATH,"//input[@placeholder='Name']")
#     # department_name.send_keys("Test Department")
    
#     # #locate department id field
#     # department_id = driver.find_element(By.XPATH,"//input[@placeholder='ID']")
#     # department_id.send_keys("9")
    
#     # #locate submit button
#     # submit_button = driver.find_element(By.XPATH,"//button[@id='submitButton']")
#     # submit_button.click()
    
#     #for editing the department
#     three_dots = driver.find_element(By.XPATH,"(//button[@class='attn-ajax-action_button'])[1]")
#     three_dots.click()
    
#     # edit_button = driver.find_element(By.XPATH,"(//a[contains(.,'edit')])[1]")
#     # edit_button.click()
        
#     # #locate branch dropdown
#     # branch_dropdown = driver.find_element(By.XPATH,"(//div[@class='nice-select primary_select form-control'])[1]")
#     # branch_dropdown.click()
#     # time.sleep(1)
        
#     # options = branch_dropdown.find_element(By.XPATH, "//li[.='STU Marol(east) Mumbai 400002']")
#     # options.click()
        
#     # #locate dean dropdown
#     # dean_dropdown = driver.find_element(By.XPATH,"(//div[@class='nice-select primary_select form-control'])[2]")
#     # dean_dropdown.click()
#     # time.sleep(1)
            
#     # options = dean_dropdown.find_element(By.XPATH, "//li[.='abc abc (Admin)']")
#     # options.click()
        
#     # #locate department name field
#     # department_name = driver.find_element(By.XPATH,"//input[@placeholder='Name']")
#     # department_name.clear()
#     # department_name.send_keys("Test Department1")
        
#     # #locate department id field
#     # department_id = driver.find_element(By.XPATH,"//input[@placeholder='ID']")
#     # department_id.clear()
#     # department_id.send_keys("8")
        
#     # #locate submit button
#     # submit_button = driver.find_element(By.XPATH,"//button[@id='submitButton']")
#     # submit_button.click()
    
    
    
#     #locate delete button
#     delete_button = driver.find_element(By.XPATH,"(//a[contains(.,'delete')])[1]")
#     delete_button.click()
#     time.sleep(1)

#     modal = wait.until  
#     (EC.visibility_of_element_located(
#         (By.XPATH, "//div[@aria-describedby='swal2-html-container']")
#     )
# )
    
#     confirm_button = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//button[@class='swal2-confirm swal2-styled']")
#     )
# )
#     # confirm_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (By.XPATH, "//button[@class='swal2-cancel swal2-styled']")
#     #     )
#     # )
#     confirm_button.click()
    
#     time.sleep(3)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_department(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "STU Marol(east) Mumbai 400002"
    dean_value = "abc abc (Admin)"

    department_name_value = "Test Department"
    department_id_value = "9"

    edit_department_name = "Test Department Updated"
    edit_department_id = "10"

    # ---------------- EDGE CASE DATA ----------------

    empty_department_name = ""
    empty_department_id = ""

    long_department_name = (
        "Test Department Long Name For Validation And Boundary Testing"
    )

    invalid_department_id = "ABC@123"

    # ==========================================================
    # UNIVERSITY
    # ==========================================================

    university = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div//span[normalize-space()='University']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        university
    )

    driver.execute_script(
        "arguments[0].click();",
        university
    )

    time.sleep(1)

    # ==========================================================
    # DEPARTMENT
    # ==========================================================

    department = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Department']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        department
    )

    driver.execute_script(
        "arguments[0].click();",
        department
    )

    time.sleep(1)

    # ==========================================================
    # ADD BUTTON
    # ==========================================================

    add_button = wait.until(
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
        add_button
    )

    driver.execute_script(
        "arguments[0].click();",
        add_button
    )

    time.sleep(1)

    # ==========================================================
    # BRANCH DROPDOWN
    # ==========================================================

    branch_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[1]"
            )
        )
    )

    branch_dropdown.click()

    branch_option = wait.until(
        EC.presence_of_element_located(
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

    time.sleep(1)

    # ==========================================================
    # DEAN DROPDOWN
    # ==========================================================

    dean_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[2]"
            )
        )
    )

    dean_dropdown.click()

    dean_option = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[normalize-space()='{dean_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        dean_option
    )

    driver.execute_script(
        "arguments[0].click();",
        dean_option
    )

    time.sleep(1)

    # ==========================================================
    # DEPARTMENT NAME
    # ==========================================================

    department_name = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Name']"
            )
        )
    )

    department_name.click()
    department_name.clear()
    department_name.send_keys(department_name_value)

    assert (
        department_name.get_attribute("value")
        == department_name_value
    )

    # ==========================================================
    # DEPARTMENT ID
    # ==========================================================

    department_id = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='ID']"
            )
        )
    )

    department_id.click()
    department_id.clear()
    department_id.send_keys(department_id_value)

    assert (
        department_id.get_attribute("value")
        == department_id_value
    )

    # ==========================================================
    # EDGE CASE 1 - EMPTY DEPARTMENT NAME
    # ==========================================================

    department_name.clear()

    assert (
        department_name.get_attribute("value")
        == empty_department_name
    )

    # Restore valid name
    department_name.send_keys(department_name_value)

    # ==========================================================
    # EDGE CASE 2 - EMPTY DEPARTMENT ID
    # ==========================================================

    department_id.clear()

    assert (
        department_id.get_attribute("value")
        == empty_department_id
    )

    # Restore valid ID
    department_id.send_keys(department_id_value)

    # ==========================================================
    # EDGE CASE 3 - LONG DEPARTMENT NAME
    # ==========================================================

    department_name.clear()
    department_name.send_keys(long_department_name)

    entered_long_name = department_name.get_attribute("value")

    assert entered_long_name != ""

    # If max length is applied, browser/application may truncate it.
    # Therefore, do not expect the complete string here.

    # Restore valid name
    department_name.clear()
    department_name.send_keys(department_name_value)

    # ==========================================================
    # EDGE CASE 4 - INVALID DEPARTMENT ID
    # ==========================================================

    department_id.clear()
    department_id.send_keys(invalid_department_id)

    invalid_id_entered = department_id.get_attribute("value")

    # Invalid characters should NOT be accepted.
    assert invalid_id_entered != invalid_department_id

    # Restore valid ID
    department_id.clear()
    department_id.send_keys(department_id_value)

    assert (
        department_id.get_attribute("value")
        == department_id_value
    )

    # ==========================================================
    # EDGE CASE 5 - ZERO DEPARTMENT ID
    # ==========================================================

    department_id.clear()
    department_id.send_keys("0")

    zero_id_value = department_id.get_attribute("value")

    assert zero_id_value == "0"

    # Restore valid ID
    department_id.clear()
    department_id.send_keys(department_id_value)

        # ==========================================================
    # EDGE CASE - NEGATIVE DEPARTMENT ID
    # ==========================================================

    department_id.clear()
    department_id.send_keys("-1")

    negative_id_value = department_id.get_attribute("value")

    # Negative sign should not be accepted
    assert negative_id_value == "1"

    # Restore valid ID
    department_id.clear()
    department_id.send_keys(department_id_value)

    assert (
        department_id.get_attribute("value")
        == department_id_value
    )

    # ==========================================================
    # EDGE CASE 7 - SPECIAL CHARACTERS IN DEPARTMENT NAME
    # ==========================================================

    special_department_name = "@@@###$$$"

    department_name.clear()
    department_name.send_keys(special_department_name)

    special_name_value = department_name.get_attribute("value")

    assert special_name_value != ""

    # Restore valid name
    department_name.clear()
    department_name.send_keys(department_name_value)

    # ==========================================================
    # SUBMIT
    # ==========================================================

    submit_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "submitButton"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        submit_button
    )

    driver.execute_script(
        "arguments[0].click();",
        submit_button
    )

    time.sleep(3)

    # ==========================================================
    # OPEN THREE DOTS
    # ==========================================================

    # three_dots = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//button[contains(@class,'attn-ajax-action_button')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     three_dots
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     three_dots
    # )

    # time.sleep(1)

    # # ==========================================================
    # # EDIT
    # # ==========================================================

    # edit_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//a[contains(.,'edit')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     edit_button
    # )

    # time.sleep(2)

    # # ==========================================================
    # # EDIT DEPARTMENT NAME
    # # ==========================================================

    # department_name = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Name']"
    #         )
    #     )
    # )

    # department_name.clear()
    # department_name.send_keys(edit_department_name)

    # assert (
    #     department_name.get_attribute("value")
    #     == edit_department_name
    # )

    # # ==========================================================
    # # EDIT DEPARTMENT ID
    # # ==========================================================

    # department_id = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='ID']"
    #         )
    #     )
    # )

    # department_id.clear()
    # department_id.send_keys(edit_department_id)

    # assert (
    #     department_id.get_attribute("value")
    #     == edit_department_id
    # )

    # # ==========================================================
    # # SAVE EDIT
    # # ==========================================================

    # submit_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "submitButton"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     submit_button
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     submit_button
    # )

    # time.sleep(3)

    # # ==========================================================
    # # OPEN ACTION MENU AGAIN
    # # ==========================================================

    # three_dots = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//button[contains(@class,'attn-ajax-action_button')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     three_dots
    # )

    # time.sleep(1)

    # # ==========================================================
    # # DELETE
    # # ==========================================================

    # delete_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//a[contains(@class,'delete-button-datatable') "
    #             "or contains(.,'delete')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     delete_button
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     delete_button
    # )

    # # ==========================================================
    # # DELETE CONFIRMATION MODAL
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

    # driver.execute_script(
    #     "arguments[0].click();",
    #     confirm_button
    # )

    # # ==========================================================
    # # VERIFY DELETE MODAL CLOSED
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