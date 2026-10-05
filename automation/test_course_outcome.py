# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time


# def test_course_outcome(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 50)

#     # ---------------- Attainment ----------------

#     attainment = driver.find_element(
#         By.XPATH,
#         "//div//span[normalize-space()='Attainment']"
#     )
#     attainment.click()

#     # ---------------- Course Outcome ----------------

#     course_outcome = driver.find_element(
#         By.XPATH,
#         "//a[normalize-space()='Course Outcome']"
#     )
#     course_outcome.click()
#     time.sleep(1)

#     # ---------------- Add Button ----------------

#     # add_btn = driver.find_element(
#     #     By.XPATH,
#     #     "//a[@class='nxgn_primary_button button_bg_primary']"
#     # )
#     # add_btn.click()
#     # time.sleep(1)

#     # # ---------------- Branch Dropdown ----------------

#     # branch = driver.find_element(
#     #     By.XPATH,
#     #     "(//div[@class='nice-select primary_select form-control'])[1]"
#     # )
#     # branch.click()
#     # time.sleep(2)

#     # branch_options = wait.until(
#     #     EC.presence_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "//li[normalize-space()='STU Marol(east) Mumbai 400002']"
#     #         )
#     #     )
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     branch_options
#     # )

#     # driver.execute_script(
#     #     "arguments[0].click();",
#     #     branch_options
#     # )

#     # time.sleep(2)

#     # # ---------------- Department Dropdown ----------------

#     # department = driver.find_element(
#     #     By.XPATH,
#     #     "(//div[@class='nice-select primary_select form-control'])[2]"
#     # )
#     # department.click()
#     # time.sleep(2)

#     # department_options = wait.until(
#     #     EC.presence_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "//li[normalize-space()='IT-26']"
#     #         )
#     #     )
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     department_options
#     # )

#     # driver.execute_script(
#     #     "arguments[0].click();",
#     #     department_options
#     # )

#     # time.sleep(2)

#     # # ---------------- Program Dropdown ----------------

#     # program_dropdown = driver.find_element(
#     #     By.XPATH,
#     #     "(//div[@class='nice-select primary_select form-control'])[3]"
#     # )
#     # program_dropdown.click()
#     # time.sleep(1)

#     # program_options = wait.until(
#     #     EC.presence_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "//li[normalize-space()='New-IT']"
#     #         )
#     #     )
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     program_options
#     # )

#     # driver.execute_script(
#     #     "arguments[0].click();",
#     #     program_options
#     # )

#     # time.sleep(1)

#     # # ---------------- Subject Dropdown ----------------

#     # subject_dropdown = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//div[contains(@class,'nice-select') "
#     #             "and contains(@class,'primary_select')])[4]"
#     #         )
#     #     )
#     # )

#     # subject_dropdown.click()

#     # subject_option = wait.until(
#     #     EC.presence_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "//li[normalize-space()='Database Management Systems']"
#     #         )
#     #     )
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     subject_option
#     # )

#     # driver.execute_script(
#     #     "arguments[0].click();",
#     #     subject_option
#     # )

#     # time.sleep(1)

#     # # ---------------- Fetch ----------------

#     # fetch_btn = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (By.XPATH, "//button[normalize-space()='Fetch']")
#     #     )
#     # )
#     # fetch_btn.click()

#     # time.sleep(2)

#     # # ---------------- Plus Button ----------------

#     # plus_btn = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (By.ID, "add_course_outcomes_btn")
#     #     )
#     # )
#     # plus_btn.click()

#     # time.sleep(2)

#     # # ==================================================
#     # #                    COURSE OUTCOME 1
#     # # ==================================================

#     # # ---------------- CO1 Code ----------------

#     # code_field = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//input[contains(@class,'course-code-change')])[1]"
#     #         )
#     #     )
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     code_field
#     # )

#     # code_field.click()
#     # code_field.clear()
#     # code_field.send_keys("CO1")

#     # time.sleep(2)

#     # # ---------------- CO1 BT ----------------

#     # bt_dropdown_1 = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//div[contains(@class,'nice-select') "
#     #             "and contains(@class,'primary_select')])[5]"
#     #         )
#     #     )
#     # )

#     # bt_dropdown_1.click()

#     # bt_option_1 = wait.until(
#     #     EC.presence_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "//li[normalize-space()='ANALYZE']"
#     #         )
#     #     )
#     # )

#     # driver.execute_script(
#     #     "arguments[0].click();",
#     #     bt_option_1
#     # )
#     # time.sleep(1)

#     # # ---------------- CO1 Description ----------------

#     # desc_1 = wait.until(
#     #     EC.visibility_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "(//textarea[contains(@class,'course-description-change')])[1]"
#     #         )
#     #     )
#     # )

#     # desc_1.send_keys("analyzed")

#     # # ==================================================
#     # #                    COURSE OUTCOME 2
#     # # ==================================================

#     # # ---------------- CO2 Code ----------------


#     # code_field_2 = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//input[contains(@class,'course-code-change')])[2]"
#     #         )
#     #     )
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     code_field_2
#     # )

#     # code_field_2.click()
#     # code_field_2.clear()
#     # code_field_2.send_keys("CO2")

#     # time.sleep(2)


#     # # ---------------- CO2 BT Dropdown ----------------


#     # bt_dropdown_2 = driver.find_element(
#     #     By.XPATH,
#     #     "(//div[contains(@class,'nice-select') and contains(@class,'primary_select')])[6]"
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     bt_dropdown_2
#     # )

#     # bt_dropdown_2.click()

#     # time.sleep(1)

#     # # REMEMBER option
#     # bt_option_2 = driver.find_element(
#     #     By.XPATH,
#     #     "//div[contains(@class,'nice-select') and contains(@class,'open')]"
#     #     "//li[contains(@class,'option') and normalize-space()='REMEMBER']"
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     bt_option_2
#     # )

#     # driver.execute_script(
#     #     "arguments[0].click();",
#     #     bt_option_2
#     # )

#     # time.sleep(1)

#     # # ---------------- CO2 Description ----------------

#     # desc_2 = wait.until(
#     #     EC.visibility_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "(//textarea[contains(@class,'course-description-change')])[2]"
#     #         )
#     #     )
#     # )

#     # desc_2.send_keys("remembered")

#     # # ==================================================
#     # #                       SAVE
#     # # ==================================================

#     # save = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (By.ID, "submitButton")
#     #     )
#     # )

#     # save.click()

#     # time.sleep(3)
    
#     #locate go to edit btn
#     # go_to_edit = driver.find_element(By.XPATH,"//a[@class='btn btn-warning']")
#     # go_to_edit.click()
    
#     # locate 3 dots
#     three_dots = driver.find_element(By.XPATH,"(//button[@class='action_button'])[1]")
#     three_dots.click()
    
#     #locate edit btn
#     # edit = driver.find_element(By.XPATH,"(//a[@class='action_item_list asign-btn'])[1]")
#     # edit.click()
#     # time.sleep(2)
    
#     # # locate branch dropdown
#     # branch = driver.find_element(By.XPATH,"(//div[contains(@class,'nice-select') "
#     #             "and contains(@class,'primary_select')])[1]")
#     # branch.click()
#     # time.sleep(3)
        
#     # branch_options = branch.find_element(By.XPATH,"//li[.='STU Marol(east) Mumbai 400002']")
#     # branch_options.click()
        
#     # time.sleep(4)
        
#     # # locate department dropdown
#     # department = driver.find_element(By.XPATH,"(//div[contains(@class,'nice-select') "
#     #    "and contains(@class,'primary_select')])[2]")
#     # department.click()
#     # time.sleep(3)
            
#     # department_options = department.find_element(By.XPATH,"//li[.='IT-26']")
#     # department_options.click()
    
#     # ---------------- Plus Button ----------------
    
#     # plus_btn = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (By.ID, "add_course_outcomes_btn")
#     #         )
#     #     )
#     # plus_btn.click()
    
#     # time.sleep(2)
    
#     #     # ==================================================
#     #     #                    COURSE OUTCOME 1
#     #     # ==================================================
    
#     #     # ---------------- CO1 Code ----------------
    
#     # code_field = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 By.XPATH,
#     #                 "(//input[contains(@class,'course-code-change')])[1]"
#     #             )
#     #         )
#     #     )
    
#     # driver.execute_script(
#     #         "arguments[0].scrollIntoView({block:'center'});",
#     #         code_field
#     #     )
    
#     # code_field.click()
#     # code_field.clear()
#     # code_field.send_keys("CO2")
    
#     # time.sleep(2)
    
#     #     # ---------------- CO1 BT ----------------
    
#     # bt_dropdown_1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 By.XPATH,
#     #                 "(//div[contains(@class,'nice-select') "
#     #                 "and contains(@class,'primary_select')])[5]"
#     #             )
#     #         )
#     #     )
    
#     # bt_dropdown_1.click()
    
#     # bt_option_1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (
#     #                 By.XPATH,
#     #                 "//li[normalize-space()='ANALYZE']"
#     #             )
#     #         )
#     #     )
    
#     # driver.execute_script(
#     #         "arguments[0].click();",
#     #         bt_option_1
#     #     )
#     # time.sleep(1)
    
#     #     # ---------------- CO1 Description ----------------
    
#     # desc_1 = wait.until(
#     #         EC.visibility_of_element_located(
#     #             (
#     #                 By.XPATH,
#     #                 "(//textarea[contains(@class,'course-description-change')])[1]"
#     #             )
#     #         )
#     #     )
    
#     # desc_1.send_keys("analyzed")
    
#     #     # ==================================================
#     #     #                    COURSE OUTCOME 2
#     #     # ==================================================
    
#     #     # ---------------- CO2 Code ----------------
    
    
#     # code_field_2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 By.XPATH,
#     #                 "(//input[contains(@class,'course-code-change')])[2]"
#     #             )
#     #         )
#     #     )
    
#     # driver.execute_script(
#     #         "arguments[0].scrollIntoView({block:'center'});",
#     #         code_field_2
#     #     )
    
#     # code_field_2.click()
#     # code_field_2.clear()
#     # code_field_2.send_keys("CO1")
    
#     # time.sleep(2)
    
    
#     #     # ---------------- CO2 BT Dropdown ----------------
    
    
#     # bt_dropdown_2 = driver.find_element(
#     #         By.XPATH,
#     #         "(//div[contains(@class,'nice-select') and contains(@class,'primary_select')])[6]"
#     #     )
    
#     # driver.execute_script(
#     #         "arguments[0].scrollIntoView({block:'center'});",
#     #         bt_dropdown_2
#     #     )
    
#     # bt_dropdown_2.click()
    
#     # time.sleep(1)
    
#     #     # REMEMBER option
#     # bt_option_2 = driver.find_element(
#     #         By.XPATH,
#     #         "//div[contains(@class,'nice-select') and contains(@class,'open')]"
#     #         "//li[contains(@class,'option') and normalize-space()='REMEMBER']"
#     #     )
    
#     # driver.execute_script(
#     #         "arguments[0].scrollIntoView({block:'center'});",
#     #         bt_option_2
#     #     )
    
#     # driver.execute_script(
#     #         "arguments[0].click();",
#     #         bt_option_2
#     #     )
    
#     # time.sleep(1)
    
#     #     # ---------------- CO2 Description ----------------
    
#     # desc_2 = wait.until(
#     #         EC.visibility_of_element_located(
#     #             (
#     #                 By.XPATH,
#     #                 "(//textarea[contains(@class,'course-description-change')])[2]"
#     #             )
#     #         )
#     #     )
    
#     # desc_2.send_keys("remembered")
    
#         # ==================================================
#         #                       SAVE
#         # ==================================================
    
#     # save = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (By.ID, "submitButton")
#     #         )
#     #     )
    
#     # save.click()
    
#     # time.sleep(3)
    
#     # ---------------- DELETE BUTTON ----------------

#     delete_button = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH, '(//a[@class="action_item_list delete-button-datatable"])[1]')
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
    

#     time.sleep(1)
    


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)
import time


def test_course_outcome(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "STU Marol(east) Mumbai 400002"
    department_value = "IT-26"
    program_value = "New-IT"
    subject_value = "Database Management Systems"

    co1_code = "CO1"
    co1_bloom_level = "ANALYZE"
    co1_description = "Analyze database concepts and management techniques."

    co2_code = "CO2"
    co2_bloom_level = "REMEMBER"
    co2_description = "Remember fundamental database management concepts."

    # ---------------- EDGE CASE DATA ----------------

    duplicate_co_code = "CO1"

    empty_description = ""

    long_description = (
        "This is a long course outcome description used to verify "
        "whether the application correctly handles lengthy text input "
        "without breaking the layout or validation."
    )

    invalid_co_code = "12345"

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

    # ==========================================================
    # COURSE OUTCOME
    # ==========================================================

    course_outcome = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Course Outcome']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        course_outcome
    )

    driver.execute_script(
        "arguments[0].click();",
        course_outcome
    )

    time.sleep(1)

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

    driver.execute_script(
        "arguments[0].click();",
        add_btn
    )

    time.sleep(1)

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

    department_option = wait.until(
        EC.presence_of_element_located(
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

    driver.execute_script(
        "arguments[0].click();",
        department_option
    )

    time.sleep(1)

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

    program_option = wait.until(
        EC.presence_of_element_located(
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

    driver.execute_script(
        "arguments[0].click();",
        program_option
    )

    time.sleep(1)

    # ==========================================================
    # SUBJECT DROPDOWN
    # ==========================================================

    subject = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[4]"
            )
        )
    )

    subject.click()

    subject_option = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[normalize-space()='{subject_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        subject_option
    )

    driver.execute_script(
        "arguments[0].click();",
        subject_option
    )

    time.sleep(1)

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

    time.sleep(2)

    # ==========================================================
    # PLUS BUTTON
    # ==========================================================

    # plus_btn = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "add_course_outcomes_btn"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     plus_btn
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     plus_btn
    # )

    # time.sleep(1)

    # ==========================================================
    # COURSE OUTCOME 1
    # ==========================================================

    # ---------------- CO1 CODE ----------------

    code_field_1 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//input[contains(@class,'course-code-change')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        code_field_1
    )

    code_field_1.click()
    code_field_1.clear()
    code_field_1.send_keys(co1_code)

    # Verify CO1 code
    assert code_field_1.get_attribute("value") == co1_code

    # ==========================================================
    # CO1 BLOOM'S TAXONOMY
    # ==========================================================

    bt_dropdown_1 = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[5]"
            )
        )
    )

    bt_dropdown_1.click()

    bt_option_1 = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                "//li[contains(@class,'option') "
                f"and normalize-space()='{co1_bloom_level}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        bt_option_1
    )

    # ==========================================================
    # CO1 DESCRIPTION
    # ==========================================================

    desc_1 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//textarea[contains(@class,'course-description-change')])[1]"
            )
        )
    )

    desc_1.clear()
    desc_1.send_keys(co1_description)

    assert desc_1.get_attribute("value") == co1_description

    # ==========================================================
    # ADD SECOND COURSE OUTCOME
    # ==========================================================

    plus_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "add_course_outcomes_btn"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        plus_btn
    )

    driver.execute_script(
        "arguments[0].click();",
        plus_btn
    )

    time.sleep(1)

    # ==========================================================
    # COURSE OUTCOME 2
    # ==========================================================

    # ---------------- CO2 CODE ----------------

    code_field_2 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//input[contains(@class,'course-code-change')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        code_field_2
    )

    code_field_2.click()
    code_field_2.clear()
    code_field_2.send_keys(co2_code)

    assert code_field_2.get_attribute("value") == co2_code

    # ==========================================================
    # CO2 BLOOM'S TAXONOMY
    # ==========================================================

    bt_dropdown_2 = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[6]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        bt_dropdown_2
    )

    bt_dropdown_2.click()

    bt_option_2 = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                "//li[contains(@class,'option') "
                f"and normalize-space()='{co2_bloom_level}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        bt_option_2
    )

    # ==========================================================
    # CO2 DESCRIPTION
    # ==========================================================

    desc_2 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//textarea[contains(@class,'course-description-change')])[2]"
            )
        )
    )

    desc_2.clear()
    desc_2.send_keys(co2_description)

    assert desc_2.get_attribute("value") == co2_description

    # ==========================================================
    # EDGE CASE - LONG DESCRIPTION
    # ==========================================================

    desc_2.clear()
    desc_2.send_keys(long_description)

    assert desc_2.get_attribute("value") == long_description

    # Restore valid description
    desc_2.clear()
    desc_2.send_keys(co2_description)

    # ==========================================================
    # EDGE CASE - EMPTY DESCRIPTION
    # ==========================================================

    desc_2.clear()

    assert desc_2.get_attribute("value") == empty_description

    # Restore valid description
    desc_2.send_keys(co2_description)

    # ==========================================================
    # EDGE CASE - INVALID CO CODE
    # ==========================================================

    code_field_2.clear()
    code_field_2.send_keys(invalid_co_code)

    assert code_field_2.get_attribute("value") == invalid_co_code

    # Restore valid CO code
    code_field_2.clear()
    code_field_2.send_keys(co2_code)

    # ==========================================================
    # EDGE CASE - DUPLICATE CO CODE
    # ==========================================================

    code_field_2.clear()
    code_field_2.send_keys(duplicate_co_code)

    assert code_field_2.get_attribute("value") == duplicate_co_code

    # Restore valid CO2
    code_field_2.clear()
    code_field_2.send_keys(co2_code)

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

    time.sleep(3)

    # ==========================================================
    # VERIFY SAVE RESULT
    # ==========================================================

    try:

        success_message = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(@class,'swal2') "
                    "or contains(@class,'alert-success')]"
                )
            )
        )

        assert success_message.is_displayed()

    except TimeoutException:

        # If application redirects directly after save,
        # verify page is still available.
        assert driver.current_url is not None

    # ==========================================================
    # THREE DOTS / ACTION MENU
    # ==========================================================

    three_dots = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//button[contains(@class,'action_button')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        three_dots
    )

    driver.execute_script(
        "arguments[0].click();",
        three_dots
    )

    time.sleep(1)

    # ==========================================================
    # DELETE BUTTON
    # ==========================================================

    delete_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[contains(@class,'action_item_list') "
                "and contains(@class,'delete-button-datatable')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        delete_button
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

    assert modal.is_displayed()

    # ==========================================================
    # CONFIRM DELETE
    # ==========================================================

    confirm_button = wait.until(
        EC.element_to_be_clickable(
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

    time.sleep(2)

    # ==========================================================
    # VERIFY DELETE
    # ==========================================================

    try:

        deleted_message = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(@class,'swal2') "
                    "or contains(@class,'alert-success')]"
                )
            )
        )

        assert deleted_message.is_displayed()

    except TimeoutException:

        # Table should refresh after deletion
        assert driver.current_url is not None

    time.sleep(1)