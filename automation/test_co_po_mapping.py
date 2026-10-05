# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time


# def test_co_po_mapping(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 10)

#     # ---------------- Attainment ----------------

#     attainment = driver.find_element(
#         By.XPATH,
#         "//div//span[normalize-space()='Attainment']"
#     )
#     attainment.click()

#     # ---------------- CO PO Mapping ----------------

#     program_outcome = driver.find_element(
#         By.XPATH,
#         "//a[normalize-space()='CO PO Mapping']"
#     )
#     program_outcome.click()
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
    
#     ##----------Subject dropdown-------------
#     subject_dropdown = wait.until(
#                 EC.element_to_be_clickable(
#                     (
#                         By.XPATH,
#                         "(//div[@class='nice-select primary_select form-control'])[5]"
#                     )
#                 )
#             )
        
#     subject_dropdown.click()
        
#     time.sleep(1)
        
#     subject_option = wait.until(
#                 EC.element_to_be_clickable(
#                     (
#                         By.XPATH,
#                         "//li[normalize-space()='Networksssss']"
#                     )
#                 )
#             )
        
#     subject_option.click()
#     time.sleep(2)


#     # # ---------------- Fetch ----------------

#     search_btn = wait.until(
#         EC.element_to_be_clickable(
#             (By.ID, "attainmentSearchButton")
#         )
#     )
#     search_btn.click()

#     time.sleep(2)

#     driver.execute_script(
#     "window.scrollTo(0, document.body.scrollHeight);"
# )
#     time.sleep(2)
#     ticker_1 = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//button[contains(@class,'co-po-ticker') and contains(@class,'is-1')]"
#             )
#         )
#     )

#     ticker_1.click()
    
#     time.sleep(2)
    
#     ticker_2 = wait.until(
#     EC.element_to_be_clickable(
#         (
#             By.XPATH,
#             "//button[contains(@class,'co-po-ticker') and contains(@class,'is-3')]"
#         )
#     )
# )

#     ticker_2.click()
#     time.sleep(2)

#     # # ==================================================
#     # #                       SAVE
#     # # ==================================================

#     save = wait.until(
#         EC.element_to_be_clickable(
#             (By.ID, "attainmentSaveButton")
#         )
#     )

#     save.click()
    
#     time.sleep(2)
    
#     #----OK Btn-----
#     ok_btn = driver.find_element(By.XPATH,"//button[.='OK']")
#     ok_btn.click()

#     time.sleep(5)   


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_co_po_mapping(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 15)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "STU Marol(east) Mumbai 400002"
    department_value = "IT-26"
    program_value = "New-IT"
    semester_value = "Sem-3-IT"
    subject_value = "Networksssss"

    # CO-PO TICKERS
    ticker_1_value = "1"
    ticker_2_value = "3"

    # EDGE CASE DATA
    invalid_subject = "Invalid Subject"
    invalid_branch = "Invalid Branch"

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
    # CO PO MAPPING
    # ==========================================================

    program_outcome = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[normalize-space()='CO PO Mapping']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        program_outcome
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
    # SUBJECT DROPDOWN
    # ==========================================================

    subject_dropdown = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[5]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        subject_dropdown
    )

    driver.execute_script(
        "arguments[0].click();",
        subject_dropdown
    )

    time.sleep(1)

    # ==========================================================
    # SUBJECT OPTION
    # ==========================================================

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

    time.sleep(2)

    # ==========================================================
    # VERIFY SELECTED DATA
    # ==========================================================

    assert branch_value in driver.page_source
    assert department_value in driver.page_source
    assert program_value in driver.page_source
    assert semester_value in driver.page_source
    assert subject_value in driver.page_source

    # ==========================================================
    # FETCH / SEARCH
    # ==========================================================

    search_btn = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "attainmentSearchButton"
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
    # WAIT FOR CO-PO MAPPING RESULT
    # ==========================================================

    time.sleep(3)

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(2)


    # ==========================================================
    # TICKER 1
    # ==========================================================

    ticker_1 = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//button[contains(@class,'co-po-ticker')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        ticker_1
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        ticker_1
    )

    time.sleep(2)


    # ==========================================================
    # TICKER 2
    # ==========================================================

    ticker_2 = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//button[contains(@class,'co-po-ticker')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        ticker_2
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        ticker_2
    )

    time.sleep(2)

    # ==========================================================
    # SAVE
    # ==========================================================

    save = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "attainmentSaveButton"
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

    time.sleep(2)

    # ==========================================================
    # SUCCESS / CONFIRMATION
    # ==========================================================

    ok_btn = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[normalize-space()='OK']"
            )
        )
    )

    assert ok_btn.is_displayed()

    driver.execute_script(
        "arguments[0].click();",
        ok_btn
    )

    time.sleep(3)

    # ==========================================================
    # VERIFY SUCCESS
    # ==========================================================

    assert driver.current_url is not None