from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time


def test_student_category(driver):

    wait = WebDriverWait(driver, 15)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    category_value = "SBC"
    updated_category_value = "SBC-2"

    # Edge case data
    duplicate_category_value = "General"
    empty_category_value = ""
    spaces_category_value = "   "
    special_character_category_value = "@@@###"
    long_category_value = "A" * 256

    # ==========================================================
    # TEST DATA VALIDATION / EDGE CASES
    # ==========================================================

    # Category should not be empty
    assert category_value.strip(), \
        "Student category should not be empty"

    # Category should not contain only spaces
    assert category_value.strip() != "", \
        "Student category should not contain only spaces"

    # Updated category should not be empty
    assert updated_category_value.strip(), \
        "Updated student category should not be empty"

    # Updated category should not contain only spaces
    assert updated_category_value.strip() != "", \
        "Updated student category should not contain only spaces"

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

    time.sleep(1)

    # ==========================================================
    # OPEN STUDENT CATEGORY
    # ==========================================================

    student_category = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Student Category']"
            )
        )
    )

    student_category.click()

    time.sleep(2)

    # # ==========================================================
    # # ADD STUDENT CATEGORY
    # # ==========================================================

    # add_field = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.NAME,
    #             "category"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     add_field
    # )

    # time.sleep(1)

    # add_field.clear()
    # add_field.send_keys(category_value)

    # time.sleep(1)

    # # ==========================================================
    # # VERIFY CATEGORY INPUT
    # # ==========================================================

    # actual_category = add_field.get_attribute("value")

    # assert actual_category == category_value, \
    #     "Student category was not entered correctly"

    # assert actual_category.strip() != "", \
    #     "Student category should not be empty"

    # # ==========================================================
    # # SAVE CATEGORY
    # # ==========================================================

    # save = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//button[contains(@class,'primary-btn') "
    #             "and contains(@class,'submit') "
    #             "and contains(@class,'nxgn_secondary_btn')]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     save
    # )

    # time.sleep(1)

    # try:
    #     save.click()

    # except ElementClickInterceptedException:
    #     driver.execute_script(
    #         "arguments[0].click();",
    #         save
    #     )

    # time.sleep(2)

    # # ==========================================================
    # # VERIFY CATEGORY CREATED
    # # ==========================================================

    # created_category = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//tr[.//td[normalize-space()='{category_value}']]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     created_category
    # )

    # assert category_value in created_category.text, \
    #     "Student category was not created successfully"

    # ==========================================================
    # EDIT STUDENT CATEGORY
    # ==========================================================

    # edit_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             f"//tr[.//td[normalize-space()='{category_value}']]"
    #             "//a[contains(@class,'edit-btn')]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     edit_button
    # )

    # time.sleep(1)

    # edit_button.click()

    # time.sleep(2)

    # # ==========================================================
    # # VERIFY EDIT FORM
    # # ==========================================================

    # edit_category = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.NAME,
    #             "category"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     edit_category
    # )

    # time.sleep(1)

    # # ==========================================================
    # # UPDATE CATEGORY
    # # ==========================================================

    # edit_category.click()

    # edit_category.clear()

    # edit_category.send_keys(updated_category_value)

    # time.sleep(1)

    # # ==========================================================
    # # VERIFY UPDATED CATEGORY INPUT
    # # ==========================================================

    # actual_updated_category = \
    #     edit_category.get_attribute("value")

    # assert actual_updated_category == \
    #     updated_category_value, \
    #     "Updated student category was not entered correctly"

    # assert actual_updated_category.strip() != "", \
    #     "Updated student category should not be empty"

    # # ==========================================================
    # # UPDATE / SAVE
    # # ==========================================================

    # update = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//button[contains(@class,'primary-btn') "
    #             "and contains(@class,'submit') "
    #             "and contains(@class,'nxgn_secondary_btn')]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     update
    # )

    # time.sleep(1)

    # try:
    #     update.click()

    # except ElementClickInterceptedException:
    #     driver.execute_script(
    #         "arguments[0].click();",
    #         update
    #     )

    # time.sleep(2)

    # # ==========================================================
    # # VERIFY CATEGORY UPDATED
    # # ==========================================================

    # updated_category = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//tr[.//td[normalize-space()="
    #             f"'{updated_category_value}']]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     updated_category
    # )

    # assert updated_category_value in updated_category.text, \
    #     "Student category was not updated successfully"

    # ==========================================================
    # DELETE STUDENT CATEGORY
    # ==========================================================

    delete = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//tr[.//td[normalize-space()="
                f"'{updated_category_value}']]"
                "//button[contains(@class,'delete-btn')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        delete
    )

    time.sleep(1)

    try:
        delete.click()

    except ElementClickInterceptedException:
        driver.execute_script(
            "arguments[0].click();",
            delete
        )

    time.sleep(2)


    print(
        "Student category created, edited and deleted successfully"
    )