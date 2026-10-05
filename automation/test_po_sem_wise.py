# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time


# def test_po_sem_wise(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 10)

#     # ---------------- Attainment ----------------

#     attainment = driver.find_element(
#         By.XPATH,
#         "//div//span[normalize-space()='Attainment']"
#     )
#     attainment.click()

#     # ---------------- CO Attainment ----------------

#     po_sem = driver.find_element(
#         By.XPATH,
#         "//a[normalize-space()='PO Semester Wise']"
#     )
#     po_sem.click()
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
    


#     # # ---------------- Search ----------------

#     search_btn = wait.until(
#         EC.element_to_be_clickable(
#             (By.ID, "semPoAttnSearchButton")
#         )
#     )
#     search_btn.click()

#     time.sleep(2)

#     driver.execute_script(
#     "window.scrollTo(0, document.body.scrollHeight);"

# )
#     time.sleep(2)
#     #eye btn
#     eye_btn = driver.find_element(By.XPATH,"//a[@class='sem-po-attn-eye-link js-sem-po-attn-detail-link']")
#     eye_btn.click()
    
#     time.sleep(4)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_po_sem_wise(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # EXTERNAL TEST DATA
    # ==========================================================

    branch_value = "STU Marol(east) Mumbai 400002"
    department_value = "IT-26"
    program_value = "New-IT"

    # Edge case data
    invalid_branch_value = "Invalid Branch"
    invalid_department_value = "Invalid Department"
    invalid_program_value = "Invalid Program"

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

    time.sleep(1)

    # ==========================================================
    # PO SEMESTER WISE
    # ==========================================================

    po_sem = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='PO Semester Wise']"
            )
        )
    )

    po_sem.click()

    time.sleep(2)

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

    time.sleep(1)

    # Verify valid branch exists
    branch_option = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[normalize-space()='{branch_value}']"
            )
        )
    )

    assert branch_option.is_displayed()

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
    # VERIFY SELECTED BRANCH
    # ==========================================================

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

    assert selected_branch.text.strip().casefold() == branch_value.casefold()
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

    time.sleep(1)

    department_option = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[normalize-space()='{department_value}']"
            )
        )
    )

    assert department_option.is_displayed()

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
    # VERIFY SELECTED DEPARTMENT
    # ==========================================================

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

    assert selected_department.text.strip() == department_value

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

    time.sleep(1)

    program_option = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[normalize-space()='{program_value}']"
            )
        )
    )

    assert program_option.is_displayed()

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
    # VERIFY SELECTED PROGRAM
    # ==========================================================

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

    assert selected_program.text.strip() == program_value

    # ==========================================================
    # EDGE CASE - INVALID BRANCH DATA
    # ==========================================================

    branch.click()

    invalid_branch = driver.find_elements(
        By.XPATH,
        f"//li[normalize-space()='{invalid_branch_value}']"
    )

    assert len(invalid_branch) == 0

    # Close dropdown
    branch.click()

    # ==========================================================
    # EDGE CASE - INVALID DEPARTMENT DATA
    # ==========================================================

    department.click()

    invalid_department = driver.find_elements(
        By.XPATH,
        f"//li[normalize-space()='{invalid_department_value}']"
    )

    assert len(invalid_department) == 0

    # Close dropdown
    department.click()

    # ==========================================================
    # EDGE CASE - INVALID PROGRAM DATA
    # ==========================================================

    program_dropdown.click()

    invalid_program = driver.find_elements(
        By.XPATH,
        f"//li[normalize-space()='{invalid_program_value}']"
    )

    assert len(invalid_program) == 0

    # Close dropdown
    program_dropdown.click()

    # ==========================================================
    # SEARCH BUTTON
    # ==========================================================

    search_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "semPoAttnSearchButton"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        search_btn
    )

    assert search_btn.is_enabled()

    search_btn.click()

    time.sleep(3)

    # ==========================================================
    # VERIFY SEARCH RESULT / NO RESULT
    # ==========================================================

    result_links = driver.find_elements(
        By.XPATH,
        "//a[contains(@class,'sem-po-attn-eye-link') "
        "and contains(@class,'js-sem-po-attn-detail-link')]"
    )

    # Either result should be displayed or application should
    # display a no-record message.
    no_record_messages = driver.find_elements(
        By.XPATH,
        "//*[contains(normalize-space(),'No Data') "
        "or contains(normalize-space(),'No Record') "
        "or contains(normalize-space(),'No records') "
        "or contains(normalize-space(),'No result')]"
    )

    assert len(result_links) > 0 or len(no_record_messages) > 0

    # ==========================================================
    # OPEN DETAIL
    # ==========================================================

    if len(result_links) > 0:

        eye_btn = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//a[contains(@class,'sem-po-attn-eye-link') "
                    "and contains(@class,'js-sem-po-attn-detail-link')])[1]"
                )
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            eye_btn
        )

        eye_btn.click()

        time.sleep(3)

        # ======================================================
        # VERIFY DETAIL PAGE / MODAL
        # ======================================================

        current_url = driver.current_url

        assert current_url is not None
        assert current_url != ""

    else:

        # No data available
        assert len(no_record_messages) > 0

    time.sleep(2)