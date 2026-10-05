from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from excel_reader import get_all_data
from excel_report import create_report
import time


def test_examination(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # EXTERNAL TEST DATA FROM EXCEL
    # ==========================================================

    data_list = get_all_data("Examination")

    results = []

    # ==========================================================
    # LOOP THROUGH ALL EXCEL DATA
    # ==========================================================

    for data in data_list:

        test_case = str(
            data.get("Test Case") or "Examination Create"
        ).strip()

        test_data = str(
            data.get("Test Data") or ""
        ).strip()

        exam_name_value = str(
            data.get("Examination Name") or ""
        ).strip()

        passing_marks_value = str(
            data.get("Passing Marks") or ""
        ).strip()

        subject_category_value = str(
            data.get("Subject Category") or ""
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

        subject_value = str(
            data.get("Subject") or ""
        ).strip()

        attainment_tool_value = str(
            data.get("Attainment Tool") or ""
        ).strip()

        exam_date_value = str(
            data.get("Exam Date") or ""
        ).strip()

        start_time_value = str(
            data.get("Start Time") or ""
        ).strip()

        end_time_value = str(
            data.get("End Time") or ""
        ).strip()

        instructions_value = str(
            data.get("Instructions") or ""
        ).strip()

        validation_value = str(
            data.get("Validation") or ""
        ).strip()

        retry_test = str(
            data.get("Retry Test") or ""
        ).strip().upper()

        # ======================================================
        # QUESTIONS
        # ======================================================

        questions = []

        for i in range(1, 4):

            question_title = str(
                data.get(
                    f"Q{i} Title"
                ) or ""
            ).strip()

            if question_title:

                questions.append({

                    "title": question_title,

                    "type": str(
                        data.get(
                            f"Q{i} Type"
                        ) or ""
                    ).strip(),

                    "marks": str(
                        data.get(
                            f"Q{i} Marks"
                        ) or ""
                    ).strip(),

                    "co": str(
                        data.get(
                            f"Q{i} CO"
                        ) or ""
                    ).strip(),

                    "text": str(
                        data.get(
                            f"Q{i} Text"
                        ) or ""
                    ).strip()
                })

        # ======================================================
        # DETERMINE EDGE CASE
        # ======================================================

        validation_lower = validation_value.lower()

        is_valid_test = validation_lower.startswith(
            "valid examination"
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
                # OPEN EXAMINATION
                # ==================================================

                examination_menu = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//span[normalize-space()='Examination']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    examination_menu
                )

                time.sleep(1)

                ActionChains(driver).move_to_element(
                    examination_menu
                ).click().perform()

                time.sleep(1)

                # ==================================================
                # EXAMINATION SUBMENU
                # ==================================================

                examination_link = wait.until(
                    lambda current_driver: next(
                        (
                            link
                            for link in current_driver.find_elements(
                                By.XPATH,
                                "//a[.='Examination']"
                            )
                            if link.is_displayed()
                            and link.is_enabled()
                        ),
                        False
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    examination_link
                )

                time.sleep(1)

                try:

                    ActionChains(driver).move_to_element(
                        examination_link
                    ).click().perform()

                except Exception:

                    driver.execute_script(
                        "arguments[0].click();",
                        examination_link
                    )

                # ==================================================
                # VERIFY EXAMINATION PAGE
                # ==================================================

                try:

                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (
                                By.ID,
                                "attnAjaxAddRowsBtn"
                            )
                        )
                    )

                except TimeoutException:

                    examination_url = (
                        examination_link.get_attribute("href")
                    )

                    assert examination_url, (
                        "Examination submenu has no URL"
                    )

                    driver.get(examination_url)

                time.sleep(2)

                # ==================================================
                # ADD EXAMINATION
                # ==================================================

                add_button = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.ID,
                            "attnAjaxAddRowsBtn"
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

                # ==================================================
                # EXAMINATION NAME
                # ==================================================

                exam_name = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.NAME,
                            "name"
                        )
                    )
                )

                exam_name.clear()

                exam_name.send_keys(
                    exam_name_value
                )

                actual_exam_name = (
                    exam_name.get_attribute("value")
                )

                assert actual_exam_name == exam_name_value, (
                    f"Examination name mismatch. "
                    f"Expected: '{exam_name_value}', "
                    f"Actual: '{actual_exam_name}'"
                )

                # ==================================================
                # DROPDOWNS
                # ==================================================

                dropdowns = [

                    (1, subject_category_value),

                    (2, branch_value),

                    (3, department_value),

                    (4, program_value),

                    (5, semester_value),

                    (6, subject_value),

                    (7, attainment_tool_value)
                ]

                for number, value in dropdowns:

                    dropdown = wait.until(
                        EC.element_to_be_clickable(
                            (
                                By.XPATH,
                                f"(//div[contains(@class,'nice-select') "
                                f"and contains(@class,'primary_select')])"
                                f"[{number}]"
                            )
                        )
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        dropdown
                    )

                    driver.execute_script(
                        "arguments[0].click();",
                        dropdown
                    )

                    time.sleep(2)

                    option = wait.until(
                        EC.element_to_be_clickable(
                            (
                                By.XPATH,
                                "//div[contains(@class,'nice-select') "
                                "and contains(@class,'open')]"
                                f"//li[normalize-space()='{value}']"
                            )
                        )
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        option
                    )

                    driver.execute_script(
                        "arguments[0].click();",
                        option
                    )

                # ==================================================
                # PASSING MARKS
                # ==================================================

                passing_marks = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.ID,
                            "passing_marks"
                        )
                    )
                )

                passing_marks.clear()

                passing_marks.send_keys(
                    passing_marks_value
                )

                # ==================================================
                # START TIME
                # ==================================================

                start_time = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.ID,
                            "start_time"
                        )
                    )
                )

                start_time.click()

                start_time.send_keys(
                    Keys.CONTROL,
                    "a"
                )

                start_time.send_keys(
                    start_time_value
                )

                # ==================================================
                # END TIME
                # ==================================================

                end_time = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.ID,
                            "end_time"
                        )
                    )
                )

                end_time.click()

                end_time.send_keys(
                    Keys.CONTROL,
                    "a"
                )

                end_time.send_keys(
                    end_time_value
                )

                # ==================================================
                # EXAM DATE
                # ==================================================

                exam_date = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.NAME,
                            "exam_date"
                        )
                    )
                )

                exam_date.click()

                exam_date.send_keys(
                    Keys.CONTROL,
                    "a"
                )

                exam_date.send_keys(
                    exam_date_value
                )

                # ==================================================
                # CONTINUE
                # ==================================================

                continue_button = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.ID,
                            "submitButton"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    continue_button
                )

                time.sleep(1)

                wait.until(
                    lambda d:
                    continue_button.is_displayed()
                    and continue_button.is_enabled()
                )

                print(
                    "Clicking Continue..."
                )

                driver.execute_script(
                    "arguments[0].click();",
                    continue_button
                )

                time.sleep(2)

                # ==================================================
                # EDGE CASE VALIDATION
                # ==================================================

                if is_edge_case:

                    validation_messages = driver.find_elements(
                        By.XPATH,
                        "//*[contains(@class,'invalid-feedback') "
                        "or contains(@class,'text-danger') "
                        "or contains(@class,'error') "
                        "or @role='alert']"
                    )

                    # ----------------------------------------------
                    # DUPLICATE EXAMINATION
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

                        message_text = (
                            all_validation_messages[0]
                            .text
                            .strip()
                        )

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
                    # IF VALIDATION MESSAGE NOT FOUND
                    # ----------------------------------------------

                    else:

                        raise AssertionError(
                            f"Expected validation not displayed "
                            f"for edge case: "
                            f"{validation_value}"
                        )

                # ==================================================
                # VALID EXAMINATION
                # ==================================================

                instruction_box = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "(//div[contains(@class,'note-editable') "
                            "and @contenteditable='true'])[1]"
                        )
                    )
                )

                print(
                    "Continue clicked successfully."
                )

                # ==================================================
                # INSTRUCTIONS
                # ==================================================

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    instruction_box
                )

                time.sleep(1)

                driver.execute_script(
                    "arguments[0].click();",
                    instruction_box
                )

                instruction_box.send_keys(
                    instructions_value
                )

                # ==================================================
                # QUESTIONS
                # ==================================================

                for index, question in enumerate(
                    questions,
                    start=1
                ):

                    # ==============================================
                    # ADD QUESTION
                    # ==============================================

                    if index > 1:

                        add_question = wait.until(
                            EC.element_to_be_clickable(
                                (
                                    By.XPATH,
                                    "//button[@id='add-question-btn']"
                                )
                            )
                        )

                        driver.execute_script(
                            "arguments[0].scrollIntoView({block:'center'});",
                            add_question
                        )

                        driver.execute_script(
                            "arguments[0].click();",
                            add_question
                        )

                        time.sleep(1)

                    # ==============================================
                    # QUESTION TITLE
                    # ==============================================

                    question_title = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                f"(//input[contains(@class,'q-title')])"
                                f"[{index}]"
                            )
                        )
                    )

                    question_title.clear()

                    question_title.send_keys(
                        question["title"]
                    )

                    # ==============================================
                    # QUESTION TYPE
                    # ==============================================

                    question_type = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                f"(//select[contains(@class,'q-type')])"
                                f"[{index}]"
                            )
                        )
                    )

                    Select(
                        question_type
                    ).select_by_visible_text(
                        question["type"]
                    )

                    # ==============================================
                    # QUESTION MARKS
                    # ==============================================

                    question_marks = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                f"(//input[contains(@class,'q-marks')])"
                                f"[{index}]"
                            )
                        )
                    )

                    question_marks.clear()

                    question_marks.send_keys(
                        question["marks"]
                    )

                    # ==============================================
                    # CO
                    # ==============================================

                    question_co = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                f"(//select[contains(@class,'q-co')])"
                                f"[{index}]"
                            )
                        )
                    )

                    Select(
                        question_co
                    ).select_by_visible_text(
                        question["co"]
                    )

                    # ==============================================
                    # QUESTION TEXT
                    # ==============================================

                    question_editor = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                f"(//div[contains(@class,'note-editable') "
                                f"and @contenteditable='true'])"
                                f"[{index + 1}]"
                            )
                        )
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        question_editor
                    )

                    driver.execute_script(
                        "arguments[0].click();",
                        question_editor
                    )

                    question_editor.send_keys(
                        question["text"]
                    )

                # ==================================================
                # FINAL SAVE
                # ==================================================

                save_button = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.ID,
                            "submitButton"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    save_button
                )

                driver.execute_script(
                    "arguments[0].click();",
                    save_button
                )

                time.sleep(3)

                # ==================================================
                # SUCCESS
                # ==================================================

                print(
                    f"PASS: {exam_name_value} | "
                    f"Questions: {len(questions)}"
                )

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
                    f"FAIL: {exam_name_value} "
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
                        f"Retrying {exam_name_value}..."
                    )

                    results.append({

                        "Test Case":
                            test_case,

                        "Test Data":
                            test_data,

                        "Edge Case":
                            "YES" if is_edge_case else "NO",

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
                        f"FINAL FAIL: "
                        f"{exam_name_value}"
                    )

                    results.append({

                        "Test Case":
                            test_case,

                        "Test Data":
                            test_data,

                        "Edge Case":
                            "YES" if is_edge_case else "NO",

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
        "ALL EXAMINATION TEST CASES COMPLETED"
    )

    print(
        "Excel report generated successfully."
    )

    print(
        "================================================"
    )