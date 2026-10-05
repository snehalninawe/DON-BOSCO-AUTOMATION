from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_branch(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    branch_name_value = "Test Branch"
    dean_value = "Deepika Gupta (Teacher)"
    email_value = "deepika@gmail.com"

    # EDIT DATA
    edit_branch_name = "Test Branch Updated"
    edit_email = "deepikagupta@gmail.com"

    # EDGE CASE DATA
    blank_branch_name = ""
    spaces_branch_name = "     "
    special_branch_name = "Branch@#$%"
    numeric_branch_name = "12345"
    long_branch_name = "Branch-" + ("A" * 100)

    invalid_email = "deepika@"
    blank_email = ""

    # ==========================================================
    # UNIVERSITY
    # ==========================================================

    university = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div//span[normalize-space()='University']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        university
    )

    time.sleep(1)

    # ==========================================================
    # BRANCH
    # ==========================================================

    branch = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[normalize-space()='Branch']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        branch
    )

    time.sleep(2)

    # ==========================================================
    # ADD BRANCH
    # ==========================================================

    # add_button = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//a[contains(@class,'nxgn_primary_button') "
    #             "and contains(@class,'button_bg_primary')]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     add_button
    # )

    # time.sleep(1)

    # # ==========================================================
    # # BRANCH NAME
    # # ==========================================================

    # branch_name = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Branch Name']"
    #         )
    #     )
    # )

    # branch_name.click()
    # branch_name.clear()
    # branch_name.send_keys(branch_name_value)

    # # ==========================================================
    # # DEAN DROPDOWN
    # # ==========================================================

    # dean = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     dean
    # )

    # time.sleep(1)

    # dean_option = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//li[normalize-space()='{dean_value}']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     dean_option
    # )

    # # ==========================================================
    # # EMAIL
    # # ==========================================================

    # email = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.NAME,
    #             "email"
    #         )
    #     )
    # )

    # email.click()
    # email.clear()
    # email.send_keys(email_value)

    # # ==========================================================
    # # SUBMIT
    # # ==========================================================

    # submit_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "submitButton"
    #         )
    #     )
    # )

    # submit_button.click()

    # time.sleep(2)

    # # ==========================================================
    # # VERIFY BRANCH CREATED
    # # ==========================================================

    # wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//*[contains(normalize-space(),"
    #             f"'{branch_name_value}')]"
    #         )
    #     )
    # )

    # assert branch_name_value in driver.page_source
    # assert email_value in driver.page_source

    # ==========================================================
    # THREE DOTS
    # ==========================================================

    # three_dots = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//button[contains(@class,"
    #             "'attn-ajax-action_button')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     three_dots
    # )

    # # ==========================================================
    # # EDIT
    # # ==========================================================

    # edit_button = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//a[contains("
    #             "translate(normalize-space(),"
    #             "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
    #             "'abcdefghijklmnopqrstuvwxyz'),"
    #             "'edit')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     edit_button
    # )

    # time.sleep(1)

    # # ==========================================================
    # # EDIT BRANCH NAME
    # # ==========================================================

    # branch_name = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Branch Name']"
    #         )
    #     )
    # )

    # branch_name.click()
    # branch_name.clear()
    # branch_name.send_keys(edit_branch_name)

    # # ==========================================================
    # # EDIT DEAN
    # # ==========================================================

    # dean = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[1]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     dean
    # )

    # time.sleep(1)

    # dean_option = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//li[normalize-space()='{dean_value}']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].click();",
    #     dean_option
    # )

    # # ==========================================================
    # # EDIT EMAIL
    # # ==========================================================

    # email = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.NAME,
    #             "email"
    #         )
    #     )
    # )

    # email.click()
    # email.clear()
    # email.send_keys(edit_email)

    # # ==========================================================
    # # SAVE EDIT
    # # ==========================================================

    # submit_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "submitButton"
    #         )
    #     )
    # )

    # submit_button.click()

    # time.sleep(2)

    # # ==========================================================
    # # VERIFY EDIT
    # # ==========================================================

    # wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//*[contains(normalize-space(),"
    #             f"'{edit_branch_name}')]"
    #         )
    #     )
    # )

    # assert edit_branch_name in driver.page_source
    # assert edit_email in driver.page_source

    # ==========================================================
    # THREE DOTS FOR DELETE
    # ==========================================================

    three_dots = wait.until(
        EC.presence_of_element_located(
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
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//a[contains("
                "translate(normalize-space(),"
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                "'abcdefghijklmnopqrstuvwxyz'),"
                "'delete')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        delete_button
    )

    time.sleep(1)

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
        EC.presence_of_element_located(
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
    # VERIFY DELETE
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

    assert edit_branch_name not in driver.page_source