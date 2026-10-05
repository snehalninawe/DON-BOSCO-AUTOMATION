# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import (
#     ElementClickInterceptedException,
#     ElementNotInteractableException
# )
# import time


# def test_fee_template(driver):

#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 20)

#     # ==========================================================
#     # TEST DATA
#     # ==========================================================

#     branch_value = "RTM,Marol(West),Mumbai-400021"
#     department_value = "CSE-2026"
#     program_value = "new-btech"
#     semester_value = "Sem-3(CSE)"

#     template_type_value = "Semester-wise"
#     academic_year_value = "2026-27"

#     template_name_value = "fee-demo"
#     fee_head_value = "Tution fees"
#     amount_value = "50000"
#     description_value = "tution fee"

#     # ==========================================================
#     # EDGE CASE DATA
#     # ==========================================================

#     empty_branch = ""
#     empty_department = ""
#     empty_program = ""
#     empty_semester = ""

#     invalid_branch = "Invalid Branch"
#     invalid_department = "Invalid Department"
#     invalid_program = "Invalid Program"
#     invalid_semester = "Invalid Semester"

#     invalid_amount = "-500"
#     zero_amount = "0"
#     empty_amount = ""

#     # ==========================================================
#     # DATA VALIDATION
#     # ==========================================================

#     assert branch_value.strip(), \
#         "Branch should not be empty"

#     assert department_value.strip(), \
#         "Department should not be empty"

#     assert program_value.strip(), \
#         "Program should not be empty"

#     assert semester_value.strip(), \
#         "Semester should not be empty"

#     assert template_type_value.strip(), \
#         "Template type should not be empty"

#     assert academic_year_value.strip(), \
#         "Academic year should not be empty"

#     assert template_name_value.strip(), \
#         "Template name should not be empty"

#     assert fee_head_value.strip(), \
#         "Fee head should not be empty"

#     assert amount_value.isdigit(), \
#         "Amount should contain only numbers"

#     assert int(amount_value) > 0, \
#         "Amount should be greater than zero"

#     assert description_value.strip(), \
#         "Description should not be empty"

#     # ==========================================================
#     # OPEN FEES COLLECTION
#     # ==========================================================

#     fees_collection_menu = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//div//span[normalize-space()='Fees Collection']"
#             )
#         )
#     )

#     fees_collection_menu.click()

#     time.sleep(1)

#     # ==========================================================
#     # OPEN FEES TEMPLATE
#     # ==========================================================

#     fees_template_modify = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//li[contains(.,'Fees Template')])[2]"
#             )
#         )
#     )

#     fees_template_modify.click()

#     time.sleep(2)

#     # ==========================================================
#     # ADD BUTTON
#     # ==========================================================

#     add_btn = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "attnAjaxAddRowsBtn"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         add_btn
#     )

#     time.sleep(1)

#     add_btn.click()

#     time.sleep(2)

#     # ==========================================================
#     # TEMPLATE TYPE
#     # ==========================================================

#     template_type = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'nice-select') "
#                 "and contains(@class,'primary_select') "
#                 "and contains(@class,'form-control')])[1]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         template_type
#     )

#     time.sleep(1)

#     template_type.click()

#     time.sleep(1)

#     template_option = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.XPATH,
#                 "//div[contains(@class,'nice-select') "
#                 "and contains(@class,'open')]"
#                 "//li[normalize-space()='Semester-wise']"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         template_option
#     )

#     time.sleep(1)

#     template_option.click()

#     time.sleep(1)

#     actual_template = template_type.text.strip()

#     assert actual_template.lower() == \
#         template_type_value.lower(), \
#         (
#             f"Template type was not selected correctly. "
#             f"Expected: '{template_type_value}', "
#             f"Actual: '{actual_template}'"
#         )

#     # # ==========================================================
#     # # ACADEMIC YEAR
#     # # ==========================================================

#     # academic_year = wait.until(
#     #     EC.element_to_be_clickable(
#     #         (
#     #             By.XPATH,
#     #             "(//div[contains(@class,'nice-select') "
#     #             "and contains(@class,'primary_select') "
#     #             "and contains(@class,'form-control')])[2]"
#     #         )
#     #     )
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     academic_year
#     # )

#     # time.sleep(1)

#     # academic_year.click()

#     # time.sleep(1)

#     # # ==========================================================
#     # # FIND ACADEMIC YEAR OPTION
#     # # ==========================================================

#     # academic_year_option = wait.until(
#     #     EC.visibility_of_element_located(
#     #         (
#     #             By.XPATH,
#     #             "//div[contains(@class,'nice-select') "
#     #             "and contains(@class,'open')]"
#     #             "//li[normalize-space()='2026-27']"
#     #         )
#     #     )
#     # )

#     # driver.execute_script(
#     #     "arguments[0].scrollIntoView({block:'center'});",
#     #     academic_year_option
#     # )

#     # time.sleep(1)

#     # try:

#     #     academic_year_option.click()

#     # except (
#     #     ElementClickInterceptedException,
#     #     ElementNotInteractableException
#     # ):

#     #     driver.execute_script(
#     #         "arguments[0].click();",
#     #         academic_year_option
#     #     )

#     # time.sleep(1)

#     # actual_academic_year = academic_year.text.strip()

#     # assert actual_academic_year.lower() == \
#     #     academic_year_value.lower(), \
#     #     (
#     #         f"Academic year was not selected correctly. "
#     #         f"Expected: '{academic_year_value}', "
#     #         f"Actual: '{actual_academic_year}'"
#     #     )

#     # ==========================================================
# # BRANCH MULTI-SELECT
# # ==========================================================

#     branch_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[1]"
#             )
#         )
#     )

#     branch_dropdown.click()

#     time.sleep(1)

#     branch_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[contains(normalize-space(),'{branch_value}')]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         branch_option
#     )

#     time.sleep(1)

#     branch_option.click()

#     time.sleep(1)


#     # ==========================================================
#     # DEPARTMENT MULTI-SELECT
#     # ==========================================================

#     department_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[2]"
#             )
#         )
#     )

#     department_dropdown.click()

#     time.sleep(1)

#     department_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[contains(normalize-space(),'{department_value}')]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         department_option
#     )

#     time.sleep(1)

#     department_option.click()

#     time.sleep(1)


#     # ==========================================================
#     # PROGRAM MULTI-SELECT
#     # ==========================================================

#     program_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[3]"
#             )
#         )
#     )

#     program_dropdown.click()

#     time.sleep(1)

#     program_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[contains(normalize-space(),'{program_value}')]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         program_option
#     )

#     time.sleep(1)

#     program_option.click()

#     time.sleep(1)


#     # ==========================================================
#     # SEMESTER MULTI-SELECT
#     # ==========================================================

#     semester_dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "(//div[contains(@class,'ms-options-wrap')])[4]"
#             )
#         )
#     )

#     semester_dropdown.click()

#     time.sleep(1)

#     semester_option = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 f"//li[contains(normalize-space(),'{semester_value}')]"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         semester_option
#     )

#     time.sleep(1)

#     semester_option.click()

#     time.sleep(1)

#     # ==========================================================
#     # FETCH
#     # ==========================================================

#     fetch = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.ID,
#                 "fetchTemplateBtn"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         fetch
#     )

#     time.sleep(1)

#     fetch.click()

#     time.sleep(3)

#     # ==========================================================
#     # SCROLL TO BOTTOM
#     # ==========================================================

#     driver.execute_script(
#         "window.scrollTo(0, document.body.scrollHeight);"
#     )

#     time.sleep(2)

#     # ==========================================================
#     # TEMPLATE NAME
#     # ==========================================================

#     template_name = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.ID,
#                 "template_name"
#             )
#         )
#     )

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         template_name
#     )

#     time.sleep(1)

#     template_name.clear()
#     template_name.send_keys(template_name_value)

#     assert template_name.get_attribute("value") == \
#         template_name_value, \
#         "Template name was not entered correctly"

#     # ==========================================================
#     # FEE HEAD NAME
#     # ==========================================================

#     fee_head_name = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.NAME,
#                 "fee_head_name[]"
#             )
#         )
#     )

#     fee_head_name.clear()
#     fee_head_name.send_keys(fee_head_value)

#     assert fee_head_name.get_attribute("value") == \
#         fee_head_value, \
#         "Fee head was not entered correctly"

#     # ==========================================================
#     # AMOUNT
#     # ==========================================================

#     amount = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.NAME,
#                 "fee_head_amount[]"
#             )
#         )
#     )

#     amount.clear()
#     amount.send_keys(amount_value)

#     assert amount.get_attribute("value") == \
#         amount_value, \
#         "Amount was not entered correctly"

#     # ==========================================================
#     # DESCRIPTION
#     # ==========================================================

#     desc = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.NAME,
#                 "fee_head_description[]"
#             )
#         )
#     )

#     desc.clear()
#     desc.send_keys(description_value)

#     assert desc.get_attribute("value") == \
#         description_value, \
#         "Description was not entered correctly"

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

#     driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});",
#         save
#     )

#     time.sleep(1)

#     try:

#         save.click()

#     except ElementClickInterceptedException:

#         driver.execute_script(
#             "arguments[0].click();",
#             save
#         )

#     time.sleep(3)

#     # ==========================================================
#     # VERIFY SUCCESS
#     # ==========================================================

#     success_message = wait.until(
#         EC.visibility_of_element_located(
#             (
#                 By.XPATH,
#                 "//*[contains(@class,'alert-success') "
#                 "or contains(@class,'toast-success') "
#                 "or contains(@class,'swal2-success')]"
#             )
#         )
#     )

#     assert success_message.is_displayed(), \
#         "Fee template success message was not displayed"

#     print("Fee template created successfully")



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    TimeoutException
)

from excel_reader import get_all_data
from excel_report import create_report

import time


def test_fee_template(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # EXTERNAL TEST DATA FROM EXCEL
    # ==========================================================

    data_list = get_all_data("Fee Template")

    results = []

    # ==========================================================
    # LOOP THROUGH ALL EXCEL DATA
    # ==========================================================

    for data in data_list:

        test_case = str(
            data.get("Test Case") or "Fee Template Create"
        ).strip()

        test_data = str(
            data.get("Test Data") or ""
        ).strip()

        branch_value = str(
            data.get("Branch") or ""
        ).strip()

        department_value = str(
            data.get("Department") or ""
        ).strip()

        program_value = str(
            data.get("Program") or ""
        ).strip()

        semester_value = str(
            data.get("Semester") or ""
        ).strip()

        template_type_value = str(
            data.get("Template Type") or ""
        ).strip()

        academic_year_value = str(
            data.get("Academic Year") or ""
        ).strip()

        template_name_value = str(
            data.get("Template Name") or ""
        ).strip()

        fee_head_value = str(
            data.get("Fee Head") or ""
        ).strip()

        amount_value = str(
            data.get("Amount") or ""
        ).strip()

        description_value = str(
            data.get("Description") or ""
        ).strip()

        validation_value = str(
            data.get("Validation") or ""
        ).strip()

        retry_test = str(
            data.get("Retry Test") or ""
        ).strip().upper()

        # ======================================================
        # DETERMINE EDGE CASE
        # ======================================================

        validation_lower = validation_value.lower()

        is_valid_test = validation_lower.startswith(
            "valid fee template"
        )

        is_edge_case = not is_valid_test

        # ======================================================
        # RETRY - MAXIMUM 3 ATTEMPTS
        # ======================================================

        max_attempts = 3 if retry_test == "YES" else 1

        for attempt in range(max_attempts):

            try:

                print(
                    "\n========================================"
                )

                print(
                    f"Test Case : {test_case}"
                )

                print(
                    f"Test Data : {test_data}"
                )

                print(
                    f"Validation : {validation_value}"
                )

                print(
                    f"Attempt : {attempt + 1}"
                )

                print(
                    "========================================"
                )

                # ==================================================
                # INTENTIONAL RETRY TEST
                # ==================================================

                if retry_test == "YES" and attempt == 0:

                    raise AssertionError(
                        "Intentional failure for retry testing"
                    )

                # ==================================================
                # OPEN FEES COLLECTION
                # ==================================================

                fees_collection_menu = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div//span[normalize-space()='Fees Collection']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    fees_collection_menu
                )

                time.sleep(1)

                try:

                    fees_collection_menu.click()

                except ElementClickInterceptedException:

                    driver.execute_script(
                        "arguments[0].click();",
                        fees_collection_menu
                    )

                time.sleep(1)

                # ==================================================
                # OPEN FEES TEMPLATE
                # ==================================================

                fees_template_modify = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//li[contains(.,'Fees Template')])[2]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    fees_template_modify
                )

                time.sleep(1)

                try:

                    fees_template_modify.click()

                except ElementClickInterceptedException:

                    driver.execute_script(
                        "arguments[0].click();",
                        fees_template_modify
                    )

                time.sleep(2)

                # ==================================================
                # ADD BUTTON
                # ==================================================

                add_btn = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.ID,
                            "attnAjaxAddRowsBtn"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    add_btn
                )

                time.sleep(1)

                try:

                    add_btn.click()

                except ElementClickInterceptedException:

                    driver.execute_script(
                        "arguments[0].click();",
                        add_btn
                    )

                time.sleep(2)

                # ==================================================
                # TEMPLATE TYPE
                # ==================================================

                template_type = wait.until(
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
                    template_type
                )

                time.sleep(1)

                driver.execute_script(
                    "arguments[0].click();",
                    template_type
                )

                time.sleep(1)

                template_option = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') "
                            "and contains(@class,'open')]"
                            f"//li[normalize-space()="
                            f"'{template_type_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    template_option
                )

                time.sleep(1)

                driver.execute_script(
                    "arguments[0].click();",
                    template_option
                )

                time.sleep(1)

                # ==================================================
                # VERIFY TEMPLATE TYPE
                # ==================================================

                actual_template = template_type.text.strip()

                assert actual_template.lower() == \
                    template_type_value.lower(), (

                        f"Template type was not selected correctly. "
                        f"Expected: '{template_type_value}', "
                        f"Actual: '{actual_template}'"
                    )

                # ==================================================
                # BRANCH
                # ==================================================

                branch_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'ms-options-wrap')])[1]"
                        )
                    )
                )

                branch_dropdown.click()

                time.sleep(1)

                if branch_value:

                    branch_option = wait.until(
                        EC.element_to_be_clickable(
                            (
                                By.XPATH,
                                f"//li[contains(normalize-space(),"
                                f"'{branch_value}')]"
                            )
                        )
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        branch_option
                    )

                    time.sleep(1)

                    branch_option.click()

                    time.sleep(1)

                # ==================================================
                # DEPARTMENT
                # ==================================================

                department_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'ms-options-wrap')])[2]"
                        )
                    )
                )

                department_dropdown.click()

                time.sleep(1)

                if department_value:

                    department_option = wait.until(
                        EC.element_to_be_clickable(
                            (
                                By.XPATH,
                                f"//li[contains(normalize-space(),"
                                f"'{department_value}')]"
                            )
                        )
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        department_option
                    )

                    time.sleep(1)

                    department_option.click()

                    time.sleep(1)

                # ==================================================
                # PROGRAM
                # ==================================================

                program_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'ms-options-wrap')])[3]"
                        )
                    )
                )

                program_dropdown.click()

                time.sleep(1)

                if program_value:

                    program_option = wait.until(
                        EC.element_to_be_clickable(
                            (
                                By.XPATH,
                                f"//li[contains(normalize-space(),"
                                f"'{program_value}')]"
                            )
                        )
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        program_option
                    )

                    time.sleep(1)

                    program_option.click()

                    time.sleep(1)

                # ==================================================
                # SEMESTER
                # ==================================================

                semester_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'ms-options-wrap')])[4]"
                        )
                    )
                )

                semester_dropdown.click()

                time.sleep(1)

                if semester_value:

                    semester_option = wait.until(
                        EC.element_to_be_clickable(
                            (
                                By.XPATH,
                                f"//li[contains(normalize-space(),"
                                f"'{semester_value}')]"
                            )
                        )
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        semester_option
                    )

                    time.sleep(1)

                    semester_option.click()

                    time.sleep(1)

                # ==================================================
                # FETCH
                # ==================================================

                fetch = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.ID,
                            "fetchTemplateBtn"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    fetch
                )

                time.sleep(1)

                driver.execute_script(
                    "arguments[0].click();",
                    fetch
                )

                time.sleep(3)

                # ==================================================
                # SCROLL TO BOTTOM
                # ==================================================

                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )

                time.sleep(2)

                # ==================================================
                # TEMPLATE NAME
                # ==================================================

                template_name = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.ID,
                            "template_name"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    template_name
                )

                time.sleep(1)

                template_name.clear()

                if template_name_value:

                    template_name.send_keys(
                        template_name_value
                    )

                if template_name_value:

                    actual_template_name = (
                        template_name.get_attribute("value")
                    )

                    assert actual_template_name == \
                        template_name_value, (

                            f"Template name mismatch. "
                            f"Expected: '{template_name_value}', "
                            f"Actual: '{actual_template_name}'"
                        )

                # ==================================================
                # FEE HEAD NAME
                # ==================================================

                fee_head_name = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.NAME,
                            "fee_head_name[]"
                        )
                    )
                )

                fee_head_name.clear()

                if fee_head_value:

                    fee_head_name.send_keys(
                        fee_head_value
                    )

                if fee_head_value:

                    actual_fee_head = (
                        fee_head_name.get_attribute("value")
                    )

                    assert actual_fee_head == \
                        fee_head_value, (

                            f"Fee head mismatch. "
                            f"Expected: '{fee_head_value}', "
                            f"Actual: '{actual_fee_head}'"
                        )

                # ==================================================
                # AMOUNT
                # ==================================================

                amount = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.NAME,
                            "fee_head_amount[]"
                        )
                    )
                )

                amount.clear()

                if amount_value:

                    amount.send_keys(
                        amount_value
                    )

                if amount_value:

                    actual_amount = (
                        amount.get_attribute("value")
                    )

                    assert actual_amount == \
                        amount_value, (

                            f"Amount mismatch. "
                            f"Expected: '{amount_value}', "
                            f"Actual: '{actual_amount}'"
                        )

                # ==================================================
                # DESCRIPTION
                # ==================================================

                desc = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.NAME,
                            "fee_head_description[]"
                        )
                    )
                )

                desc.clear()

                if description_value:

                    desc.send_keys(
                        description_value
                    )

                if description_value:

                    actual_description = (
                        desc.get_attribute("value")
                    )

                    assert actual_description == \
                        description_value, (

                            f"Description mismatch. "
                            f"Expected: '{description_value}', "
                            f"Actual: '{actual_description}'"
                        )

                # ==================================================
                # SAVE
                # ==================================================

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

                time.sleep(1)

                try:

                    save.click()

                except ElementClickInterceptedException:

                    driver.execute_script(
                        "arguments[0].click();",
                        save
                    )

                time.sleep(3)

                # ==================================================
                # EDGE CASE VALIDATION
                # ==================================================

                if is_edge_case:

                    # ----------------------------------------------
                    # VALIDATION MESSAGES
                    # ----------------------------------------------

                    validation_messages = driver.find_elements(
                        By.XPATH,
                        "//*[contains(@class,'invalid-feedback') "
                        "or contains(@class,'text-danger') "
                        "or contains(@class,'error') "
                        "or @role='alert']"
                    )

                    # ----------------------------------------------
                    # DUPLICATE FEE TEMPLATE
                    # ----------------------------------------------

                    duplicate_messages = driver.find_elements(
                        By.XPATH,
                        "//*[contains("
                        "translate(normalize-space(.),"
                        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                        "'abcdefghijklmnopqrstuvwxyz'),"
                        "'already exists')]"
                    )

                    # ----------------------------------------------
                    # ALL VALIDATION MESSAGES
                    # ----------------------------------------------

                    all_validation_messages = (
                        validation_messages
                        + duplicate_messages
                    )

                    if all_validation_messages:

                        message_text = ""

                        for message in all_validation_messages:

                            text = message.text.strip()

                            if text:

                                message_text = text
                                break

                        if message_text:

                            print(
                                f"PASS EDGE CASE: "
                                f"{validation_value}"
                            )

                            print(
                                f"Validation Message: "
                                f"{message_text}"
                            )

                            results.append({

                                "Test Case":
                                    test_case,

                                "Test Data":
                                    test_data,

                                "Edge Case":
                                    "YES",

                                "Validation":
                                    validation_value,

                                "Attempt":
                                    attempt + 1,

                                "Status":
                                    "PASS",

                                "Error":
                                    message_text,

                                "Final Status":
                                    "PASS"
                            })

                            break

                    # ----------------------------------------------
                    # VALIDATION NOT FOUND
                    # ----------------------------------------------

                    raise AssertionError(
                        f"Expected validation not displayed "
                        f"for edge case: "
                        f"{validation_value}"
                    )

                # ==================================================
                # VALID FEE TEMPLATE
                # ==================================================

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

                assert success_message.is_displayed(), (
                    "Fee template success message was not displayed"
                )

                print(
                    f"PASS: {test_case}"
                )

                # ==================================================
                # SUCCESS RESULT
                # ==================================================

                results.append({

                    "Test Case":
                        test_case,

                    "Test Data":
                        test_data,

                    "Edge Case":
                        "NO",

                    "Validation":
                        validation_value,

                    "Attempt":
                        attempt + 1,

                    "Status":
                        "PASS",

                    "Error":
                        "",

                    "Final Status":
                        "PASS"
                })

                break

            # ======================================================
            # FAILURE / RETRY
            # ======================================================

            except Exception as e:

                print(
                    f"FAIL: {test_case} "
                    f"| Attempt {attempt + 1}"
                )

                print(
                    f"Error: {e}"
                )

                # ==================================================
                # RETRY
                # ==================================================

                if attempt < max_attempts - 1:

                    print(
                        f"Retrying {test_case}..."
                    )

                    results.append({

                        "Test Case":
                            test_case,

                        "Test Data":
                            test_data,

                        "Edge Case":
                            "YES"
                            if is_edge_case
                            else "NO",

                        "Validation":
                            validation_value,

                        "Attempt":
                            attempt + 1,

                        "Status":
                            "FAIL",

                        "Error":
                            str(e),

                        "Final Status":
                            "RETRY"
                    })

                    driver.refresh()

                    time.sleep(2)

                # ==================================================
                # FINAL FAILURE
                # ==================================================

                else:

                    print(
                        f"FINAL FAIL: {test_case}"
                    )

                    results.append({

                        "Test Case":
                            test_case,

                        "Test Data":
                            test_data,

                        "Edge Case":
                            "YES"
                            if is_edge_case
                            else "NO",

                        "Validation":
                            validation_value,

                        "Attempt":
                            attempt + 1,

                        "Status":
                            "FAIL",

                        "Error":
                            str(e),

                        "Final Status":
                            "FAIL"
                    })

                    # Continue with next Excel row
                    break

    # ==============================================================
    # CREATE FINAL EXCEL REPORT
    # ==============================================================

    create_report(results)

    print(
        "\n================================================"
    )

    print(
        "ALL FEE TEMPLATE TEST CASES COMPLETED"
    )

    print(
        "Excel report generated successfully."
    )

    print(
        "================================================"
    )