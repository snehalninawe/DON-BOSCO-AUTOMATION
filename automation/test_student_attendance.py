from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.keys import Keys


# ==========================================================
# EXTERNAL TEST DATA
# ==========================================================

subject_category_value = "Department"

branch_value = "RTM,Marol(West),Mumbai-400021"
department_value = "CSE-2026"
program_value = "new-btech"
semester_value = "Sem-3(CSE)"
semester_label_value = "Sem-3-cse-label"
section_value = "CSE-Section A"

subject_value = "Computer network"

attendance_date_value = "20/08/2026"

start_time_value = "10:00 AM"
end_time_value = "11:00 AM"

unit_value = "DevOps"
topic_value = "monitoring"
topic_status_value = "In Progress"


def test_student_attendance(driver):

    wait = WebDriverWait(driver, 15)

    # ==========================================================
    # OPEN STUDENT INFO
    # ==========================================================

    student_info_menu = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div//span[normalize-space()='Student Info']"
            )
        )
    )

    student_info_menu.click()

    # ==========================================================
    # OPEN SUBJECT WISE ATTENDANCE
    # ==========================================================

    student_attendance = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Subject Wise Attendance')])[2]"
            )
        )
    )

    student_attendance.click()

    # ==========================================================
    # ADD BUTTON
    # ==========================================================

    add_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "attnAjaxAddRowsBtn"
            )
        )
    )

    add_button.click()

        # ==========================================================
    # SUBJECT CATEGORY
    # ==========================================================

    subject_category_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select') and "
                "contains(@class,'form-control')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        subject_category_dropdown
    )

    subject_category_dropdown.click()

    # Wait until the dropdown is actually OPEN
    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select') and "
                "contains(@class,'form-control')])[1]"
                "[contains(@class,'open')]"
            )
        )
    )

    # Locate option only after dropdown is opened
    subject_category_option = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') and contains(@class,'open')]"
                "//li[normalize-space()='%s']" % subject_category_value
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        subject_category_option
    )

    driver.execute_script(
        "arguments[0].click();",
        subject_category_option
    )

    # Verify selected value
    selected_subject_category = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select') and "
                "contains(@class,'form-control')])[1]"
                "//span[contains(@class,'current')]"
            )
        )
    )

    assert selected_subject_category.text.strip() == subject_category_value, (
        f"Subject Category selection failed. "
        f"Expected: '{subject_category_value}', "
        f"Actual: '{selected_subject_category.text.strip()}'"
)

    # ==========================================================
    # BRANCH
    # ==========================================================

    branch_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select')])[2]"
            )
        )
    )

    branch_dropdown.click()

    branch_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{branch_value}']"
            )
        )
    )

    driver.execute_script(
            "arguments[0].click();",
            branch_option
        )

    # ==========================================================
    # DEPARTMENT
    # ==========================================================

    department_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select')])[3]"
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
                f"//li[normalize-space()='{department_value}']"
            )
        )
    )

    driver.execute_script(
                    "arguments[0].click();",
                    department_option
                )

    # ==========================================================
    # PROGRAM
    # ==========================================================

    program_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select')])[4]"
            )
        )
    )

    program_dropdown.click()

    program_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{program_value}']"
            )
        )
    )

    program_option.click()

    # ==========================================================
    # SEMESTER
    # ==========================================================

    semester_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select')])[5]"
            )
        )
    )

    semester_dropdown.click()

    semester_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{semester_value}']"
            )
        )
    )

    semester_option.click()

    # ==========================================================
    # SEMESTER LABEL
    # ==========================================================

    semester_label_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select')])[6]"
            )
        )
    )

    semester_label_dropdown.click()

    semester_label_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{semester_label_value}']"
            )
        )
    )

    semester_label_option.click()

    # ==========================================================
    # SECTION
    # ==========================================================

    section_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select')])[7]"
            )
        )
    )

    section_dropdown.click()

    section_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{section_value}']"
            )
        )
    )

    section_option.click()

    # ==========================================================
    # SUBJECT
    # ==========================================================

    subject_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select')])[8]"
            )
        )
    )

    subject_dropdown.click()

    subject_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{subject_value}']"
            )
        )
    )

    subject_option.click()

        # ==========================================================
    # ATTENDANCE DATE
    # ==========================================================

    attendance_date = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "attendance_date"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        attendance_date
    )

    attendance_date.click()

    time.sleep(1)

    attendance_day = attendance_date_value.split("/")[0]

    date = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//td[contains(@class,'day') "
                f"and normalize-space()='{attendance_day}' "
                f"and not(contains(@class,'old')) "
                f"and not(contains(@class,'new'))]"
            )
        )
    )

    date.click()

    time.sleep(1)

    assert attendance_date.get_attribute("value") == \
        attendance_date_value, \
        "Attendance date was not entered correctly"

        # ==========================================================
    # START TIME
    # ==========================================================

    start_time = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "start_time")
        )
    )

    start_time.click()
    start_time.send_keys(Keys.CONTROL, "a")
    start_time.send_keys(start_time_value)
    start_time.send_keys(Keys.TAB)

    time.sleep(1)


    # ==========================================================
    # END TIME
    # ==========================================================

    end_time = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "end_time")
        )
    )

    end_time.click()
    end_time.send_keys(Keys.CONTROL, "a")
    end_time.send_keys(end_time_value)
    end_time.send_keys(Keys.TAB)

    time.sleep(1)

    # ==========================================================
    # UNIT
    # ==========================================================

    unit_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') and "
                "contains(@class,'primary_select')])[10]"
            )
        )
    )

    unit_dropdown.click()

    unit_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{unit_value}']"
            )
        )
    )

    unit_option.click()

    # ==========================================================
    # TOPIC MULTI-SELECT
    # ==========================================================

    topic_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'ms-options-wrap')]"
            )
        )
    )

    topic_dropdown.click()

    topic_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[contains(normalize-space(),'{topic_value}')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        topic_option
    )

    topic_option.click()

    # ==========================================================
    # TOPIC STATUS
    # ==========================================================

    topic_status_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'topic-status-select')]"
            )
        )
    )

    topic_status_dropdown.click()

    topic_status_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{topic_status_value}']"
            )
        )
    )

    topic_status_option.click()

    # ==========================================================
    # MARK ATTENDANCE
    # ==========================================================

    mark_attendance_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "submitButton"
            )
        )
    )

    mark_attendance_button.click()

        # ------------------ PRESENT CHECKMARK ------------------

    present_radio = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[contains(@class,'common-radio') "
                "and contains(@class,'attendanceP') "
                "and contains(@class,'subject_attendance_type')]"
            )
        )
    )

    # Click the associated label instead of the hidden input
    present_label = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[contains(@class,'common-radio') "
                "and contains(@class,'attendanceP') "
                "and contains(@class,'subject_attendance_type')]"
                "/following-sibling::label"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        present_label
    )

    present_label.click()

    # Verify radio is selected
    wait.until(
        lambda d: present_radio.is_selected()
    )

    assert present_radio.is_selected(), "Present attendance was not selected"
    
    
    #----------SAVE BUTTON-------
    save = driver.find_element(By.ID,"submitButton")
    save.click()