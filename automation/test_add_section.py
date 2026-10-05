# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time


# def test_add_section(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 15)

#     # ---------------- UNIVERSITY ----------------

#     university = driver.find_element(
#         By.XPATH,
#         "//div//span[normalize-space()='University']"
#     )

#     university.click()
#     # driver.execute_script("arguments[0].click();", university)

#     time.sleep(2)


#     # ---------------- SEMESTER ----------------

#     section = driver.find_element(
#         By.XPATH,
#         "//a[normalize-space()='Section']"
#     )

#     section.click()

#     time.sleep(2)


#     # ---------------- ADD BUTTON ----------------

#     # add_button = driver.find_element(
#     #     By.XPATH,
#     #     "//a[contains(@class,'nxgn_primary_button button_bg_primary')]"
#     # )

#     # add_button.click()

#     # time.sleep(2)

#     #--------------name field----------------
#     # section_name = driver.find_element(By.NAME,'section_name')
#     # section_name.send_keys('section-C-IT')
        

#     # ==================================================
#     #                    SUBMIT
#     # ==================================================

#     # submit_button = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (By.ID, "submitButton")
#     #     )
#     # )

#     # submit_button.click()
    
#     #for editing the department
#     three_dots = driver.find_element(By.XPATH,"(//button[@class='attn-ajax-action_button'])[1]")
#     three_dots.click()
    
#     # edit_button = driver.find_element(By.XPATH,"(//a[contains(.,'edit')])[1]")
#     # edit_button.click()
    

#     # time.sleep(1)

# # --------------edit name field----------------
# #     section_name = wait.until(
# #     EC.visibility_of_element_located(
# #         (By.ID, "section_name")
# #     )
# # )
# #     section_name.click()
# #     section_name.clear()
# #     section_name.send_keys("section-C-IT-1")
        
    
# #         # ==================================================
# #         #                    SUBMIT
# #         # ==================================================
    
#     # submit_button = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (By.XPATH, "//button[@id='submitButton']")
#     #         )
#     #     )
    
#     # submit_button.click()
    
    
    
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
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)

from excel_reader import get_all_data
from excel_report import create_report

import time


def test_add_section(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 15)

    # ==========================================================
    # READ TEST DATA FROM EXCEL
    # ==========================================================

    data_list = get_all_data("Add Section")

    results = []

    # ==========================================================
    # EXECUTE EACH EXCEL ROW
    # ==========================================================

    for data in data_list:

        test_case = str(
            data.get("Test Case") or ""
        ).strip()

        test_data = str(
            data.get("Test Data") or ""
        ).strip()

        existing_section = str(
            data.get("Existing Section") or ""
        ).strip()

        section_name_value = str(
            data.get("Section Name") or ""
        ).strip()

        validation = str(
            data.get("Validation") or ""
        ).strip()

        retry_test = str(
            data.get("Retry Test") or ""
        ).strip().upper()

        validation_lower = validation.lower()

        # ======================================================
        # TEST TYPE
        # ======================================================

        is_create = test_case.lower() == "section create"
        is_edit = test_case.lower() == "section edit"
        is_delete = test_case.lower() == "section delete"

        # Valid create test
        is_valid_test = validation_lower.startswith("valid section")

        # Everything else for Create is edge case
        is_edge_case = not is_valid_test

        # Retry maximum 3 attempts
        max_attempts = 3 if retry_test == "YES" else 1

        print("\n==================================================")
        print("Test Case:", test_case)
        print("Test Data:", test_data)
        print("Existing Section:", existing_section)
        print("Section Name:", section_name_value)
        print("Validation:", validation)
        print("Retry Test:", retry_test)
        print("==================================================")

        final_status = "FAIL"

        # ======================================================
        # RETRY LOOP
        # ======================================================

        for attempt in range(1, max_attempts + 1):

            try:

                # ==================================================
                # INTENTIONAL FAILURE FOR RETRY TEST
                # ==================================================

                if retry_test == "YES" and attempt == 1:

                    raise AssertionError(
                        "Intentional failure for retry testing"
                    )

                # ==================================================
                # UNIVERSITY
                # ==================================================

                university = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div//span[normalize-space()='University']"
                        )
                    )
                )

                university.click()

                # ==================================================
                # SECTION
                # ==================================================

                section = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//a[normalize-space()='Section']"
                        )
                    )
                )

                section.click()

                time.sleep(2)

                # ==================================================
                # CREATE SECTION
                # ==================================================

                if is_create:

                    # ==================================================
                    # ADD SECTION BUTTON
                    # ==================================================

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

                    try:
                        add_button.click()

                    except ElementClickInterceptedException:

                        driver.execute_script(
                            "arguments[0].click();",
                            add_button
                        )

                    # ==================================================
                    # SECTION NAME
                    # ==================================================

                    section_name = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.ID,
                                "section_name"
                            )
                        )
                    )

                    section_name.click()
                    section_name.clear()

                    # Keep original value from Excel
                    original_section_value = str(
                        data.get("Section Name") or ""
                    )

                    section_name.send_keys(
                        original_section_value
                    )

                    # ==================================================
                    # SUBMIT
                    # ==================================================

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

                    time.sleep(1)

                    try:
                        submit_button.click()

                    except ElementClickInterceptedException:

                        driver.execute_script(
                            "arguments[0].click();",
                            submit_button
                        )

                    time.sleep(2)

                    # ==================================================
                    # EDGE CASE VALIDATION
                    # ==================================================

                    if is_edge_case:

                        validation_found = False

                        validation_locators = [

                            (
                                By.XPATH,
                                "//*[contains(@class,'invalid-feedback') "
                                "and normalize-space()]"
                            ),

                            (
                                By.XPATH,
                                "//*[contains(@class,'text-danger') "
                                "and normalize-space()]"
                            ),

                            (
                                By.XPATH,
                                "//*[contains(@class,'error') "
                                "and normalize-space()]"
                            ),

                            (
                                By.XPATH,
                                "//*[@role='alert' and normalize-space()]"
                            ),

                            (
                                By.XPATH,
                                "//*[contains(translate(normalize-space(),"
                                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                                "'abcdefghijklmnopqrstuvwxyz'),"
                                "'already exists')]"
                            )
                        ]

                        for locator in validation_locators:

                            try:

                                messages = driver.find_elements(
                                    *locator
                                )

                                for message in messages:

                                    if message.is_displayed():

                                        message_text = (
                                            message.text.strip()
                                        )

                                        if message_text:

                                            print(
                                                "Validation Message:",
                                                message_text
                                            )

                                            validation_found = True
                                            break

                                if validation_found:
                                    break

                            except Exception:
                                continue

                        # ==================================================
                        # VALIDATION FOUND
                        # ==================================================

                        if validation_found:

                            results.append({
                                "Test Case": test_case,
                                "Test Data": test_data,
                                "Existing Section": existing_section,
                                "Section Name": section_name_value,
                                "Validation": validation,
                                "Attempt": attempt,
                                "Status": "PASS",
                                "Error": "",
                                "Final Status": "PASS"
                            })

                            final_status = "PASS"

                            break

                        else:

                            raise AssertionError(
                                "Expected validation message "
                                "was not found"
                            )

                    # ==================================================
                    # VALID CREATE
                    # ==================================================

                    else:

                        wait.until(
                            EC.presence_of_element_located(
                                (
                                    By.XPATH,
                                    f"//*[contains(normalize-space(),"
                                    f"'{section_name_value}')]"
                                )
                            )
                        )

                        assert section_name_value in driver.page_source

                        print(
                            "Section created successfully:",
                            section_name_value
                        )

                        results.append({
                            "Test Case": test_case,
                            "Test Data": test_data,
                            "Existing Section": existing_section,
                            "Section Name": section_name_value,
                            "Validation": validation,
                            "Attempt": attempt,
                            "Status": "PASS",
                            "Error": "",
                            "Final Status": "PASS"
                        })

                        final_status = "PASS"

                        break

                # ======================================================
                # EDIT SECTION
                # ======================================================

                elif is_edit:

                    # ==================================================
                    # FIND EXISTING SECTION
                    # ==================================================

                    section_row = wait.until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                f"//tr[.//*[contains(normalize-space(),"
                                f"'{existing_section}')]]"
                            )
                        )
                    )

                    # ==================================================
                    # THREE DOTS
                    # ==================================================

                    three_dots = section_row.find_element(
                        By.XPATH,
                        ".//button[contains(@class,"
                        "'attn-ajax-action_button')]"
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        three_dots
                    )

                    time.sleep(1)

                    try:
                        three_dots.click()

                    except ElementClickInterceptedException:

                        driver.execute_script(
                            "arguments[0].click();",
                            three_dots
                        )

                    time.sleep(1)

                    # ==================================================
                    # EDIT BUTTON
                    # ==================================================

                    edit_button = section_row.find_element(
                        By.XPATH,
                        ".//a[contains(translate(normalize-space(),"
                        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                        "'abcdefghijklmnopqrstuvwxyz'),"
                        "'edit')]"
                    )

                    driver.execute_script(
                        "arguments[0].click();",
                        edit_button
                    )

                    time.sleep(1)

                    # ==================================================
                    # EDIT SECTION NAME
                    # ==================================================

                    section_name = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.ID,
                                "section_name"
                            )
                        )
                    )

                    section_name.clear()

                    section_name.send_keys(
                        section_name_value
                    )

                    # ==================================================
                    # SUBMIT EDIT
                    # ==================================================

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

                    time.sleep(1)

                    try:
                        submit_button.click()

                    except ElementClickInterceptedException:

                        driver.execute_script(
                            "arguments[0].click();",
                            submit_button
                        )

                    time.sleep(2)

                    # ==================================================
                    # VERIFY EDIT
                    # ==================================================

                    wait.until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                f"//*[contains(normalize-space(),"
                                f"'{section_name_value}')]"
                            )
                        )
                    )

                    assert section_name_value in driver.page_source

                    print(
                        "Section edited successfully:",
                        section_name_value
                    )

                    results.append({
                        "Test Case": test_case,
                        "Test Data": test_data,
                        "Existing Section": existing_section,
                        "Section Name": section_name_value,
                        "Validation": validation,
                        "Attempt": attempt,
                        "Status": "PASS",
                        "Error": "",
                        "Final Status": "PASS"
                    })

                    final_status = "PASS"

                    break

                # ======================================================
                # DELETE SECTION
                # ======================================================

                elif is_delete:

                    # ==================================================
                    # FIND EXISTING SECTION
                    # ==================================================

                    section_row = wait.until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                f"//tr[.//*[contains(normalize-space(),"
                                f"'{existing_section}')]]"
                            )
                        )
                    )

                    # ==================================================
                    # THREE DOTS
                    # ==================================================

                    three_dots = section_row.find_element(
                        By.XPATH,
                        ".//button[contains(@class,"
                        "'attn-ajax-action_button')]"
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        three_dots
                    )

                    time.sleep(1)

                    try:
                        three_dots.click()

                    except ElementClickInterceptedException:

                        driver.execute_script(
                            "arguments[0].click();",
                            three_dots
                        )

                    time.sleep(1)

                    # ==================================================
                    # DELETE BUTTON
                    # ==================================================

                    delete_buttons = section_row.find_elements(
                        By.XPATH,
                        ".//a[contains(translate(normalize-space(),"
                        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                        "'abcdefghijklmnopqrstuvwxyz'),"
                        "'delete')]"
                    )

                    print("Delete buttons found:", len(delete_buttons))

                    driver.execute_script(
                        "arguments[0].click();",
                        delete_buttons[0]
                    )

                    time.sleep(1)

                    # ==================================================
                    # DELETE MODAL
                    # ==================================================

                    modal = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                "//div[@aria-describedby="
                                "'swal2-html-container']"
                            )
                        )
                    )

                    assert modal.is_displayed()

                    # ==================================================
                    # CONFIRM DELETE
                    # ==================================================

                    confirm_button = wait.until(
                        EC.element_to_be_clickable(
                            (
                                By.XPATH,
                                "//button[contains(@class,"
                                "'swal2-confirm')]"
                            )
                        )
                    )

                    confirm_button.click()

                    # ==================================================
                    # WAIT FOR MODAL
                    # ==================================================

                    wait.until(
                        EC.invisibility_of_element_located(
                            (
                                By.XPATH,
                                "//div[@aria-describedby="
                                "'swal2-html-container']"
                            )
                        )
                    )

                    time.sleep(2)

                    # ==================================================
                    # VERIFY DELETE
                    # ==================================================

                    deleted_rows = driver.find_elements(
                        By.XPATH,
                        f"//tr[.//*[contains(normalize-space(),"
                        f"'{existing_section}')]]"
                    )

                    assert len(deleted_rows) == 0

                    print(
                        "Section deleted successfully:",
                        existing_section
                    )

                    results.append({
                        "Test Case": test_case,
                        "Test Data": test_data,
                        "Existing Section": existing_section,
                        "Section Name": section_name_value,
                        "Validation": validation,
                        "Attempt": attempt,
                        "Status": "PASS",
                        "Error": "",
                        "Final Status": "PASS"
                    })

                    final_status = "PASS"

                    break

                # ======================================================
                # UNKNOWN TEST CASE
                # ======================================================

                else:

                    raise AssertionError(
                        f"Unknown Test Case: {test_case}"
                    )

            # ======================================================
            # FAILURE / RETRY
            # ======================================================

            except Exception as e:

                error_message = str(e)

                print(
                    f"Attempt {attempt} FAILED:",
                    error_message
                )

                # ==================================================
                # RETRY
                # ==================================================

                if attempt < max_attempts:

                    results.append({
                        "Test Case": test_case,
                        "Test Data": test_data,
                        "Existing Section": existing_section,
                        "Section Name": section_name_value,
                        "Validation": validation,
                        "Attempt": attempt,
                        "Status": "RETRY",
                        "Error": error_message,
                        "Final Status": "RETRY"
                    })

                    print(
                        f"Retrying test... "
                        f"Attempt {attempt + 1}/{max_attempts}"
                    )

                    driver.refresh()

                    time.sleep(2)

                # ==================================================
                # FINAL FAILURE
                # ==================================================

                else:

                    results.append({
                        "Test Case": test_case,
                        "Test Data": test_data,
                        "Existing Section": existing_section,
                        "Section Name": section_name_value,
                        "Validation": validation,
                        "Attempt": attempt,
                        "Status": "FAIL",
                        "Error": error_message,
                        "Final Status": "FAIL"
                    })

                    final_status = "FAIL"

                    break

        print(
            "Final Status:",
            final_status
        )

    # ==========================================================
    # CREATE EXCEL REPORT
    # ==========================================================

    create_report(results)