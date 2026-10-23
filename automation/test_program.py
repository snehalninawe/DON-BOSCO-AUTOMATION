from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


def test_program(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "STU Marol(east) Mumbai 400002"
    department_value = "IT-26"
    program_name_value = "BTECH Program"
    duration_value = "3"
    type_value = "Full time"
    program_head_value = "abc abc (Admin)"

    # ---------------- EDIT DATA ----------------

    edit_program_name = "BTECH Program-1"
    edit_duration = "4"

    # ---------------- EDGE CASE DATA ----------------

    empty_program_name = ""
    empty_duration = ""

    long_program_name = (
        "BTECH Program Long Name For Boundary Validation Testing"
    )

    invalid_duration = "ABC"
    negative_duration = "-1"
    zero_duration = "0"

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

    # ==========================================================
    # PROGRAM
    # ==========================================================

    program = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Program']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        program
    )

    driver.execute_script(
        "arguments[0].click();",
        program
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
        "arguments[0].click();",
        add_button
    )

    time.sleep(1)

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
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//li[contains("
                "translate(normalize-space(),"
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                "'abcdefghijklmnopqrstuvwxyz'),"
                f"'{branch_value.lower()}')]"
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

    # Verify selected branch
    selected_branch = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[1]"
                "//span[@class='current']"
            )
        )
    )

    assert (
        selected_branch.text.strip().lower()
        == branch_value.lower()
    ), (
        f"Branch mismatch. Expected: '{branch_value}', "
        f"Actual: '{selected_branch.text.strip()}'"
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

    # Verify selected department
    selected_department = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[2]"
                "//span[@class='current']"
            )
        )
    )

    assert (
        selected_department.text.strip()
        == department_value
    )

    # ==========================================================
    # PROGRAM NAME
    # ==========================================================

    program_name = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "name"
            )
        )
    )

    program_name.clear()
    program_name.send_keys(program_name_value)

    assert (
        program_name.get_attribute("value")
        == program_name_value
    )

    # ==========================================================
    # DURATION
    # ==========================================================

    duration = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "duration_year"
            )
        )
    )

    duration.clear()
    duration.send_keys(duration_value)

    assert (
        duration.get_attribute("value")
        == duration_value
    )

    # ==========================================================
    # TYPE DROPDOWN
    # ==========================================================

    type_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[3]"
            )
        )
    )

    type_dropdown.click()

    type_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{type_value}']"
            )
        )
    )

    type_option.click()

    # Verify type
    selected_type = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[3]"
                "//span[@class='current']"
            )
        )
    )

    assert (
        selected_type.text.strip().lower()
        == type_value.lower()
    ), (
        f"Type mismatch. Expected: '{type_value}', "
        f"Actual: '{selected_type.text.strip()}'"
    )

    # ==========================================================
    # PROGRAM HEAD
    # ==========================================================

    program_head_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[4]"
            )
        )
    )

    program_head_dropdown.click()

    program_head_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{program_head_value}']"
            )
        )
    )

    program_head_option.click()

    # Verify program head
    selected_program_head = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[4]"
                "//span[@class='current']"
            )
        )
    )

    assert (
    selected_program_head.text.strip().lower()
    == program_head_value.lower()
), (
    f"Program Head mismatch. "
    f"Expected: '{program_head_value}', "
    f"Actual: '{selected_program_head.text.strip()}'"
)

    # ==========================================================
    # EDGE CASE - EMPTY PROGRAM NAME
    # ==========================================================

    program_name.clear()

    assert (
        program_name.get_attribute("value")
        == empty_program_name
    )

    # Restore valid value
    program_name.send_keys(program_name_value)

    # ==========================================================
    # EDGE CASE - EMPTY DURATION
    # ==========================================================

    duration.clear()

    assert (
        duration.get_attribute("value")
        == empty_duration
    )

    # Restore valid duration
    duration.send_keys(duration_value)

    # ==========================================================
    # EDGE CASE - LONG PROGRAM NAME
    # ==========================================================

    program_name.clear()
    program_name.send_keys(long_program_name)

    actual_long_name = program_name.get_attribute("value")

    # Do not assume maxlength behavior.
    # Verify that the application accepts or restricts the value.
    assert actual_long_name == long_program_name, (
        f"Unexpected program name value. "
        f"Expected: '{long_program_name}', "
        f"Actual: '{actual_long_name}'"
    )

    # Restore valid name
    program_name.clear()
    program_name.send_keys(program_name_value)

        # ==========================================================
    # EDGE CASE - INVALID DURATION
    # ==========================================================

    duration.clear()
    duration.send_keys(invalid_duration)

    actual_invalid_duration = duration.get_attribute("value")

    # Verify invalid data is entered for negative testing
    assert actual_invalid_duration == invalid_duration, (
        f"Unable to enter invalid duration test data. "
        f"Expected: '{invalid_duration}', "
        f"Actual: '{actual_invalid_duration}'"
    )

    # Submit invalid data
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

    time.sleep(2)

    # Verify validation message
    validation_message = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(@class,'invalid-feedback') "
                "or contains(@class,'error') "
                "or contains(@class,'text-danger')]"
            )
        )
    )

    assert validation_message.is_displayed(), (
        "Expected validation message for invalid duration, "
        "but no validation message was displayed."
    )

    # ==========================================================
    # EDGE CASE - NEGATIVE DURATION
    # ==========================================================

    duration.clear()
    duration.send_keys(negative_duration)

    actual_negative_duration = duration.get_attribute("value")

    assert actual_negative_duration in ["", "-1"], (
        f"Unexpected negative duration behavior: "
        f"'{actual_negative_duration}'"
    )

    # Restore valid duration
    duration.clear()
    duration.send_keys(duration_value)

    # ==========================================================
    # EDGE CASE - ZERO DURATION
    # ==========================================================

    duration.clear()
    duration.send_keys(zero_duration)

    actual_zero_duration = duration.get_attribute("value")

    assert actual_zero_duration == zero_duration, (
        f"Unexpected zero duration behavior: "
        f"'{actual_zero_duration}'"
    )

    # Restore valid duration
    duration.clear()
    duration.send_keys(duration_value)

    # ==========================================================
    # SUBMIT
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

    time.sleep(3)

    # ==========================================================
    # VERIFY PROGRAM CREATED / ACTION BUTTON AVAILABLE
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

    # ==========================================================
    # EDIT
    # ==========================================================

    edit_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[contains(translate(.,"
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                "'abcdefghijklmnopqrstuvwxyz'),'edit')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        edit_button
    )

    # ==========================================================
    # EDIT PROGRAM NAME
    # ==========================================================

    program_name = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "name"
            )
        )
    )

    program_name.clear()
    program_name.send_keys(edit_program_name)

    assert (
        program_name.get_attribute("value")
        == edit_program_name
    )

    # ==========================================================
    # EDIT DURATION
    # ==========================================================

    duration = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "duration_year"
            )
        )
    )

    duration.clear()
    duration.send_keys(edit_duration)

    assert (
        duration.get_attribute("value")
        == edit_duration
    )

    # ==========================================================
    # SAVE EDIT
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

    # ==========================================================
    # DELETE
    # ==========================================================

    delete_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[contains(@class,'delete-button-datatable') "
                "or contains(translate(.,"
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                "'abcdefghijklmnopqrstuvwxyz'),'delete')])[1]"
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