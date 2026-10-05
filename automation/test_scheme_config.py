from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from excel_report import create_report
from excel_reader import get_all_data


def test_scheme_config(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # EXTERNAL TEST DATA FROM EXCEL
    # ==========================================================

    data_list = get_all_data("Sheet3")
    results = []

    for data in data_list:

        scheme_name_value = data["Scheme Name"]
        edit_scheme_name = data["Edit Scheme Name"]

        empty_scheme_name = data["Empty Scheme Name"] or ""
        long_scheme_name = data["Long Scheme Name"]
        special_character_scheme = data["Special Character Scheme"]
        retry_test = str(data["Retry Test"]).strip().upper()
    
    # ==========================================================
        # RETRY - MAXIMUM 3 ATTEMPTS
        # ==========================================================

        for attempt in range(3):

            try:
                
                if retry_test == "YES" and attempt == 0:
                    assert False, "Intentional failure for retry testing"

                print(
                    f"\nRunning: {scheme_name_value} "
                    f"| Attempt: {attempt + 1}"
                )
                
                

                # ==========================================================
                # ATTAINMENT
                # ==========================================================

                attainment = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//div//span[normalize-space()='Attainment']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    attainment
                )

                driver.execute_script(
                    "arguments[0].click();",
                    attainment
                )

                # ==========================================================
                # SCHEME CONFIGURATION
                # ==========================================================

                scheme_config = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//a[normalize-space()='Scheme Configuration']"
                        )
                    )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    scheme_config
                )

                driver.execute_script(
                    "arguments[0].click();",
                    scheme_config
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

                time.sleep(1)

                # ==========================================================
                # SCHEME NAME
                # ==========================================================

                name = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.NAME,
                            "name"
                        )
                    )
                )

                name.clear()
                name.send_keys(scheme_name_value)

                assert (
                    name.get_attribute("value")
                    == scheme_name_value
                ), (
                    f"Scheme name mismatch. "
                    f"Expected: '{scheme_name_value}', "
                    f"Actual: '{name.get_attribute('value')}'"
                )

                # ==========================================================
                # EDGE CASE - EMPTY NAME
                # ==========================================================

                name.clear()

                assert (
                    name.get_attribute("value")
                    == empty_scheme_name
                )

                # Restore valid name
                name.send_keys(scheme_name_value)

                # ==========================================================
                # EDGE CASE - LONG NAME
                # ==========================================================

                name.clear()
                name.send_keys(long_scheme_name)

                actual_long_name = name.get_attribute("value")

                assert (
                    actual_long_name
                    == long_scheme_name
                ), (
                    f"Unexpected long name value. "
                    f"Expected: '{long_scheme_name}', "
                    f"Actual: '{actual_long_name}'"
                )

                # Restore valid name
                name.clear()
                name.send_keys(scheme_name_value)

                # ==========================================================
                # EDGE CASE - SPECIAL CHARACTERS
                # ==========================================================

                name.clear()
                name.send_keys(special_character_scheme)

                actual_special_name = name.get_attribute("value")

                assert (
                    actual_special_name
                    == special_character_scheme
                ), (
                    f"Unexpected special character handling. "
                    f"Expected: '{special_character_scheme}', "
                    f"Actual: '{actual_special_name}'"
                )

                # Restore valid name
                name.clear()
                name.send_keys(scheme_name_value)

                    # ==========================================================
                # SAVE
                # ==========================================================

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


                # ==========================================================
                # CHECK VALIDATION ERROR
                # ==========================================================

                validation_error = driver.find_elements(
                    By.XPATH,
                    "//*[contains(translate(normalize-space(.),"
                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    "'abcdefghijklmnopqrstuvwxyz'),"
                    "'already exists')]"
                )

                if validation_error:

                    error_message = validation_error[0].text.strip()

                    raise AssertionError(
                        f"Scheme was not created. "
                        f"Portal validation: {error_message}"
                    )
                    
                    

                # ==========================================================
                # VERIFY ACTION BUTTON
                # ==========================================================

                # three_dots = wait.until(
                #     EC.element_to_be_clickable(
                #         (
                #             By.XPATH,
                #             "(//button[contains(@class,"
                #             "'attn-ajax-action_button')])[1]"
                #         )
                #     )
                # )

                # driver.execute_script(
                #     "arguments[0].scrollIntoView({block:'center'});",
                #     three_dots
                # )

                # driver.execute_script(
                #     "arguments[0].click();",
                #     three_dots
                # )

                # ==========================================================
                # EDIT
                # ==========================================================

                # edit_button = wait.until(
                #     EC.element_to_be_clickable(
                #         (
                #             By.XPATH,
                #             "(//a[contains(translate(.,"
                #             "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                #             "'abcdefghijklmnopqrstuvwxyz'),'edit')])[1]"
                #         )
                #     )
                # )

                # driver.execute_script(
                #     "arguments[0].click();",
                #     edit_button
                # )

                # time.sleep(2)

                # # ==========================================================
                # # EDIT SCHEME NAME
                # # ==========================================================

                # name = wait.until(
                #     EC.visibility_of_element_located(
                #         (
                #             By.NAME,
                #             "name"
                #         )
                #     )
                # )

                # name.clear()
                # name.send_keys(edit_scheme_name)

                # assert (
                #     name.get_attribute("value")
                #     == edit_scheme_name
                # ), (
                #     f"Edit scheme name mismatch. "
                #     f"Expected: '{edit_scheme_name}', "
                #     f"Actual: '{name.get_attribute('value')}'"
                # )

                # # ==========================================================
                # # SAVE EDIT
                # # ==========================================================

                # save_button = wait.until(
                #     EC.element_to_be_clickable(
                #         (
                #             By.ID,
                #             "submitButton"
                #         )
                #     )
                # )

                # driver.execute_script(
                #     "arguments[0].click();",
                #     save_button
                # )

                # time.sleep(3)

                # # ==========================================================
                # # OPEN ACTION MENU AGAIN
                # # ==========================================================

                # three_dots = wait.until(
                #     EC.element_to_be_clickable(
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
                # # DELETE
                # # ==========================================================

                # delete_button = wait.until(
                #     EC.element_to_be_clickable(
                #         (
                #             By.XPATH,
                #             "(//a[contains(@class,'delete-button-datatable') "
                #             "or contains(translate(.,"
                #             "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                #             "'abcdefghijklmnopqrstuvwxyz'),'delete')])[1]"
                #         )
                #     )
                # )

                # driver.execute_script(
                #     "arguments[0].scrollIntoView({block:'center'});",
                #     delete_button
                # )

                # driver.execute_script(
                #     "arguments[0].click();",
                #     delete_button
                # )

                # # ==========================================================
                # # DELETE CONFIRMATION MODAL
                # # ==========================================================

                # modal = wait.until(
                #     EC.visibility_of_element_located(
                #         (
                #             By.XPATH,
                #             "//div[@aria-describedby='swal2-html-container']"
                #         )
                #     )
                # )

                # assert modal.is_displayed(), (
                #     "Delete confirmation modal was not displayed."
                # )

                # # ==========================================================
                # # CONFIRM DELETE
                # # ==========================================================

                # confirm_button = wait.until(
                #     EC.element_to_be_clickable(
                #         (
                #             By.XPATH,
                #             "//button[contains(@class,'swal2-confirm')]"
                #         )
                #     )
                # )

                # driver.execute_script(
                #     "arguments[0].click();",
                #     confirm_button
                # )

                # # ==========================================================
                # # VERIFY MODAL CLOSED
                # # ==========================================================

                # wait.until(
                #     EC.invisibility_of_element_located(
                #         (
                #             By.XPATH,
                #             "//div[@aria-describedby='swal2-html-container']"
                #         )
                #     )
                # )

                # time.sleep(2)

        # ==========================================================
        # SUCCESS
        # ==========================================================

                print(
                    f"PASS: {scheme_name_value}"
                )

                results.append({
                    "Test Case": "Scheme Configuration",
                    "Test Data": scheme_name_value,
                    "Attempt": attempt + 1,
                    "Status": "PASS",
                    "Error": "",
                    "Final Status": "PASS"
                })

                break

            # ==========================================================
            # FAILURE / RETRY
            # ==========================================================

            except Exception as e:

                print(
                    f"FAIL: {scheme_name_value} "
                    f"| Attempt {attempt + 1}"
                )

                print(f"Error: {e}")

                if attempt < 2:

                    print(
                        f"Retrying {scheme_name_value}..."
                    )

                    time.sleep(2)

                else:

                    print(
                        f"FINAL FAIL: {scheme_name_value}"
                    )
                    
                    results.append({
                        "Test Case": "Scheme Configuration",
                        "Test Data": scheme_name_value,
                        "Attempt": attempt + 1,
                        "Status": "FAIL",
                        "Error": str(e),
                        "Final Status": "FAIL"
                    })

                    raise
            finally:
                create_report(results)