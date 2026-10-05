# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time


# def test_co_attainment(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 10)

#     # ---------------- Attainment ----------------

#     attainment = driver.find_element(
#         By.XPATH,
#         "//div//span[normalize-space()='Attainment']"
#     )
#     attainment.click()

#     # ---------------- CO Attainment ----------------

#     co_attainment = driver.find_element(
#         By.XPATH,
#         "//a[normalize-space()='CO Attainment']"
#     )
#     co_attainment.click()
#     time.sleep(1)


#     # # ---------------- Branch Dropdown ----------------

#     branch = driver.find_element(
#         By.XPATH,
#         "(//div[@class='nice-select primary_select form-control'])[1]"
#     )
#     branch.click()
#     time.sleep(2)

#     branch_options = wait.until(
#         EC.presence_of_element_located(
#             (
#                 By.XPATH,
#                 "//li[normalize-space()='STU Marol(east) Mumbai 400002']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         branch_options
#     )

#     driver.execute_script(
#         "arguments[0].click();",
#         branch_options
#     )

#     time.sleep(2)

#     # # locate department dropdown
#     department = driver.find_element(By.XPATH,"(//div[@class='nice-select primary_select form-control'])[2]")
#     department.click()
#     time.sleep(3)
            
#     department_options = department.find_element(By.XPATH,"//li[.='IT-26']")
#     department_options.click()
#     time.sleep(2)


#     # --------------------------------------------------
#     # Open Program Dropdown
#     # --------------------------------------------------

#     program_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[@class='nice-select primary_select form-control'])[3]"
#             )
#         )
#     )

#     program_dropdown.click()

#     time.sleep(1)

#     program_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//li[normalize-space()='New-IT']"
#             )
#         )
#     )

#     program_option.click()

#     time.sleep(2)
    
#      # # ---------------- SEMESTER dropdown ----------------

#     semester_dropdown = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     "(//div[@class='nice-select primary_select form-control'])[4]"
#                 )
#             )
#         )
    
#     semester_dropdown.click()
    
#     time.sleep(1)
    
#     semester_option = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     "//li[normalize-space()='Sem-3-IT']"
#                 )
#             )
#         )
    
#     semester_option.click()
#     time.sleep(2)
    


#     # # ---------------- Search ----------------

#     search_btn = wait.until(
#         EC.element_to_be_clickable(
#             (By.ID, "coAttnSearchButton")
#         )
#     )
#     search_btn.click()

#     time.sleep(2)

#     driver.execute_script(
#     "window.scrollTo(0, document.body.scrollHeight);"

# )
#     #eye btn
#     eye_btn = driver.find_element(By.XPATH,"(//a[@class='co-attn-eye-link js-co-attn-detail-link'])[2]")
#     eye_btn.click()
    
#     time.sleep(4)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_co_attainment(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 15)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "STU Marol(east) Mumbai 400002"
    department_value = "IT-26"
    program_value = "New-IT"
    semester_value = "Sem-3-IT"

    # EDGE CASE DATA
    invalid_department = "Invalid-Department"
    invalid_program = "Invalid-Program"
    invalid_semester = "Invalid-Semester"

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
    # CO ATTAINMENT
    # ==========================================================

    co_attainment = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[normalize-space()='CO Attainment']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        co_attainment
    )

    time.sleep(1)

    # ==========================================================
    # BRANCH DROPDOWN
    # ==========================================================

    branch = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        branch
    )

    driver.execute_script(
        "arguments[0].click();",
        branch
    )

    time.sleep(1)

    # ==========================================================
    # BRANCH OPTION
    # ==========================================================

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

    # ==========================================================
    # DEPARTMENT DROPDOWN
    # ==========================================================

    department = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[2]"
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
    # DEPARTMENT OPTION
    # ==========================================================

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

    # ==========================================================
    # PROGRAM DROPDOWN
    # ==========================================================

    program_dropdown = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[3]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        program_dropdown
    )

    driver.execute_script(
        "arguments[0].click();",
        program_dropdown
    )

    time.sleep(1)

    # ==========================================================
    # PROGRAM OPTION
    # ==========================================================

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

    # ==========================================================
    # SEMESTER DROPDOWN
    # ==========================================================

    semester_dropdown = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[4]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester_dropdown
    )

    driver.execute_script(
        "arguments[0].click();",
        semester_dropdown
    )

    time.sleep(1)

    # ==========================================================
    # SEMESTER OPTION
    # ==========================================================

    semester_option = wait.until(
        EC.presence_of_element_located(
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

    driver.execute_script(
        "arguments[0].click();",
        semester_option
    )

    time.sleep(2)

    # ==========================================================
    # VERIFY SELECTED VALUES
    # ==========================================================

    assert branch_value in driver.page_source
    assert department_value in driver.page_source
    assert program_value in driver.page_source
    assert semester_value in driver.page_source

    # ==========================================================
    # SEARCH
    # ==========================================================

    search_btn = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "coAttnSearchButton"
            )
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

    time.sleep(3)

    # ==========================================================
    # VERIFY SEARCH RESULT
    # ==========================================================

    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[contains(@class,'co-attn-eye-link')]"
            )
        )
    )

    # ==========================================================
    # SCROLL TO RESULT
    # ==========================================================

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(1)

    # ==========================================================
    # EYE / VIEW BUTTON
    # ==========================================================

    eye_btn = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//a[contains(@class,"
                "'co-attn-eye-link') "
                "and contains(@class,"
                "'js-co-attn-detail-link')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        eye_btn
    )

    driver.execute_script(
        "arguments[0].click();",
        eye_btn
    )

    time.sleep(4)

    # ==========================================================
    # VERIFY DETAIL PAGE / POPUP
    # ==========================================================

    assert driver.current_url is not None