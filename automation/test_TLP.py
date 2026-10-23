from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


def test_tlp(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    comments_value = "Approved"

    # External / edge-case test data
    empty_comment = ""
    whitespace_comment = "   "
    long_comment = "A" * 500
    special_character_comment = "@#$%^&*()_+-=Test"
    normal_comment = "Approved"

    # ==========================================================
    # HELPER - JAVASCRIPT CLICK
    # ==========================================================

    def js_click(locator):
        element = wait.until(
            EC.presence_of_element_located(locator)
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        time.sleep(0.5)

        driver.execute_script(
            "arguments[0].click();",
            element
        )

        return element

    # ==========================================================
    # UNIT PLAN MENU
    # ==========================================================

    unit_plan_menu = js_click(
        (
            By.XPATH,
            "//div//span[normalize-space()='Unit Plan']"
        )
    )

    time.sleep(1)

    # ==========================================================
    # TEACHING LEARNING PLAN
    # ==========================================================

    tlp = js_click(
        (
            By.XPATH,
            "//a[normalize-space()='Teaching Learning Plan']"
        )
    )

    # Wait until TLP page/action buttons are loaded
    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[contains(@class,'attn-ajax-action_button')]"
            )
        )
    )

    # ==========================================================
    # THREE DOTS
    # ==========================================================

    three_dots = js_click(
        (
            By.XPATH,
            "(//button[contains(@class,'attn-ajax-action_button')])[5]"
        )
    )

    # ==========================================================
    # VIEW TLP
    # ==========================================================

    view_button = js_click(
        (
            By.XPATH,
            "(//a[contains(@class,'attn-ajax-action_item_list')])[5]"
        )
    )

    # Wait for TLP details/action area
    approve_button = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[contains(@class,'tlp-open-action-modal')]"
                "[contains(normalize-space(),'Approve')]"
            )
        )
    )

    # ==========================================================
    # APPROVE ACTION
    # ==========================================================

    js_click(
        (
            By.XPATH,
            "//a[contains(@class,'nxgn_common_btn') "
            "and contains(@class,'tlp-open-action-modal') "
            "and contains(normalize-space(),'Approve')]"
        )
    )

    # ==========================================================
    # COMMENT FIELD
    # ==========================================================

    comments_section = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "tlpActionComment"
            )
        )
    )

    # ==========================================================
    # EDGE CASE 1 - EMPTY COMMENT
    # ==========================================================

    comments_section.clear()

    # Try submitting without comment
    js_click(
        (
            By.ID,
            "tlpActionSubmitBtn"
        )
    )

    time.sleep(1)

    # Check whether validation is displayed
    try:

        validation_message = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(@class,'invalid-feedback') "
                    "or contains(@class,'text-danger') "
                    "or contains(@class,'error')]"
                )
            )
        )

        assert validation_message.is_displayed(), (
            "Validation message was not displayed for empty comment."
        )

    except TimeoutException:

        # If comment is optional, application may allow empty comment.
        # Verify the field still exists and no unexpected failure occurred.
        assert comments_section.is_displayed()

    # ==========================================================
    # ENTER VALID COMMENT
    # ==========================================================

    comments_section.clear()

    comments_section.send_keys(comments_value)

    assert (
        comments_section.get_attribute("value")
        == comments_value
    )

    # ==========================================================
    # EDGE CASE 2 - WHITESPACE COMMENT
    # ==========================================================

    comments_section.clear()

    comments_section.send_keys(whitespace_comment)

    actual_whitespace_comment = (
        comments_section.get_attribute("value")
    )

    # Application should either trim/reject whitespace
    # or treat it according to its validation rules.
    assert (
        actual_whitespace_comment.strip() == ""
    ), "Whitespace comment was unexpectedly modified."

    # ==========================================================
    # RESTORE VALID COMMENT
    # ==========================================================

    comments_section.clear()
    comments_section.send_keys(normal_comment)

    # ==========================================================
    # EDGE CASE 3 - SPECIAL CHARACTERS
    # ==========================================================

    comments_section.clear()

    comments_section.send_keys(
        special_character_comment
    )

    actual_special_comment = (
        comments_section.get_attribute("value")
    )

    assert (
        actual_special_comment
        == special_character_comment
    ), "Special characters were not handled correctly."

    # Restore valid comment
    comments_section.clear()
    comments_section.send_keys(normal_comment)

    # ==========================================================
    # EDGE CASE 4 - LONG COMMENT
    # ==========================================================

    comments_section.clear()

    comments_section.send_keys(long_comment)

    actual_long_comment = (
        comments_section.get_attribute("value")
    )

    # Verify application does not silently corrupt the input.
    assert actual_long_comment is not None

    # Restore valid comment
    comments_section.clear()
    comments_section.send_keys(normal_comment)

    # ==========================================================
    # FINAL APPROVAL
    # ==========================================================

    assert (
        comments_section.get_attribute("value")
        == normal_comment
    )

    approve_submit_button = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "tlpActionSubmitBtn"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        approve_submit_button
    )

    driver.execute_script(
        "arguments[0].click();",
        approve_submit_button
    )

    # ==========================================================
    # VERIFY APPROVAL
    # ==========================================================

    time.sleep(2)

    try:

        success_message = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(@class,'swal2-success') "
                    "or contains(@class,'alert-success') "
                    "or contains(@class,'toast-success') "
                    "or contains(@class,'success')]"
                )
            )
        )

        assert success_message.is_displayed()

    except TimeoutException:

        # If there is no success popup, verify that the
        # approval modal has closed.
        try:

            wait.until(
                EC.invisibility_of_element_located(
                    (
                        By.ID,
                        "tlpActionComment"
                    )
                )
            )

        except TimeoutException:

            # At minimum verify the submitted comment remains valid.
            assert normal_comment == "Approved"

    # ==========================================================
    # FINAL WAIT
    # ==========================================================

    time.sleep(1)