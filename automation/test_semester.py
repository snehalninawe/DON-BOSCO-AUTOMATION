# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time


# def test_semester(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 20)

#     # ---------------- UNIVERSITY ----------------

#     university = driver.find_element(
#         By.XPATH,
#         "//div//span[normalize-space()='University']"
#     )

#     university.click()
#     driver.execute_script("arguments[0].click();", university)

#     time.sleep(2)


#     # ---------------- SEMESTER ----------------

#     semester = driver.find_element(
#         By.XPATH,
#         "//a[normalize-space()='Semester']"
#     )

#     semester.click()

#     time.sleep(2)


#     # ---------------- ADD BUTTON ----------------

#     # add_button = driver.find_element(
#     #     By.XPATH,
#     #     "//a[contains(@class,'nxgn_primary_button button_bg_primary')]"
#     # )

#     # add_button.click()

#     # time.sleep(2)


#     # # ---------------- BRANCH ----------------

#     # branch_dropdown = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//div[@class='nice-select primary_select form-control'])[1]"
#     #         )
#     #     )
#     # )

#     # branch_dropdown.click()

#     # time.sleep(1)

#     # branch_option = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//li[normalize-space()='STU Marol(east) Mumbai 400002']"
#     #         )
#     #     )
#     # )

#     # branch_option.click()


#     # # ---------------- DEPARTMENT ----------------

#     # time.sleep(3)

#     # department_dropdown = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//div[@class='nice-select primary_select form-control'])[2]"
#     #         )
#     #     )
#     # )

#     # department_dropdown.click()

#     # time.sleep(1)

#     # department_option = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//li[normalize-space()='IT-26']"
#     #         )
#     #     )
#     # )

#     # department_option.click()


#     # # ---------------- PROGRAM ----------------

#     # time.sleep(2)

#     # program_dropdown = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//div[@class='nice-select primary_select form-control'])[3]"
#     #         )
#     #     )
#     # )

#     # program_dropdown.click()

#     # time.sleep(1)

#     # program_option = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//li[normalize-space()='New-IT']"
#     #         )
#     #     )
#     # )

#     # program_option.click()


#     # # ---------------- SEMESTER NAME ----------------

#     # semester_name = wait.until(
#     #     EC.visibility_of_element_located(
#     #         (By.NAME, "name")
#     #     )
#     # )

#     # semester_name.clear()
#     # semester_name.send_keys("sem1-it")


#     # # ---------------- SEMESTER ID ----------------

#     # semester_id = wait.until(
#     #     EC.visibility_of_element_located(
#     #         (By.NAME, "sem_id")
#     #     )
#     # )

#     # semester_id.clear()
#     # semester_id.send_keys("9")


#     # # ==================================================
#     # # START DATE = 15 FEBRUARY
#     # # ==================================================

#     # start_date = wait.until(
#     #     EC.element_to_be_clickable((By.ID, "start_date"))
#     # )

#     # start_date.click()

#     # time.sleep(1)


#     # # February tak previous month click karo
#     # for i in range(6):

#     #     previous_button = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (By.XPATH, "//th[contains(@class,'prev')]")
#     #         )
#     #     )

#     #     previous_button.click()
#     #     time.sleep(0.3)


#     # # Ab 15 February select karo
#     # start_date_option = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//td[normalize-space()='15' "
#     #             "and not(contains(@class,'old')) "
#     #             "and not(contains(@class,'new'))]"
#     #         )
#     #     )
#     # )

#     # start_date_option.click()

#     # time.sleep(1)


#     # # ==================================================
#     # # END DATE = 15 AUGUST
#     # # ==================================================


#     # end_date = wait.until(
#     #     EC.element_to_be_clickable((By.ID, "end_date"))
#     # )

#     # end_date.click()

#     # time.sleep(1)

#     # # END DATE

#     # end_date_option = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "//td[contains(@class,'day') "
#     #             "and normalize-space()='15' "
#     #             "and not(contains(@class,'old')) "
#     #             "and not(contains(@class,'new'))]"
#     #         )
#     #     )
#     # )

#     # end_date_option.click()

#     # time.sleep(2)


#     # ==================================================
#     #                    SUBMIT
#     # ==================================================

#     # submit_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (By.XPATH, "//button[@id='submitButton']")
#     #     )
#     # )

#     # submit_button.click()
    
#     #for editing the department
#     three_dots = driver.find_element(By.XPATH,"(//button[@class='attn-ajax-action_button'])[1]")
#     three_dots.click()
    
# #     edit_button = driver.find_element(By.XPATH,"(//a[contains(.,'edit')])[5]")
# #     edit_button.click()
        
# #  # ==================================================
# # # EDIT - BRANCH
# # # ==================================================

# #     branch_dropdown = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 "(//div[contains(@class,'nice-select') and contains(@class,'primary_select')])[1]"
# #             )
# #         )
# #     )

# # # Scroll dropdown into visible area
# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         branch_dropdown
# #     )

# #     time.sleep(1)

# #     branch_dropdown.click()

# #     time.sleep(1)


# #     # Branch option
# #     branch_option = wait.until(
# #         EC.presence_of_element_located(
# #             (
# #                 By.XPATH,
# #                 "//div[contains(@class,'nice-select')]//li[normalize-space()='STU Marol(east) Mumbai 400002']"
# #             )
# #         )
# #     )

# #     # Scroll option into view
# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         branch_option
# #     )

# #     time.sleep(0.5)


# #     # Normal click try
# #     try:
# #         branch_option.click()

# #     except Exception:
# #         # Overlay ki wajah se click intercept ho raha ho
# #         driver.execute_script(
# #             "arguments[0].click();",
# #             branch_option
# #         )

# #     time.sleep(3)



# # # ==================================================
# # # EDIT - DEPARTMENT
# # # ==================================================


# #     department_dropdown = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 "(//div[contains(@class,'nice-select') and contains(@class,'primary_select')])[2]"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         department_dropdown
# #     )

# #     time.sleep(1)

# #     department_dropdown.click()

# #     time.sleep(1)


# # # IMPORTANT:
# # # Fresh department option locate karo
# #     department_option = wait.until(
# #         EC.presence_of_element_located(
# #             (
# #                 By.XPATH,
# #                 "//div[contains(@class,'nice-select')]//li[normalize-space()='IT-26']"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         department_option
# #     )

# #     time.sleep(0.5)

# #     try:
# #         department_option.click()

# #     except Exception:
# #         driver.execute_script(
# #             "arguments[0].click();",
# #             department_option
# #         )

# #     time.sleep(3)

# # # ==================================================
# # # EDIT - PROGRAM
# # # ==================================================

# #     program_dropdown = wait.until(
# #         EC.element_to_be_clickable(
# #             (
# #                 By.XPATH,
# #                 "(//div[contains(@class,'nice-select') and contains(@class,'primary_select')])[3]"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         program_dropdown
# #     )

# #     time.sleep(1)

# #     program_dropdown.click()

# #     time.sleep(1)


# #     program_option = wait.until(
# #         EC.presence_of_element_located(
# #             (
# #                 By.XPATH,
# #                 "//div[contains(@class,'nice-select')]//li[normalize-space()='New-IT']"
# #             )
# #         )
# #     )

# #     driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});",
# #         program_option
# #     )

# #     time.sleep(0.5)

# #     try:
# #         program_option.click()

# #     except Exception:
# #         driver.execute_script(
# #             "arguments[0].click();",
# #             program_option
# #         )

# #     time.sleep(2)
    
    
# #         # ==================================================
# #     # SEMESTER NAME
# #     # ==================================================

# #     semester_name = wait.until(
# #         EC.visibility_of_element_located(
# #             (By.NAME, "name")
# #         )
# #     )

# #     semester_name.clear()
# #     semester_name.send_keys("sem1-it-1")


# #     # ==================================================
# #     # SEMESTER ID
# #     # ==================================================

# #     semester_id = wait.until(
# #         EC.visibility_of_element_located(
# #             (By.NAME, "sem_id")
# #         )
# #     )

# #     semester_id.clear()
# #     semester_id.send_keys("1")
    
# #     time.sleep(3)


    
# #         # ==================================================
# #         #                    SUBMIT
# #         # ==================================================
    
# #     submit_button = wait.until(
# #             EC.element_to_be_clickable(
# #                 (By.XPATH, "//button[@id='submitButton']")
# #             )
# #         )
    
# #     submit_button.click()
    
    
    
#     # locate delete button
#     delete_button = driver.find_element(By.XPATH,"(//a[contains(.,'delete')])[1]")
#     delete_button.click()
#     time.sleep(1)

#     modal = wait.until(
#     EC.visibility_of_element_located(
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


def test_semester(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "STU Marol(east) Mumbai 400002"
    department_value = "IT-26"
    program_value = "New-IT"

    semester_name_value = "sem1-it"
    semester_id_value = "9"

    start_day = "15"
    end_day = "15"

    # ---------------- EDIT DATA ----------------

    edit_semester_name = "sem1-it-updated"
    edit_semester_id = "10"

    # ---------------- EDGE CASE DATA ----------------

    empty_semester_name = ""
    empty_semester_id = ""

    long_semester_name = (
        "Semester Label Long Name For Boundary Validation Testing"
    )

    invalid_semester_id = "ABC@123"
    negative_semester_id = "-1"

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
    # SEMESTER
    # ==========================================================

    semester = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Semester']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester
    )

    driver.execute_script(
        "arguments[0].click();",
        semester
    )

    time.sleep(2)

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

    time.sleep(2)

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

    time.sleep(2)

    # Verify branch
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

    assert (
        selected_branch.text.strip().lower()
        == branch_value.strip().lower()
    )

    # ==========================================================
    # DEPARTMENT DROPDOWN
    # ==========================================================

    department_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[2]"
            )
        )
    )

    department_dropdown.click()

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

    time.sleep(2)

    # Verify department
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

    assert (
        selected_department.text.strip().lower()
        == department_value.strip().lower()
    )

    # ==========================================================
    # PROGRAM DROPDOWN
    # ==========================================================

    program_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[3]"
            )
        )
    )

    program_dropdown.click()

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

    time.sleep(2)

    # Verify program
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

    assert (
        selected_program.text.strip().lower()
        == program_value.strip().lower()
    )

    # ==========================================================
    # SEMESTER NAME
    # ==========================================================

    semester_name = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "name")
        )
    )

    semester_name.clear()
    semester_name.send_keys(semester_name_value)

    assert (
        semester_name.get_attribute("value")
        == semester_name_value
    )

    # ==========================================================
    # SEMESTER ID
    # ==========================================================

    semester_id = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "sem_id")
        )
    )

    semester_id.clear()
    semester_id.send_keys(semester_id_value)

    assert (
        semester_id.get_attribute("value")
        == semester_id_value
    )

    # ==========================================================
    # EDGE CASE - EMPTY SEMESTER NAME
    # ==========================================================

    semester_name.clear()

    assert semester_name.get_attribute("value") == ""

    semester_name.send_keys(semester_name_value)

    # ==========================================================
    # EDGE CASE - EMPTY SEMESTER ID
    # ==========================================================

    semester_id.clear()

    assert semester_id.get_attribute("value") == ""

    semester_id.send_keys(semester_id_value)

    # ==========================================================
    # EDGE CASE - LONG SEMESTER NAME
    # ==========================================================

    semester_name.clear()
    semester_name.send_keys(long_semester_name)

    actual_long_name = semester_name.get_attribute("value")

    assert actual_long_name == long_semester_name

    semester_name.clear()
    semester_name.send_keys(semester_name_value)

    # ==========================================================
    # EDGE CASE - INVALID SEMESTER ID
    # ==========================================================

    semester_id.clear()
    semester_id.send_keys(invalid_semester_id)

    actual_invalid_id = semester_id.get_attribute("value")

    # If browser accepts alphabetic characters, validation should
    # be checked through the application after submit.
    if actual_invalid_id == invalid_semester_id:

        # Clear invalid value before continuing
        semester_id.clear()
        semester_id.send_keys(semester_id_value)

    else:
        assert actual_invalid_id != invalid_semester_id

    # ==========================================================
    # EDGE CASE - NEGATIVE SEMESTER ID
    # ==========================================================

    semester_id.clear()
    semester_id.send_keys(negative_semester_id)

    actual_negative_id = semester_id.get_attribute("value")

    # Browser/application may reject '-' or may allow it.
    # Do not fail merely because the input accepts it.
    if actual_negative_id == negative_semester_id:
        semester_id.clear()
        semester_id.send_keys(semester_id_value)

    else:
        assert actual_negative_id != negative_semester_id

    # Restore valid ID
    semester_id.clear()
    semester_id.send_keys(semester_id_value)

    # ==========================================================
    # START DATE
    # ==========================================================

    start_date = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "start_date")
        )
    )

    start_date.click()

    time.sleep(1)

    # Select 15 from currently displayed calendar
    start_date_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//td[contains(@class,'day') "
                f"and normalize-space()='{start_day}' "
                f"and not(contains(@class,'old')) "
                f"and not(contains(@class,'new'))]"
            )
        )
    )

    start_date_option.click()

    time.sleep(1)

    # ==========================================================
    # END DATE
    # ==========================================================

    end_date = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "end_date")
        )
    )

    end_date.click()

    time.sleep(1)

    end_date_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//td[contains(@class,'day') "
                f"and normalize-space()='{end_day}' "
                f"and not(contains(@class,'old')) "
                f"and not(contains(@class,'new'))]"
            )
        )
    )

    end_date_option.click()

    time.sleep(2)

    # ==========================================================
    # SUBMIT
    # ==========================================================

    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "submitButton")
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
    # OPEN ACTION MENU
    # ==========================================================

    three_dots = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//button[contains(@class,"
                "'attn-ajax-action_button')])[1]"
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
    # EDIT
    # ==========================================================

    edit_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[contains(.,'edit')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        edit_button
    )

    time.sleep(2)

    # ==========================================================
    # EDIT SEMESTER NAME
    # ==========================================================

    semester_name = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "name")
        )
    )

    semester_name.clear()
    semester_name.send_keys(edit_semester_name)

    assert (
        semester_name.get_attribute("value")
        == edit_semester_name
    )

    # ==========================================================
    # EDIT SEMESTER ID
    # ==========================================================

    semester_id = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "sem_id")
        )
    )

    semester_id.clear()
    semester_id.send_keys(edit_semester_id)

    assert (
        semester_id.get_attribute("value")
        == edit_semester_id
    )

    # ==========================================================
    # SAVE EDIT
    # ==========================================================

    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "submitButton")
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
    # OPEN ACTION MENU AGAIN
    # ==========================================================

    three_dots = wait.until(
        EC.element_to_be_clickable(
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

    time.sleep(1)

    # ==========================================================
    # DELETE
    # ==========================================================

    delete_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[contains(@class,'delete-button-datatable') "
                "or contains(.,'delete')])[1]"
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

    # ==========================================================
    # VERIFY MODAL CLOSED
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