from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException
)
import time


def test_fee_discount(driver):

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    fee_template_value = "fee-demo (Semester-wise)"

    discount_name_value = "demo-discount"
    discount_value_data = "10"

    # ==========================================================
    # EDGE CASE DATA
    # ==========================================================

    # Discount Name
    empty_discount_name = ""
    space_discount_name = "     "
    long_discount_name = "demo-discount-" * 20
    special_discount_name = "@#$%discount"

    # Discount Value
    empty_discount_value = ""
    zero_discount_value = "0"
    negative_discount_value = "-10"
    decimal_discount_value = "10.5"
    alphabet_discount_value = "abc"
    special_discount_value = "@10"
    greater_discount_value = "101"

    # Boundary values
    minimum_discount_value = "1"
    maximum_discount_value = "100"

    # Fee Template
    empty_fee_template = ""
    invalid_fee_template = "Invalid Fee Template"

    # ==========================================================
    # DATA VALIDATION
    # ==========================================================

    assert discount_name_value.strip(), \
        "Discount name should not be empty"

    assert discount_value_data.strip(), \
        "Discount value should not be empty"

    assert discount_value_data.isdigit(), \
        "Discount value should contain only numbers"

    assert 0 < int(discount_value_data) <= 100, \
        "Discount value should be between 1 and 100"

    assert fee_template_value.strip(), \
        "Fee template should not be empty"

    # ==========================================================
    # EDGE CASE DATA VALIDATION
    # ==========================================================

    assert empty_discount_name == "", \
        "Empty discount name test data is incorrect"

    assert space_discount_name.strip() == "", \
        "Space discount name test data is incorrect"

    assert empty_discount_value == "", \
        "Empty discount value test data is incorrect"

    assert int(zero_discount_value) == 0, \
        "Zero discount test data is incorrect"

    assert int(negative_discount_value) < 0, \
        "Negative discount test data is incorrect"

    assert float(decimal_discount_value) > 0, \
        "Decimal discount test data is incorrect"

    assert not alphabet_discount_value.isdigit(), \
        "Alphabet discount test data is incorrect"

    assert int(greater_discount_value) > 100, \
        "Greater than 100 test data is incorrect"

    assert int(minimum_discount_value) == 1, \
        "Minimum discount value should be 1"

    assert int(maximum_discount_value) == 100, \
        "Maximum discount value should be 100"

    # ==========================================================
    # OPEN FEES COLLECTION
    # ==========================================================

    fees_collection_menu = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div//span[normalize-space()='Fees Collection']"
            )
        )
    )

    fees_collection_menu.click()

    time.sleep(1)

    # ==========================================================
    # OPEN FEES DISCOUNT
    # ==========================================================

    fees_discount = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Fees Discount')])[2]"
            )
        )
    )

    fees_discount.click()

    time.sleep(2)

    # ==========================================================
    # ADD BUTTON
    # ==========================================================

    add_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "attnAjaxAddRowsBtn"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        add_btn
    )

    time.sleep(1)

    try:

        add_btn.click()

    except ElementClickInterceptedException:

        driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

    time.sleep(2)

    # ==========================================================
    # DISCOUNT NAME
    # ==========================================================

    discount_name = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "name"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        discount_name
    )

    time.sleep(1)

    discount_name.clear()

    discount_name.send_keys(
        discount_name_value
    )

    # ==========================================================
    # VERIFY DISCOUNT NAME
    # ==========================================================

    actual_discount_name = discount_name.get_attribute(
        "value"
    )

    assert actual_discount_name == \
        discount_name_value, \
        (
            f"Discount name was not entered correctly. "
            f"Expected: '{discount_name_value}', "
            f"Actual: '{actual_discount_name}'"
        )

    # ==========================================================
    # DISCOUNT VALUE
    # ==========================================================

    discount_value = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "discount_value"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        discount_value
    )

    time.sleep(1)

    discount_value.clear()

    discount_value.send_keys(
        discount_value_data
    )

    # ==========================================================
    # VERIFY DISCOUNT VALUE
    # ==========================================================

    actual_discount_value = discount_value.get_attribute(
        "value"
    )

    assert actual_discount_value == \
        discount_value_data, \
        (
            f"Discount value was not entered correctly. "
            f"Expected: '{discount_value_data}', "
            f"Actual: '{actual_discount_value}'"
        )

    # ==========================================================
    # FEE TEMPLATE MULTI-SELECT
    # ==========================================================

    fee_template = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'ms-options-wrap')])[1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fee_template
    )

    time.sleep(1)

    fee_template.click()

    time.sleep(1)

    # ==========================================================
    # FEE TEMPLATE OPTION
    # ==========================================================

    fee_template_option = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                f"//li[contains(normalize-space(),"
                f"'{fee_template_value}')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fee_template_option
    )

    time.sleep(1)

    try:

        fee_template_option.click()

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException
    ):

        driver.execute_script(
            "arguments[0].click();",
            fee_template_option
        )

    time.sleep(1)

        # ==========================================================
    # VERIFY FEE TEMPLATE SELECTION
    # ==========================================================

    selected_fee_template = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[contains(@class,'ms-options-wrap')])[1]"
            )
        )
    )

    actual_fee_template = selected_fee_template.text.strip()

    assert fee_template_value.lower() in actual_fee_template.lower(), \
        (
            f"Fee template was not selected correctly. "
            f"Expected: '{fee_template_value}', "
            f"Actual: '{actual_fee_template}'"
        )

    print("Fee template selected successfully")
    # ==========================================================
    # SAVE BUTTON
    # ==========================================================

    save = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "submitButton"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        save
    )

    time.sleep(1)

    
    driver.execute_script(
            "arguments[0].click();",
            save
        )

    time.sleep(3)

    # ==========================================================
    # VERIFY SUCCESS
    # ==========================================================

    print(
        "Fee discount created successfully"
    )