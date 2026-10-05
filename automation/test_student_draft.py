from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_student_draft(driver):

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
    # OPEN STUDENT FORM DRAFT
    # ==========================================================

    student_draft_form = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Student Form Draft')])[2]"
            )
        )
    )

    student_draft_form.click()

    # ==========================================================
    # PREVIEW BUTTON
    # ==========================================================

    # preview_btn = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//button[@class='primary-btn fix-gr-bg nxgn_secondary_btn draft-preview-button'])[1]"
    #         )
    #     )
    # )
    #
    # preview_btn.click()

    # ==========================================================
    # CLOSE PREVIEW
    # ==========================================================

    # close_btn = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//button[@aria-label='Close']"
    #         )
    #     )
    # )
    #
    # close_btn.click()

    # ==========================================================
    # THREE DOTS
    # ==========================================================

    three_dots = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//button[@class='attn-ajax-action_button'])[1]"
            )
        )
    )

    three_dots.click()

    # ==========================================================
    # OPEN BUTTON
    # ==========================================================

    # open_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//a[@class='attn-ajax-action_item_list'])[1]"
    #         )
    #     )
    # )
    #
    # open_button.click()

    # ==========================================================
    # DELETE BUTTON
    # ==========================================================

    delete_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[contains(@class,'delete-button-datatable')])[1]"
            )
        )
    )

    delete_button.click()

    # ==========================================================
    # DELETE CONFIRMATION POPUP
    # ==========================================================

    confirmation_popup = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[@aria-describedby='swal2-html-container']"
            )
        )
    )

    # ==========================================================
    # CANCEL DELETE
    # ==========================================================

    cancel_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(@class,'swal2-cancel')]"
            )
        )
    )

    cancel_button.click()

    # ==========================================================
    # CONFIRM DELETE
    # ==========================================================

    # confirm_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//button[contains(@class,'swal2-confirm')]"
    #         )
    #     )
    # )
    #
    # confirm_button.click()