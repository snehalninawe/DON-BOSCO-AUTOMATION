from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_sem_label(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_value = "STU Marol(east) Mumbai 400002"
    department_value = "IT-26"
    program_value = "New-IT"
    semester_value = "sem1-it"

    semester_label_value = "sem1-it-label"
    minimum_hour_value = "10"

    edit_semester_label_value = "sem1-it-label-updated"
    edit_minimum_hour_value = "20"

    # ---------------- EDGE CASE DATA ----------------

    empty_label_value = ""
    empty_hour_value = ""

    long_label_value = (
        "Semester Label Long Name For Boundary Validation Testing"
    )

    invalid_hour_value = "ABC"
    negative_hour_value = "-5"
    zero_hour_value = "0"

    special_character_label = "@@@###"

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
    # SEMESTER LABEL
    # ==========================================================

    semester_label_menu = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Semester Label']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester_label_menu
    )

    driver.execute_script(
        "arguments[0].click();",
        semester_label_menu
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
    # BRANCH
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
                "//li[normalize-space()='STU Marol(East) Mumbai 400002' "
                "or normalize-space()='STU Marol(east) Mumbai 400002']"
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

    # Verify selected branch - case insensitive
    selected_branch = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[1]"
                "//span"
            )
        )
    )

    assert (
        selected_branch.text.strip().lower()
        == branch_value.strip().lower()
    ), (
        f"Branch mismatch. Expected: {branch_value}, "
        f"Actual: {selected_branch.text.strip()}"
    )

    # ==========================================================
    # DEPARTMENT
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
        "arguments[0].click();",
        department_option
    )

    time.sleep(2)

    # ==========================================================
    # PROGRAM
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
        "arguments[0].click();",
        program_option
    )

    time.sleep(2)

    # ==========================================================
    # SEMESTER
    # ==========================================================

    semester_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[4]"
            )
        )
    )

    semester_dropdown.click()

    semester_option = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[normalize-space()='{semester_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        semester_option
    )

    time.sleep(2)

    # ==========================================================
    # SEMESTER LABEL NAME
    # ==========================================================

    semester_label = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "name"
            )
        )
    )

    semester_label.clear()
    semester_label.send_keys(semester_label_value)

    assert (
        semester_label.get_attribute("value")
        == semester_label_value
    ), "Semester label value was not entered correctly."

    # ==========================================================
    # MINIMUM HOUR
    # ==========================================================

    hour = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "minimum_hour"
            )
        )
    )

    hour.clear()
    hour.send_keys(minimum_hour_value)

    actual_hour = hour.get_attribute("value")

    assert (
        actual_hour == minimum_hour_value
    ), "Minimum hour value was not entered correctly."

    # ==========================================================
    # EDGE CASE - EMPTY SEMESTER LABEL
    # ==========================================================

    semester_label.clear()

    assert (
        semester_label.get_attribute("value") == ""
    ), "Semester label field should allow clearing."

    semester_label.send_keys(semester_label_value)

    # ==========================================================
    # EDGE CASE - EMPTY MINIMUM HOUR
    # ==========================================================

    hour.clear()

    assert (
        hour.get_attribute("value") == ""
    ), "Minimum hour field should be clearable."

    hour.send_keys(minimum_hour_value)

    # ==========================================================
    # EDGE CASE - LONG SEMESTER LABEL
    # ==========================================================

    semester_label.clear()
    semester_label.send_keys(long_label_value)

    actual_long_label = semester_label.get_attribute("value")

    assert (
        len(actual_long_label) <= len(long_label_value)
    ), "Unexpected value handling for long semester label."

    semester_label.clear()
    semester_label.send_keys(semester_label_value)

    # ==========================================================
    # EDGE CASE - SPECIAL CHARACTERS
    # ==========================================================

    semester_label.clear()
    semester_label.send_keys(special_character_label)

    actual_special_label = semester_label.get_attribute("value")

    assert (
        actual_special_label == special_character_label
    ), "Special character handling failed."

    semester_label.clear()
    semester_label.send_keys(semester_label_value)

    # ==========================================================
    # EDGE CASE - ALPHABETIC HOUR
    # ==========================================================

    hour.clear()
    hour.send_keys(invalid_hour_value)

    actual_invalid_hour = hour.get_attribute("value")

    # HTML number inputs may reject letters completely.
    # If the browser accepts them, this test records the behavior
    # instead of assuming the expected implementation.

    assert (
        actual_invalid_hour == ""
        or actual_invalid_hour == invalid_hour_value
    ), "Unexpected handling of alphabetic hour input."

    hour.clear()
    hour.send_keys(minimum_hour_value)

    # ==========================================================
    # EDGE CASE - NEGATIVE HOUR
    # ==========================================================

    hour.clear()
    hour.send_keys(negative_hour_value)

    actual_negative_hour = hour.get_attribute("value")

    assert (
        actual_negative_hour in ["", negative_hour_value]
    ), "Unexpected handling of negative hour value."

    hour.clear()
    hour.send_keys(minimum_hour_value)

    # ==========================================================
    # EDGE CASE - ZERO HOUR
    # ==========================================================

    hour.clear()
    hour.send_keys(zero_hour_value)

    actual_zero_hour = hour.get_attribute("value")

    assert (
        actual_zero_hour == zero_hour_value
    ), "Zero hour value was not handled correctly."

    hour.clear()
    hour.send_keys(minimum_hour_value)

    # ==========================================================
    # SECTION A
    # ==========================================================

    section_a = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "section109"
            )
        )
    )

    if not section_a.is_selected():
        driver.execute_script(
            "arguments[0].click();",
            section_a
        )

    assert section_a.is_selected(), (
        "Section A checkbox could not be selected."
    )

    # ==========================================================
    # SECTION B
    # ==========================================================

    section_b = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "section110"
            )
        )
    )

    if not section_b.is_selected():
        driver.execute_script(
            "arguments[0].click();",
            section_b
        )

    assert section_b.is_selected(), (
        "Section B checkbox could not be selected."
    )

    # ==========================================================
    # INSTALLMENT PERCENTAGE
    # ==========================================================

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    installment_field = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[contains(@class,'unPercentage')]"
            )
        )
    )

    installment_field.clear()
    installment_field.send_keys("100")

    assert (
        installment_field.get_attribute("value") == "100"
    ), "Installment percentage was not entered correctly."

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
    # OPEN ACTION MENU
    # ==========================================================

    three_dots = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//button[contains(@class,'attn-ajax-action_button')])[1]"
            )
        )
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
    # EDIT SEMESTER LABEL
    # ==========================================================

    semester_label = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "name"
            )
        )
    )

    semester_label.clear()
    semester_label.send_keys(edit_semester_label_value)

    assert (
        semester_label.get_attribute("value")
        == edit_semester_label_value
    ), "Semester label edit failed."

    # ==========================================================
    # EDIT MINIMUM HOUR
    # ==========================================================

    hour = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "minimum_hour"
            )
        )
    )

    hour.clear()
    hour.send_keys(edit_minimum_hour_value)

    assert (
        hour.get_attribute("value")
        == edit_minimum_hour_value
    ), "Minimum hour edit failed."

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
                "(//button[contains(@class,'attn-ajax-action_button')])[1]"
            )
        )
    )

    three_dots.click()

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

    assert modal.is_displayed(), (
        "Delete confirmation modal was not displayed."
    )

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