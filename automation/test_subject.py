from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from excel_report import create_report
from excel_reader import get_all_data


def test_subject(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # EXTERNAL TEST DATA FROM EXCEL
    # ==========================================================

    data_list = get_all_data("Sheet4")
    results = []

    # ==========================================================
    # LOOP THROUGH ALL EXCEL DATA
    # ==========================================================

    for data in data_list:

        # ======================================================
        # VALID DATA
        # ======================================================

        subject_name_value = str(
            data["Subject Name"] or ""
        ).strip()

        subject_code_value = str(
            data["Subject Code"] or ""
        ).strip()

        subject_type_value = str(
            data["Subject Type"] or ""
        ).strip()

        branch_value = str(
            data["Branch"] or ""
        ).strip()

        department_value = str(
            data["Department"] or ""
        ).strip()

        program_value = str(
            data["Program"] or ""
        ).strip()

        semester_value = str(
            data["Semester"] or ""
        ).strip()

        scheme_value = str(
            data["Scheme"] or ""
        ).strip()

        total_marks_value = str(
            data["Total Marks"] or ""
        ).strip()

        pass_marks_value = str(
            data["Pass Marks"] or ""
        ).strip()

        ia1_marks_value = str(
            data["IA1 Marks"] or ""
        ).strip()

        ia2_marks_value = str(
            data["IA2 Marks"] or ""
        ).strip()

        # ======================================================
        # EDGE CASE DATA
        # ======================================================

        invalid_total_marks = str(
            data["Invalid Total Marks"] or ""
        ).strip()

        invalid_pass_marks = str(
            data["Invalid Pass Marks"] or ""
        ).strip()

        invalid_marks = str(
            data["Invalid Marks"] or ""
        ).strip()

        retry_test = str(
            data["Retry Test"] or ""
        ).strip().upper()

        # ======================================================
        # RETRY - MAXIMUM 3 ATTEMPTS
        # ======================================================

        for attempt in range(3):

            try:

                print(
                    "\n========================================"
                )

                print(
                    f"Running: {subject_name_value}"
                )

                print(
                    f"Attempt: {attempt + 1}"
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
                # SUBJECT
                # ==========================================================

                subject = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//a[normalize-space()='Subject']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    subject
                )

                driver.execute_script(
                    "arguments[0].click();",
                    subject
                )

                time.sleep(2)

                # ==========================================================
                # ADD SUBJECT
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
                # SUBJECT NAME
                # ==========================================================

                subject_name = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.NAME,
                            "subject_name"
                        )
                    )
                )

                subject_name.clear()

                subject_name.send_keys(
                    subject_name_value
                )

                actual_subject_name = (
                    subject_name.get_attribute("value")
                )

                assert (
                    actual_subject_name
                    == subject_name_value
                ), (
                    f"Subject name mismatch. "
                    f"Expected: {subject_name_value}, "
                    f"Actual: {actual_subject_name}"
                )

                # ==========================================================
                # SUBJECT CODE
                # ==========================================================

                subject_code = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.NAME,
                            "subject_code"
                        )
                    )
                )

                subject_code.clear()

                subject_code.send_keys(
                    subject_code_value
                )

                actual_subject_code = (
                    subject_code.get_attribute("value")
                )

                assert (
                    actual_subject_code
                    == subject_code_value
                ), (
                    f"Subject code mismatch. "
                    f"Expected: {subject_code_value}, "
                    f"Actual: {actual_subject_code}"
                )

                # ==========================================================
                # SUBJECT TYPE
                # ==========================================================

                subject_type_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[1]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    subject_type_dropdown
                )

                subject_type_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') "
                            "and contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{subject_type_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    subject_type_option
                )

                selected_subject_type = wait.until(
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
                    selected_subject_type.text.strip().lower()
                    == subject_type_value.lower()
                ), "Subject Type selection mismatch"

                # ==========================================================
                # BRANCH
                # ==========================================================

                branch_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[3]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    branch_dropdown
                )

                branch_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') "
                            "and contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{branch_value}']"
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

                selected_branch = wait.until(
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
                    selected_branch.text.strip().lower()
                    == branch_value.lower()
                ), "Branch selection mismatch"

                # ==========================================================
                # DEPARTMENT
                # ==========================================================

                department_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[4]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    department_dropdown
                )

                department_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') "
                            "and contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{department_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    department_option
                )

                selected_department = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[4]"
                            "//span[contains(@class,'current')]"
                        )
                    )
                )

                assert (
                    selected_department.text.strip().lower()
                    == department_value.lower()
                ), "Department selection mismatch"

                # ==========================================================
                # PROGRAM
                # ==========================================================

                program_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[5]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    program_dropdown
                )

                program_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') "
                            "and contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{program_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    program_option
                )

                selected_program = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[5]"
                            "//span[contains(@class,'current')]"
                        )
                    )
                )

                assert (
                    selected_program.text.strip().lower()
                    == program_value.lower()
                ), "Program selection mismatch"

                # ==========================================================
                # SEMESTER
                # ==========================================================

                semester_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[6]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    semester_dropdown
                )

                semester_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') "
                            "and contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{semester_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    semester_option
                )

                selected_semester = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[6]"
                            "//span[contains(@class,'current')]"
                        )
                    )
                )

                assert (
                    selected_semester.text.strip().lower()
                    == semester_value.lower()
                ), "Semester selection mismatch"

                # ==========================================================
                # SCHEME
                # ==========================================================

                scheme_dropdown = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[7]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    scheme_dropdown
                )

                scheme_option = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,'nice-select') "
                            "and contains(@class,'open')]"
                            "//li[normalize-space()="
                            f"'{scheme_value}']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    scheme_option
                )

                selected_scheme = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'nice-select') "
                            "and contains(@class,'primary_select')])[7]"
                            "//span[contains(@class,'current')]"
                        )
                    )
                )

                assert (
                    selected_scheme.text.strip().lower()
                    == scheme_value.lower()
                ), "Scheme selection mismatch"

                # ==========================================================
                # TOTAL MARKS
                # ==========================================================

                total_marks = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.ID,
                            "total_marks"
                        )
                    )
                )

                total_marks.clear()

                total_marks.send_keys(
                    total_marks_value
                )

                assert (
                    total_marks.get_attribute("value")
                    == total_marks_value
                ), "Total Marks mismatch"

                # ==========================================================
                # PASS MARKS
                # ==========================================================

                pass_marks = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.ID,
                            "pass_mark"
                        )
                    )
                )

                pass_marks.clear()

                pass_marks.send_keys(
                    pass_marks_value
                )

                assert (
                    pass_marks.get_attribute("value")
                    == pass_marks_value
                ), "Pass Marks mismatch"

                # ==========================================================
                # VALIDATION LOCATOR
                # ==========================================================

                validation_xpath = (
                    "//*[contains(@class,'invalid-feedback') "
                    "or contains(@class,'text-danger') "
                    "or contains(@class,'error') "
                    "or contains(@class,'alert-danger') "
                    "or contains(translate(normalize-space(.),"
                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    "'abcdefghijklmnopqrstuvwxyz'),"
                    "'already exists')]"
                )

                # ==========================================================
                # EDGE CASE - INVALID TOTAL MARKS
                # ==========================================================

                if invalid_total_marks:

                    print(
                        "Testing Invalid Total Marks: "
                        f"{invalid_total_marks}"
                    )

                    total_marks.clear()

                    total_marks.send_keys(
                        invalid_total_marks
                    )

                    actual_invalid_total = (
                        total_marks.get_attribute("value")
                    )

                    if actual_invalid_total == invalid_total_marks:

                        submit_button = wait.until(
                            EC.element_to_be_clickable(
                                (
                                    By.ID,
                                    "submitButton"
                                )
                            )
                        )

                        driver.execute_script(
                            "arguments[0].click();",
                            submit_button
                        )

                        time.sleep(1)

                        validation_error = driver.find_elements(
                            By.XPATH,
                            validation_xpath
                        )

                        assert validation_error, (
                            "Invalid Total Marks were accepted "
                            "without validation."
                        )

                        print(
                            "PASS: Invalid Total Marks validation."
                        )

                    total_marks.clear()

                    total_marks.send_keys(
                        total_marks_value
                    )

                # ==========================================================
                # EDGE CASE - INVALID PASS MARKS
                # ==========================================================

                if invalid_pass_marks:

                    print(
                        "Testing Invalid Pass Marks: "
                        f"{invalid_pass_marks}"
                    )

                    pass_marks.clear()

                    pass_marks.send_keys(
                        invalid_pass_marks
                    )

                    submit_button = wait.until(
                        EC.element_to_be_clickable(
                            (
                                By.ID,
                                "submitButton"
                            )
                        )
                    )

                    driver.execute_script(
                        "arguments[0].click();",
                        submit_button
                    )

                    time.sleep(1)

                    validation_messages = driver.find_elements(
                        By.XPATH,
                        validation_xpath
                    )

                    actual_pass_marks = (
                        pass_marks.get_attribute("value")
                    )

                    if not validation_messages:

                        assert (
                            actual_pass_marks
                            != invalid_pass_marks
                        ), (
                            "Invalid Pass Marks were accepted."
                        )

                    else:

                        print(
                            "PASS: Invalid Pass Marks "
                            "validation displayed."
                        )

                    pass_marks.clear()

                    pass_marks.send_keys(
                        pass_marks_value
                    )

                # ==========================================================
                # RESTORE VALID MARKS
                # ==========================================================

                total_marks.clear()

                total_marks.send_keys(
                    total_marks_value
                )

                pass_marks.clear()

                pass_marks.send_keys(
                    pass_marks_value
                )

                # ==========================================================
                # SUBMIT VALID SUBJECT
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

                time.sleep(2)

                # ==========================================================
                # PORTAL VALIDATION
                # ==========================================================

                validation_messages = driver.find_elements(
                    By.XPATH,
                    validation_xpath
                )

                if validation_messages:

                    messages = []

                    for message in validation_messages:

                        text = message.text.strip()

                        if text:
                            messages.append(text)

                    if messages:

                        validation_text = " | ".join(
                            list(dict.fromkeys(messages))
                        )

                        print(
                            f"Portal validation: "
                            f"{validation_text}"
                        )

                # ==========================================================
                # EXPAND ATTAINMENT
                # ==========================================================

                expand_btn = wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "(//button[@class="
                            "'subject-attainment-tool-item__btn'])[1]"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    expand_btn
                )

                time.sleep(1)

                driver.execute_script(
                    "arguments[0].click();",
                    expand_btn
                )

                time.sleep(2)

                # ==========================================================
                # SELECT SUM
                # ==========================================================

                sum_btn = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//button[normalize-space()='Sum']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    sum_btn
                )

                # ==========================================================
                # IA1
                # ==========================================================

                ia1_row = wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//div[contains(@class,"
                            "'subject-attainment-child-row')]"
                            "[.//*[normalize-space()='IA1']]"
                        )
                    )
                )

                if "is-selected" not in (
                    ia1_row.get_attribute("class")
                ):

                    ia1_button = ia1_row.find_element(
                        By.XPATH,
                        ".//button[contains(@class,"
                        "'subject-attainment-child-row__select')]"
                    )

                    driver.execute_script(
                        "arguments[0].click();",
                        ia1_button
                    )

                # ==========================================================
                # IA2
                # ==========================================================

                ia2_row = wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//div[contains(@class,"
                            "'subject-attainment-child-row')]"
                            "[.//*[normalize-space()='IA2']]"
                        )
                    )
                )

                if "is-selected" not in (
                    ia2_row.get_attribute("class")
                ):

                    ia2_button = ia2_row.find_element(
                        By.XPATH,
                        ".//button[contains(@class,"
                        "'subject-attainment-child-row__select')]"
                    )

                    driver.execute_script(
                        "arguments[0].click();",
                        ia2_button
                    )

                # ==========================================================
                # IA1 MARKS
                # ==========================================================

                ia1_marks = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,"
                            "'subject-attainment-child-row')]"
                            "[.//*[normalize-space()='IA1']]//input"
                        )
                    )
                )

                ia1_marks.clear()

                ia1_marks.send_keys(
                    ia1_marks_value
                )

                assert (
                    ia1_marks.get_attribute("value")
                    == ia1_marks_value
                ), "IA1 Marks mismatch"

                # ==========================================================
                # IA2 MARKS
                # ==========================================================

                ia2_marks = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div[contains(@class,"
                            "'subject-attainment-child-row')]"
                            "[.//*[normalize-space()='IA2']]//input"
                        )
                    )
                )

                ia2_marks.clear()

                ia2_marks.send_keys(
                    ia2_marks_value
                )

                assert (
                    ia2_marks.get_attribute("value")
                    == ia2_marks_value
                ), "IA2 Marks mismatch"

                # ==========================================================
                # EDGE CASE - INVALID IA MARKS
                # ==========================================================

                if invalid_marks:

                    print(
                        f"Testing Invalid IA Marks: "
                        f"{invalid_marks}"
                    )

                    ia1_marks.clear()

                    ia1_marks.send_keys(
                        invalid_marks
                    )

                    actual_invalid_marks = (
                        ia1_marks.get_attribute("value")
                    )

                    if actual_invalid_marks == invalid_marks:

                        ia_validation = driver.find_elements(
                            By.XPATH,
                            validation_xpath
                        )

                        assert ia_validation, (
                            "Invalid IA Marks were accepted "
                            "without validation."
                        )

                    ia1_marks.clear()

                    ia1_marks.send_keys(
                        ia1_marks_value
                    )

                # ==========================================================
                # DONE
                # ==========================================================

                done_btn = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.ID,
                            "attainmentDoneBtn"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    done_btn
                )

                time.sleep(2)

                # ==========================================================
                # SUCCESS
                # ==========================================================

                print(
                    f"PASS: {subject_name_value}"
                )

                results.append({
                    "Test Case": "Subject Configuration",
                    "Test Data": subject_name_value,
                    "Attempt": attempt + 1,
                    "Status": "PASS",
                    "Error": "",
                    "Final Status": "PASS"
                })

                # Stop retry for this Excel row
                break

            # ==========================================================
            # FAILURE / RETRY
            # ==========================================================

            except Exception as e:

                print(
                    f"FAIL: {subject_name_value} "
                    f"| Attempt {attempt + 1}"
                )

                print(
                    f"Error: {e}"
                )

                # ======================================================
                # RETRY
                # ======================================================

                if attempt < 2:

                    print(
                        f"Retrying {subject_name_value}..."
                    )

                    results.append({
                        "Test Case": "Subject Configuration",
                        "Test Data": subject_name_value,
                        "Attempt": attempt + 1,
                        "Status": "FAIL",
                        "Error": str(e),
                        "Final Status": "RETRY"
                    })

                    time.sleep(2)

                # ======================================================
                # FINAL FAILURE
                # ======================================================

                else:

                    print(
                        f"FINAL FAIL: {subject_name_value}"
                    )

                    results.append({
                        "Test Case": "Subject Configuration",
                        "Test Data": subject_name_value,
                        "Attempt": attempt + 1,
                        "Status": "FAIL",
                        "Error": str(e),
                        "Final Status": "FAIL"
                    })

                    # Don't raise.
                    # Continue with next Excel row.
                    break

            # ==========================================================
            # UPDATE EXCEL REPORT AFTER EVERY ATTEMPT
            # ==========================================================

            finally:

                create_report(results)

                print(
                    "Excel summary report updated."
                )

    # ==============================================================
    # FINAL REPORT
    # ==============================================================

    create_report(results)

    print(
        "\n================================================"
    )

    print(
        "ALL SUBJECT TEST CASES COMPLETED"
    )

    print(
        "Excel summary report generated successfully."
    )

    print(
        "================================================"
    )