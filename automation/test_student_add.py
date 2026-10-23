from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)
import time


def test_student_add(driver):

    wait = WebDriverWait(driver, 15)

    # ==========================================================
    # TEST DATA
    # ==========================================================

    admission_date_value = "19/08/2026"

    roll_number_value = "STU001"

    student_category_value = "General"

    first_name_value = "Rahul"
    last_name_value = "Patil"

    date_of_birth_value = "15/08/2026"

    gender_value = "Male"
    mother_tongue_value = "Marathi"

    religion_value = "Hindu"
    caste_value = "General"

    reserved_category_value = "Yes"
    admission_type_value = "Regular"

    form_number_value = "FORM001"
    landline_value = "0201234567"

    phone_number_value = "4598658967"
    email_address_value = "rahul.patil@example.com"

    current_status_value = "Regular"
    joining_semester_value = "Sem-3-IT"

    marital_status_value = "Single"
    blood_group_value = "O+"

    height_value = "165"
    weight_value = "55"

    disability_value = "No"

    abc_id_value = "ABC123456"
    prn_number_value = "PRN001"

    # ==========================================================
    # PARENT & GUARDIAN TEST DATA
    # ==========================================================

    total_family_members_value = "4"

    father_name_value = "Rajesh Patil"
    father_email_value = "rajesh.patil@example.com"
    father_phone_value = "5698745632"
    father_dob_value = "15/06/1975"
    father_income_value = "600000"
    father_landline_value = "0201234567"
    father_education_value = "MBA"
    father_occupation_value = "Business"
    father_work_address_value = "Pune, Maharashtra"

    mother_name_value = "Sunita Patil"
    mother_email_value = "sunita.patil@example.com"
    mother_phone_value = "9876543211"
    mother_dob_value = "20/08/1978"
    mother_income_value = "450000"
    mother_landline_value = "0201234568"
    mother_education_value = "MA"
    mother_occupation_value = "Teacher"
    mother_work_address_value = "Pune, Maharashtra"

    guardian_relation_value = "Father"

    # ==========================================================
    # VALIDATIONS
    # ==========================================================

    assert admission_date_value.strip() != "", \
        "Admission date should not be empty"

    assert roll_number_value.strip() != "", \
        "Roll number should not be empty"

    assert student_category_value.strip() != "", \
        "Student category should not be empty"

    assert first_name_value.strip() != "", \
        "First name should not be empty"

    assert last_name_value.strip() != "", \
        "Last name should not be empty"

    assert phone_number_value.isdigit(), \
        "Phone number should contain only numbers"

    assert len(phone_number_value) == 10, \
        "Phone number should contain 10 digits"

    assert email_address_value.strip() != "", \
        "Email address should not be empty"

    assert "@" in email_address_value, \
        "Email address should contain @"

    assert height_value.isdigit(), \
        "Height should contain only numbers"

    assert int(height_value) > 0, \
        "Height should be greater than zero"

    assert weight_value.isdigit(), \
        "Weight should contain only numbers"

    assert int(weight_value) > 0, \
        "Weight should be greater than zero"

    # ==========================================================
    # PARENT & GUARDIAN VALIDATIONS
    # ==========================================================

    assert total_family_members_value.strip() != "", \
        "Total family members should not be empty"

    assert total_family_members_value.isdigit(), \
        "Total family members should contain only numbers"

    assert int(total_family_members_value) > 0, \
        "Total family members should be greater than zero"

    assert father_name_value.strip() != "", \
        "Father name should not be empty"

    assert father_email_value.strip() != "", \
        "Father email should not be empty"

    assert "@" in father_email_value, \
        "Father email should contain @"

    assert father_phone_value.isdigit(), \
        "Father phone should contain only numbers"

    assert len(father_phone_value) == 10, \
        "Father phone should contain 10 digits"

    assert mother_name_value.strip() != "", \
        "Mother name should not be empty"

    assert mother_email_value.strip() != "", \
        "Mother email should not be empty"

    assert "@" in mother_email_value, \
        "Mother email should contain @"

    assert mother_phone_value.isdigit(), \
        "Mother phone should contain only numbers"

    assert len(mother_phone_value) == 10, \
        "Mother phone should contain 10 digits"

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
    # STUDENT ADD / MODIFY
    # ==========================================================

    student_add_modify = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Student Add/Modify')])[2]"
            )
        )
    )

    student_add_modify.click()

    time.sleep(2)

    # ==========================================================
    # ADD STUDENT
    # ==========================================================

    add_student_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[contains(.,'Add Student')]"
            )
        )
    )

    add_student_button.click()

    time.sleep(2)

    # ==========================================================
    # ADMISSION DATE
    # ==========================================================

    admission_date = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@placeholder='Select Date'])[1]"
            )
        )
    )

    admission_date.click()

    time.sleep(1)

    admission_day = admission_date_value.split("/")[0]

    date = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//td[contains(@class,'day') "
                f"and normalize-space()='{admission_day}' "
                f"and not(contains(@class,'old')) "
                f"and not(contains(@class,'new'))]"
            )
        )
    )

    date.click()

    time.sleep(1)

    assert admission_date.get_attribute("value") == \
        admission_date_value, \
        "Admission date was not entered correctly"

    # ==========================================================
    # ROLL NUMBER
    # ==========================================================

    roll_number = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "roll_number"
            )
        )
    )

    roll_number.send_keys(roll_number_value)

    assert roll_number.get_attribute("value") == \
        roll_number_value, \
        "Roll number was not entered correctly"

    # ==========================================================
    # STUDENT CATEGORY
    # ==========================================================

    student_category = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[1]"
            )
        )
    )

    student_category.click()

    student_category_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                "//li[normalize-space()='General']"
            )
        )
    )

    student_category_option.click()

    # ==========================================================
    # FIRST NAME
    # ==========================================================

    first_name = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "first_name"
            )
        )
    )

    first_name.send_keys(first_name_value)

    assert first_name.get_attribute("value") == \
        first_name_value, \
        "First name was not entered correctly"

    # ==========================================================
    # LAST NAME
    # ==========================================================

    last_name = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "last_name"
            )
        )
    )

    last_name.send_keys(last_name_value)

    assert last_name.get_attribute("value") == \
        last_name_value, \
        "Last name was not entered correctly"

    # ==========================================================
    # DATE OF BIRTH
    # ==========================================================

    date_of_birth = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@placeholder='Select Date'])[2]"
            )
        )
    )

    date_of_birth.click()

    time.sleep(1)

    dob_day = date_of_birth_value.split("/")[0]

    date = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//td[contains(@class,'day') "
                f"and normalize-space()='{dob_day}' "
                f"and not(contains(@class,'old')) "
                f"and not(contains(@class,'new'))]"
            )
        )
    )

    date.click()

    time.sleep(1)

    assert date_of_birth.get_attribute("value") == \
        date_of_birth_value, \
        "Date of birth was not entered correctly"

    # ==========================================================
    # GENDER
    # ==========================================================

    gender = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[2]"
            )
        )
    )

    gender.click()

    gender_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{gender_value}']"
            )
        )
    )

    gender_option.click()

    # ==========================================================
    # MOTHER TONGUE
    # ==========================================================

    mother_tongue = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[3]"
            )
        )
    )

    mother_tongue.click()

    mother_tongue_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{mother_tongue_value}']"
            )
        )
    )

    mother_tongue_option.click()

    # ==========================================================
    # RELIGION
    # ==========================================================

    religion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[4]"
            )
        )
    )

    religion.click()

    religion_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{religion_value}']"
            )
        )
    )

    religion_option.click()

    # ==========================================================
    # CASTE
    # ==========================================================

    caste = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "caste"
            )
        )
    )

    caste.send_keys(caste_value)

    assert caste.get_attribute("value") == \
        caste_value, \
        "Caste was not entered correctly"

    # ==========================================================
    # RESERVED CATEGORY
    # ==========================================================

    reserved_category = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[5]"
            )
        )
    )

    reserved_category.click()

    reserved_category_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{reserved_category_value}']"
            )
        )
    )

    reserved_category_option.click()

    # ==========================================================
    # ADMISSION TYPE
    # ==========================================================

    admission_type = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[6]"
            )
        )
    )

    admission_type.click()

    admission_type_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{admission_type_value}']"
            )
        )
    )

    admission_type_option.click()

    # ==========================================================
    # FORM NUMBER
    # ==========================================================

    form_number = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "form_number"
            )
        )
    )

    form_number.send_keys(form_number_value)

    assert form_number.get_attribute("value") == \
        form_number_value, \
        "Form number was not entered correctly"

    # ==========================================================
    # LANDLINE
    # ==========================================================

    landline = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "landline"
            )
        )
    )

    if landline_value:
        landline.send_keys(landline_value)

        assert landline.get_attribute("value") == \
            landline_value, \
            "Landline was not entered correctly"

    # ==========================================================
    # PHONE NUMBER
    # ==========================================================

    phone_number = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "phone_number"
            )
        )
    )

    phone_number.send_keys(phone_number_value)

    assert phone_number.get_attribute("value") == \
        phone_number_value, \
        "Phone number was not entered correctly"

    # ==========================================================
    # EMAIL
    # ==========================================================

    email_address = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "email_address"
            )
        )
    )

    email_address.send_keys(email_address_value)

    assert email_address.get_attribute("value") == \
        email_address_value, \
        "Email address was not entered correctly"

    # ==========================================================
    # CURRENT STATUS
    # ==========================================================

    current_status = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[7]"
            )
        )
    )

    current_status.click()

    current_status_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{current_status_value}']"
            )
        )
    )

    current_status_option.click()

    # # ==========================================================
    # # JOINING SEMESTER
    # # ==========================================================

    # joining_semester = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[8]"
    #         )
    #     )
    # )

    # joining_semester.click()

    # joining_semester_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{joining_semester_value}']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #             "arguments[0].click();",
    #             joining_semester_option
    #         )

    # ==========================================================
    # MARITAL STATUS
    # ==========================================================

    marital_status = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[9]"
            )
        )
    )

    marital_status.click()

    marital_status_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{marital_status_value}']"
            )
        )
    )

    marital_status_option.click()

    # ==========================================================
    # BLOOD GROUP
    # ==========================================================

    blood_group = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[10]"
            )
        )
    )

    blood_group.click()

    blood_group_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{blood_group_value}']"
            )
        )
    )

    blood_group_option.click()

    # ==========================================================
    # HEIGHT
    # ==========================================================

    height = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "height"
            )
        )
    )

    height.send_keys(height_value)

    assert height.get_attribute("value") == \
        height_value, \
        "Height was not entered correctly"

    # ==========================================================
    # WEIGHT
    # ==========================================================

    weight = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "weight"
            )
        )
    )

    weight.send_keys(weight_value)

    assert weight.get_attribute("value") == \
        weight_value, \
        "Weight was not entered correctly"

    # ==========================================================
    # DISABILITY
    # ==========================================================

    disability = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[11]"
            )
        )
    )

    disability.click()

    disability_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{disability_value}']"
            )
        )
    )

    disability_option.click()

    # ==========================================================
    # ABC ID
    # ==========================================================

    abc_id = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "abc_id"
            )
        )
    )

    abc_id.send_keys(abc_id_value)

    assert abc_id.get_attribute("value") == \
        abc_id_value, \
        "ABC ID was not entered correctly"

    # ==========================================================
    # PRN NUMBER
    # ==========================================================

    prn_number = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "prn_no"
            )
        )
    )

    prn_number.send_keys(prn_number_value)

    assert prn_number.get_attribute("value") == \
        prn_number_value, \
        "PRN number was not entered correctly"

    # ==========================================================
    # REQUIRED FIELD VALIDATION
    # ==========================================================

    assert admission_date.get_attribute("value").strip() != "", \
        "Admission date is required"

    assert roll_number.get_attribute("value").strip() != "", \
        "Roll number is required"

    assert first_name.get_attribute("value").strip() != "", \
        "First name is required"

    assert last_name.get_attribute("value").strip() != "", \
        "Last name is required"

    assert phone_number.get_attribute("value").strip() != "", \
        "Phone number is required"

    assert email_address.get_attribute("value").strip() != "", \
        "Email address is required"

    # ==========================================================
    # NEXT
    # ==========================================================

    next_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'Next')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        next_button
    )

    time.sleep(1)

    try:
        next_button.click()

    except ElementClickInterceptedException:
        driver.execute_script(
            "arguments[0].click();",
            next_button
        )

    time.sleep(3)

    # ==========================================================
    # VERIFY PARENT & GUARDIAN STEP
    # ==========================================================

    parent_guardian = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(normalize-space(),"
                "'Parent & Guardian Info')]"
            )
        )
    )

    assert parent_guardian.is_displayed(), \
        "Parent & Guardian Info step was not opened"

    print(
        "Student Add - Personal Information completed successfully"
    )

    # ==========================================================
    # TOTAL FAMILY MEMBERS
    # ==========================================================

    total_family_members = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "total_family_members"
            )
        )
    )

    total_family_members.send_keys(
        total_family_members_value
    )

    assert total_family_members.get_attribute("value") == \
        total_family_members_value, \
        "Total family members was not entered correctly"

    # ==========================================================
    # FATHER NAME
    # ==========================================================

    father_name = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "fathers_name"
            )
        )
    )

    father_name.send_keys(father_name_value)

    assert father_name.get_attribute("value") == \
        father_name_value, \
        "Father name was not entered correctly"

    # ==========================================================
    # FATHER EMAIL
    # ==========================================================

    father_email = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "fathers_email"
            )
        )
    )

    father_email.send_keys(father_email_value)

    assert father_email.get_attribute("value") == \
        father_email_value, \
        "Father email was not entered correctly"

    # ==========================================================
    # FATHER PHONE
    # ==========================================================

    father_phone = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "fathers_phone"
            )
        )
    )

    father_phone.send_keys(father_phone_value)

    assert father_phone.get_attribute("value") == \
        father_phone_value, \
        "Father phone was not entered correctly"

    # # ==========================================================
    # # FATHER DOB
    # # ==========================================================

    # father_dob = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "fathers_dob"
    #         )
    #     )
    # )

    # father_dob.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # GET VISIBLE DATEPICKER
    # # ----------------------------------------------------------

    # visible_datepicker_days = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-days"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # # ----------------------------------------------------------
    # # OPEN MONTH VIEW
    # # ----------------------------------------------------------

    # datepicker_switch = visible_datepicker_days.find_element(
    #     By.CSS_SELECTOR,
    #     "th.datepicker-switch"
    # )

    # datepicker_switch.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # OPEN YEAR VIEW
    # # ----------------------------------------------------------

    # visible_datepicker_months = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-months"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # month_switch = visible_datepicker_months.find_element(
    #     By.CSS_SELECTOR,
    #     "th.datepicker-switch"
    # )

    # month_switch.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # SELECT YEAR
    # # ----------------------------------------------------------

    # year_value = father_dob_value.split("/")[2]

    # visible_datepicker_years = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-years"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # year = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in visible_datepicker_years.find_elements(
    #                 By.CSS_SELECTOR,
    #                 "span.year"
    #             )
    #             if element.text.strip() == year_value
    #             and element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # year.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # SELECT MONTH
    # # ----------------------------------------------------------

    # month_number = father_dob_value.split("/")[1]

    # month_names = {
    #     "01": "Jan",
    #     "02": "Feb",
    #     "03": "Mar",
    #     "04": "Apr",
    #     "05": "May",
    #     "06": "Jun",
    #     "07": "Jul",
    #     "08": "Aug",
    #     "09": "Sep",
    #     "10": "Oct",
    #     "11": "Nov",
    #     "12": "Dec"
    # }

    # month_value = month_names[month_number]

    # visible_datepicker_months = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-months"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # month = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in visible_datepicker_months.find_elements(
    #                 By.CSS_SELECTOR,
    #                 "span.month"
    #             )
    #             if element.text.strip() == month_value
    #             and element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # month.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # SELECT DAY
    # # ----------------------------------------------------------

    # day_value = father_dob_value.split("/")[0]

    # visible_datepicker_days = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-days"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # day = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in visible_datepicker_days.find_elements(
    #                 By.CSS_SELECTOR,
    #                 "td.day"
    #             )
    #             if element.text.strip() == day_value
    #             and "old" not in element.get_attribute("class")
    #             and "new" not in element.get_attribute("class")
    #             and element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # day.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # VERIFY FATHER DOB
    # # ----------------------------------------------------------

    # actual_father_dob = father_dob.get_attribute("value")

    # print(
    #     "Father DOB entered:",
    #     actual_father_dob
    # )

    # assert actual_father_dob == father_dob_value, \
    #     f"Father DOB was not entered correctly. Expected: {father_dob_value}, Got: {actual_father_dob}"

    # ==========================================================
    # FATHER INCOME
    # ==========================================================

    father_income = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "fathers_income"
            )
        )
    )

    father_income.send_keys(father_income_value)

    assert father_income.get_attribute("value") == \
        father_income_value, \
        "Father income was not entered correctly"

    # ==========================================================
    # FATHER LANDLINE
    # ==========================================================

    father_landline = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "fathers_landline"
            )
        )
    )

    if father_landline_value:
        father_landline.send_keys(
            father_landline_value
        )

        assert father_landline.get_attribute("value") == \
            father_landline_value, \
            "Father landline was not entered correctly"

    # ==========================================================
    # FATHER EDUCATION
    # ==========================================================

    father_education = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "fathers_education"
            )
        )
    )

    father_education.send_keys(
        father_education_value
    )

    assert father_education.get_attribute("value") == \
        father_education_value, \
        "Father education was not entered correctly"

    # ==========================================================
    # FATHER OCCUPATION
    # ==========================================================

    father_occupation = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "fathers_occupation"
            )
        )
    )

    father_occupation.send_keys(
        father_occupation_value
    )

    assert father_occupation.get_attribute("value") == \
        father_occupation_value, \
        "Father occupation was not entered correctly"

    # ==========================================================
    # FATHER WORK ADDRESS
    # ==========================================================

    father_work_address = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "fathers_work_address"
            )
        )
    )

    father_work_address.send_keys(
        father_work_address_value
    )

    assert father_work_address.get_attribute("value") == \
        father_work_address_value, \
        "Father work address was not entered correctly"

    # # ==========================================================
    # # MOTHER NAME
    # # ==========================================================

    # mother_name = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.ID,
    #             "mothers_name"
    #         )
    #     )
    # )

    # mother_name.send_keys(
    #     mother_name_value
    # )

    # assert mother_name.get_attribute("value") == \
    #     mother_name_value, \
    #     "Mother name was not entered correctly"

    # # ==========================================================
    # # MOTHER EMAIL
    # # ==========================================================

    # mother_email = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.ID,
    #             "mothers_email"
    #         )
    #     )
    # )

    # mother_email.send_keys(
    #     mother_email_value
    # )

    # assert mother_email.get_attribute("value") == \
    #     mother_email_value, \
    #     "Mother email was not entered correctly"

    # # ==========================================================
    # # MOTHER PHONE
    # # ==========================================================

    # mother_phone = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Mother Phone']"
    #         )
    #     )
    # )

    # mother_phone.send_keys(
    #     mother_phone_value
    # )

    # assert mother_phone.get_attribute("value") == \
    #     mother_phone_value, \
    #     "Mother phone was not entered correctly"

    # # ==========================================================
    # # MOTHER DOB
    # # ==========================================================

    # mother_dob = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//input[@placeholder='Select Date'])[2]"
    #         )
    #     )
    # )

    # mother_dob.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # OPEN MONTH VIEW
    # # ----------------------------------------------------------

    # visible_datepicker_days = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-days"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # visible_datepicker_days.find_element(
    #     By.CSS_SELECTOR,
    #     "th.datepicker-switch"
    # ).click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # OPEN YEAR VIEW
    # # ----------------------------------------------------------

    # visible_datepicker_months = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-months"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # visible_datepicker_months.find_element(
    #     By.CSS_SELECTOR,
    #     "th.datepicker-switch"
    # ).click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # SELECT YEAR
    # # ----------------------------------------------------------

    # year_value = mother_dob_value.split("/")[2]

    # visible_datepicker_years = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-years"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # year = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in visible_datepicker_years.find_elements(
    #                 By.CSS_SELECTOR,
    #                 "span.year"
    #             )
    #             if element.text.strip() == year_value
    #             and element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # year.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # SELECT MONTH
    # # ----------------------------------------------------------

    # month_number = mother_dob_value.split("/")[1]

    # month_value = month_names[month_number]

    # visible_datepicker_months = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-months"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # month = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in visible_datepicker_months.find_elements(
    #                 By.CSS_SELECTOR,
    #                 "span.month"
    #             )
    #             if element.text.strip() == month_value
    #             and element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # month.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # SELECT DAY
    # # ----------------------------------------------------------

    # day_value = mother_dob_value.split("/")[0]

    # visible_datepicker_days = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in driver.find_elements(
    #                 By.CSS_SELECTOR,
    #                 ".datepicker-days"
    #             )
    #             if element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # day = wait.until(
    #     lambda driver: next(
    #         (
    #             element
    #             for element in visible_datepicker_days.find_elements(
    #                 By.CSS_SELECTOR,
    #                 "td.day"
    #             )
    #             if element.text.strip() == day_value
    #             and "old" not in element.get_attribute("class")
    #             and "new" not in element.get_attribute("class")
    #             and element.is_displayed()
    #         ),
    #         False
    #     )
    # )

    # day.click()

    # time.sleep(1)

    # # ----------------------------------------------------------
    # # VERIFY MOTHER DOB
    # # ----------------------------------------------------------

    # actual_mother_dob = mother_dob.get_attribute("value")

    # print(
    #     "Mother DOB entered:",
    #     actual_mother_dob
    # )

    # assert actual_mother_dob == mother_dob_value, \
    #     f"Mother DOB was not entered correctly. Expected: {mother_dob_value}, Got: {actual_mother_dob}"

    # ==========================================================
    # MOTHER INCOME
    # ==========================================================

    # mother_income = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Mother Income']"
    #         )
    #     )
    # )

    # mother_income.send_keys(
    #     mother_income_value
    # )

    # assert mother_income.get_attribute("value") == \
    #     mother_income_value, \
    #     "Mother income was not entered correctly"

    # # ==========================================================
    # # MOTHER LANDLINE
    # # ==========================================================

    # mother_landline = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Mother Landline']"
    #         )
    #     )
    # )

    # if mother_landline_value:
    #     mother_landline.send_keys(
    #         mother_landline_value
    #     )

    #     assert mother_landline.get_attribute("value") == \
    #         mother_landline_value, \
    #         "Mother landline was not entered correctly"

    # # ==========================================================
    # # MOTHER EDUCATION
    # # ==========================================================

    # mother_education = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Mother Education']"
    #         )
    #     )
    # )

    # mother_education.send_keys(
    #     mother_education_value
    # )

    # assert mother_education.get_attribute("value") == \
    #     mother_education_value, \
    #     "Mother education was not entered correctly"

    # # ==========================================================
    # # MOTHER OCCUPATION
    # # ==========================================================

    # mother_occupation = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//input[@placeholder='Occupation'])[2]"
    #         )
    #     )
    # )

    # mother_occupation.send_keys(
    #     mother_occupation_value
    # )

    # assert mother_occupation.get_attribute("value") == \
    #     mother_occupation_value, \
    #     "Mother occupation was not entered correctly"

    # # ==========================================================
    # # MOTHER WORK ADDRESS
    # # ==========================================================

    # mother_work_address = wait.until(
    #     EC.visibility_of_element_located(
    #         (
    #             By.XPATH,
    #             "//textarea[@placeholder='Mother Work Address']"
    #         )
    #     )
    # )

    # mother_work_address.send_keys(
    #     mother_work_address_value
    # )

    # assert mother_work_address.get_attribute("value") == \
    #     mother_work_address_value, \
    #     "Mother work address was not entered correctly"

    # ==========================================================
    # RELATION WITH GUARDIAN
    # ==========================================================

    relation_with_guardian = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[12]"
            )
        )
    )

    relation_with_guardian.click()

    relation_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{guardian_relation_value}']"
            )
        )
    )

    relation_option.click()

    time.sleep(1)

        # ==========================================================
    # SELECT GUARDIAN DATA
    # ==========================================================

    if guardian_relation_value == "Father":

        guardian_name_value = father_name_value
        guardian_email_value = father_email_value
        guardian_phone_value = father_phone_value
        guardian_dob_value = father_dob_value
        guardian_income_value = father_income_value
        guardian_landline_value = father_landline_value
        guardian_education_value = father_education_value
        guardian_occupation_value = father_occupation_value
        guardian_work_address_value = father_work_address_value

    elif guardian_relation_value == "Mother":

        guardian_name_value = mother_name_value
        guardian_email_value = mother_email_value
        guardian_phone_value = mother_phone_value
        guardian_dob_value = mother_dob_value
        guardian_income_value = mother_income_value
        guardian_landline_value = mother_landline_value
        guardian_education_value = mother_education_value
        guardian_occupation_value = mother_occupation_value
        guardian_work_address_value = mother_work_address_value

    elif guardian_relation_value == "Others":

        guardian_name_value = "Guardian"
        guardian_email_value = "guardian@example.com"
        guardian_phone_value = "9876543212"
        guardian_dob_value = "15/08/1975"
        guardian_income_value = "500000"
        guardian_landline_value = "0201234569"
        guardian_education_value = "MBA"
        guardian_occupation_value = "Business"
        guardian_work_address_value = "Pune, Maharashtra"


    # ==========================================================
    # NEXT
    # ==========================================================

    next_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'Next')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        next_button
    )

    time.sleep(1)

    try:

        next_button.click()

    except ElementClickInterceptedException:

        driver.execute_script(
            "arguments[0].click();",
            next_button
        )

    time.sleep(3)


    # ==========================================================
    # GUARDIAN DETAILS
    # ONLY FOR "OTHERS"
    # ==========================================================

    if guardian_relation_value == "Others":

        # ======================================================
        # GUARDIAN NAME
        # ======================================================

        guardian_name = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[@placeholder='Guardian Name']"
                )
            )
        )

        guardian_name.send_keys(
            guardian_name_value
        )

        assert guardian_name.get_attribute("value") == \
            guardian_name_value, \
            "Guardian name was not entered correctly"


        # ======================================================
        # GUARDIAN EMAIL
        # ======================================================

        guardian_email = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[@placeholder='Guardian Email']"
                )
            )
        )

        guardian_email.send_keys(
            guardian_email_value
        )

        assert guardian_email.get_attribute("value") == \
            guardian_email_value, \
            "Guardian email was not entered correctly"


        # ======================================================
        # GUARDIAN PHONE
        # ======================================================

        guardian_phone = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[@placeholder='Guardian Phone']"
                )
            )
        )

        guardian_phone.send_keys(
            guardian_phone_value
        )

        assert guardian_phone.get_attribute("value") == \
            guardian_phone_value, \
            "Guardian phone was not entered correctly"


        # ======================================================
        # GUARDIAN DOB
        # ======================================================

        # Your DOB code goes here when you enable it.


        # ======================================================
        # GUARDIAN INCOME
        # ======================================================

        guardian_income = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[@placeholder='Guardian Income']"
                )
            )
        )

        guardian_income.send_keys(
            guardian_income_value
        )

        assert guardian_income.get_attribute("value") == \
            guardian_income_value, \
            "Guardian income was not entered correctly"


        # ======================================================
        # GUARDIAN LANDLINE
        # ======================================================

        guardian_landline = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[@placeholder='Guardian Landline']"
                )
            )
        )

        if guardian_landline_value:

            guardian_landline.send_keys(
                guardian_landline_value
            )

            assert guardian_landline.get_attribute("value") == \
                guardian_landline_value, \
                "Guardian landline was not entered correctly"


        # ======================================================
        # GUARDIAN EDUCATION
        # ======================================================

        guardian_education = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[@placeholder='Guardian Education']"
                )
            )
        )

        guardian_education.send_keys(
            guardian_education_value
        )

        assert guardian_education.get_attribute("value") == \
            guardian_education_value, \
            "Guardian education was not entered correctly"


        # ======================================================
        # GUARDIAN OCCUPATION
        # ======================================================

        guardian_occupation = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "(//input[@placeholder='Occupation'])[3]"
                )
            )
        )

        guardian_occupation.send_keys(
            guardian_occupation_value
        )

        assert guardian_occupation.get_attribute("value") == \
            guardian_occupation_value, \
            "Guardian occupation was not entered correctly"


        # ======================================================
        # GUARDIAN WORK ADDRESS
        # ======================================================

        guardian_work_address = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//textarea[@placeholder='Guardian Work Address']"
                )
            )
        )

        guardian_work_address.send_keys(
            guardian_work_address_value
        )

        assert guardian_work_address.get_attribute("value") == \
            guardian_work_address_value, \
            "Guardian work address was not entered correctly"


    # ==========================================================
    # FINAL MESSAGE
    # ==========================================================

    print(
        "Student Add - Parent & Guardian Information "
        "completed successfully"
    )
        
    
        # ==========================================================
    # RESIDENTIAL & PERMANENT ADDRESS TEST DATA
    # ==========================================================

    residential_address_line1_value = "123 MG Road"
    residential_address_line2_value = "Shivajinagar"
    residential_state_value = "Maharashtra"
    residential_city_value = "Pune"
    residential_pincode_value = "411005"

    permanent_address_line1_value = "123 MG Road"
    permanent_address_line2_value = "Shivajinagar"
    permanent_state_value = "Maharashtra"
    permanent_city_value = "Pune"
    permanent_pincode_value = "411005"

    nationality_value = "Indian"


    # ==========================================================
    # VALIDATIONS
    # ==========================================================

    assert residential_address_line1_value.strip() != "", \
        "Residential Address Line 1 should not be empty"

    assert residential_address_line2_value.strip() != "", \
        "Residential Address Line 2 should not be empty"

    assert residential_state_value.strip() != "", \
        "Residential State should not be empty"

    assert residential_city_value.strip() != "", \
        "Residential City should not be empty"

    assert residential_pincode_value.isdigit(), \
        "Residential Pincode should contain only numbers"

    assert len(residential_pincode_value) == 6, \
        "Residential Pincode should contain 6 digits"

    assert permanent_address_line1_value.strip() != "", \
        "Permanent Address Line 1 should not be empty"

    assert permanent_address_line2_value.strip() != "", \
        "Permanent Address Line 2 should not be empty"

    assert permanent_state_value.strip() != "", \
        "Permanent State should not be empty"

    assert permanent_city_value.strip() != "", \
        "Permanent City should not be empty"

    assert permanent_pincode_value.isdigit(), \
        "Permanent Pincode should contain only numbers"

    assert len(permanent_pincode_value) == 6, \
        "Permanent Pincode should contain 6 digits"

    assert nationality_value.strip() != "", \
        "Nationality should not be empty"


    # ==========================================================
    # RESIDENTIAL ADDRESS LINE 1
    # ==========================================================

    residential_address_line1 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//textarea[@placeholder='Residential Address Line 1']"
            )
        )
    )

    residential_address_line1.send_keys(
        residential_address_line1_value
    )

    assert residential_address_line1.get_attribute("value") == \
        residential_address_line1_value, \
        "Residential Address Line 1 was not entered correctly"


    # ==========================================================
    # RESIDENTIAL ADDRESS LINE 2
    # ==========================================================

    residential_address_line2 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//textarea[@placeholder='Residential Address Line 2']"
            )
        )
    )

    residential_address_line2.send_keys(
        residential_address_line2_value
    )

    assert residential_address_line2.get_attribute("value") == \
        residential_address_line2_value, \
        "Residential Address Line 2 was not entered correctly"


    # ==========================================================
    # RESIDENTIAL STATE
    # ==========================================================

    residential_state = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[13]"
            )
        )
    )

    residential_state.click()

    residential_state_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{residential_state_value}']"
            )
        )
    )

    driver.execute_script(
                "arguments[0].click();",
                residential_state_option
            )


    # ==========================================================
    # RESIDENTIAL CITY
    # ==========================================================

    # residential_city = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[@class='nice-select primary_select form-control'])[14]"
    #         )
    #     )
    # )

    # residential_city.click()

    # residential_city_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             f"//li[normalize-space()='{residential_city_value}']"
    #         )
    #     )
    # )

    # residential_city_option.click()

    # ==========================================================
    # RESIDENTIAL PINCODE
    # ==========================================================

    residential_pincode = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "residential_pincode"
            )
        )
    )

    residential_pincode.send_keys(
        residential_pincode_value
    )

    assert residential_pincode.get_attribute("value") == \
        residential_pincode_value, \
        "Residential Pincode was not entered correctly"


    # ==========================================================
    # PERMANENT ADDRESS
    # ==========================================================
    # Screenshot shows:
    # "SAME AS RESIDENTIAL ADDRESS"
    #
    # We intentionally do NOT click it here because we want to
    # test the permanent-address fields separately.
    # ==========================================================


    # ==========================================================
    # PERMANENT ADDRESS LINE 1
    # ==========================================================

    permanent_address_line1 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//textarea[@placeholder='Permanent Address Line 1']"
            )
        )
    )

    permanent_address_line1.send_keys(
        permanent_address_line1_value
    )

    assert permanent_address_line1.get_attribute("value") == \
        permanent_address_line1_value, \
        "Permanent Address Line 1 was not entered correctly"


    # ==========================================================
    # PERMANENT ADDRESS LINE 2
    # ==========================================================

    permanent_address_line2 = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//textarea[@placeholder='Permanent Address Line 2']"
            )
        )
    )

    permanent_address_line2.send_keys(
        permanent_address_line2_value
    )

    assert permanent_address_line2.get_attribute("value") == \
        permanent_address_line2_value, \
        "Permanent Address Line 2 was not entered correctly"


    # ==========================================================
    # PERMANENT STATE
    # ==========================================================

    permanent_state = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[15]"
            )
        )
    )

    permanent_state.click()

    permanent_state_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{permanent_state_value}']"
            )
        )
    )

    driver.execute_script(
                "arguments[0].click();",
                permanent_state_option
            )


    # ==========================================================
    # PERMANENT CITY
    # ==========================================================

    # permanent_city = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[@class='nice-select primary_select form-control'])[16]"
    #         )
    #     )
    # )

    # permanent_city.click()

    # permanent_city_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{permanent_city_value}']"
    #         )
    #     )
    # )

    # permanent_city_option.click()


    # ==========================================================
    # PERMANENT PINCODE
    # ==========================================================

    permanent_pincode = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "permanent_pincode"
            )
        )
    )

    permanent_pincode.send_keys(
        permanent_pincode_value
    )

    assert permanent_pincode.get_attribute("value") == \
        permanent_pincode_value, \
        "Permanent Pincode was not entered correctly"


    # ==========================================================
    # NATIONALITY
    # ==========================================================

    nationality = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "nationality"
            )
        )
    )

    nationality.send_keys(
        nationality_value
    )

    assert nationality.get_attribute("value") == \
        nationality_value, \
        "Nationality was not entered correctly"


    # ==========================================================
    # REQUIRED FIELD VALIDATION
    # ==========================================================

    assert residential_address_line1.get_attribute("value").strip() != "", \
        "Residential Address Line 1 is required"

    assert residential_address_line2.get_attribute("value").strip() != "", \
        "Residential Address Line 2 is required"

    assert residential_pincode.get_attribute("value").strip() != "", \
        "Residential Pincode is required"

    assert permanent_address_line1.get_attribute("value").strip() != "", \
        "Permanent Address Line 1 is required"

    assert permanent_address_line2.get_attribute("value").strip() != "", \
        "Permanent Address Line 2 is required"

    assert permanent_pincode.get_attribute("value").strip() != "", \
        "Permanent Pincode is required"

    assert nationality.get_attribute("value").strip() != "", \
        "Nationality is required"


    # ==========================================================
    # VERIFY ADDRESS VALUES
    # ==========================================================

    print(
        "Residential Address:",
        residential_address_line1.get_attribute("value"),
        residential_address_line2.get_attribute("value"),
        residential_pincode.get_attribute("value")
    )

    print(
        "Permanent Address:",
        permanent_address_line1.get_attribute("value"),
        permanent_address_line2.get_attribute("value"),
        permanent_pincode.get_attribute("value")
    )

    print(
        "Nationality:",
        nationality.get_attribute("value")
    )


    # ==========================================================
    # NEXT BUTTON
    # ==========================================================

    next_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(normalize-space(),'Next')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        next_button
    )

    time.sleep(1)

    try:
        next_button.click()

    except ElementClickInterceptedException:
        driver.execute_script(
            "arguments[0].click();",
            next_button
        )

    time.sleep(3)

    print(
        "Student Add - Residential, Permanent Address "
        "and Other Details completed successfully"
    )
        
        # ==========================================================
    # CURRENT EDUCATION INFO - TEST DATA
    # ==========================================================

    current_academic_year_value = "2026-2027 test2"
    branch_value = "RTM,Marol(West),Mumbai-400021"
    department_value = "CSE-2026"
    program_value = "new-btech"

    semester_value = "Sem-3(CSE)"
    semester_label_value = "Sem-3-cse-label"
    section_value = "CSE-Section A"
    admission_department_value = "Basic Sciences and Humanities"

    economically_backward_class_value = "NO"
    admitted_through_value = "CAP"
    semester_1_division_value = "A"
    semester_2_division_value = "A"


    # ==========================================================
    # CURRENT ACADEMIC YEAR
    # ==========================================================

    current_academic_year = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[17]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        current_academic_year
    )

    current_academic_year.click()

    current_academic_year_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{current_academic_year_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        current_academic_year_option
    )


    # ==========================================================
    # BRANCH
    # ==========================================================

    branch = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[18]"
            )
        )
    )

    branch.click()

    branch_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
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

    department = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[19]"
            )
        )
    )

    department.click()

    department_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
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

    program = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[20]"
            )
        )
    )

    program.click()

    program_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{program_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        program_option
    )


    # ==========================================================
    # SEMESTER
    # ==========================================================

    semester = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[21]"
            )
        )
    )

    semester.click()

    semester_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{semester_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        semester_option
    )


    # ==========================================================
    # SEMESTER LABEL
    # ==========================================================

    semester_label = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[22]"
            )
        )
    )

    semester_label.click()

    semester_label_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{semester_label_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        semester_label_option
    )


    # ==========================================================
    # SECTION
    # ==========================================================

    section = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[23]"
            )
        )
    )

    section.click()

    section_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{section_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        section_option
    )


    # ==========================================================
    # ADMISSION DEPARTMENT
    # ==========================================================

    admission_department = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[24]"
            )
        )
    )

    admission_department.click()

    admission_department_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{admission_department_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        admission_department_option
    )


    # ==========================================================
    # ECONOMICALLY BACKWARD CLASS
    # ==========================================================

    economically_backward_class = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[25]"
            )
        )
    )

    economically_backward_class.click()

    economically_backward_class_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{economically_backward_class_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        economically_backward_class_option
    )


    # ==========================================================
    # ADMITTED THROUGH
    # ==========================================================

    admitted_through = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[26]"
            )
        )
    )

    admitted_through.click()

    admitted_through_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{admitted_through_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        admitted_through_option
    )


    # ==========================================================
    # SEMESTER 1 DIVISION
    # ==========================================================

    semester_1_division = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[27]"
            )
        )
    )

    semester_1_division.click()

    semester_1_division_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{semester_1_division_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        semester_1_division_option
    )


    # ==========================================================
    # SEMESTER 2 DIVISION
    # ==========================================================

    semester_2_division = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[28]"
            )
        )
    )

    semester_2_division.click()

    semester_2_division_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{semester_2_division_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        semester_2_division_option
    )


    # ==========================================================
    # NEXT BUTTON
    # ==========================================================

    next_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(normalize-space(),'Next')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        next_button
    )

    time.sleep(1)

    try:
        next_button.click()

    except ElementClickInterceptedException:
        driver.execute_script(
            "arguments[0].click();",
            next_button
        )

    time.sleep(3)

    print(
        "Student Add - Current Education Information "
        "completed successfully"
    )
    
        # ==========================================================
    # DOCUMENT INFO - TEST DATA
    # ==========================================================

    aadhaar_number_value = "123412341234"
    bank_name_value = "State Bank of India"
    bank_branch_value = "Pune Main Branch"
    bank_account_number_value = "123456789000"
    ifsc_code_value = "SBIN0001234"


    # ==========================================================
    # DOCUMENT FILE PATHS
    # ==========================================================

    # pan_card_file = r"C:\TestData\Documents\pan_card.pdf"
    # birth_certificate_file = r"C:\TestData\Documents\birth_certificate.pdf"
    # fee_payment_receipt_file = r"C:\TestData\Documents\fee_payment_receipt.pdf"
    # caste_certificate_file = r"C:\TestData\Documents\caste_certificate.pdf"
    # disability_certificate_file = r"C:\TestData\Documents\disability_certificate.pdf"


    # ==========================================================
    # VALIDATIONS - TEST DATA
    # ==========================================================

    assert aadhaar_number_value.strip() != "", \
        "Aadhaar Number should not be empty"

    assert aadhaar_number_value.isdigit(), \
        "Aadhaar Number should contain only numbers"

    assert len(aadhaar_number_value) == 12, \
        "Aadhaar Number should contain 12 digits"


    assert bank_name_value.strip() != "", \
        "Bank Name should not be empty"

    assert bank_branch_value.strip() != "", \
        "Bank Branch should not be empty"

    assert bank_account_number_value.strip() != "", \
        "Bank Account Number should not be empty"

    assert bank_account_number_value.isdigit(), \
        "Bank Account Number should contain only numbers"

    assert ifsc_code_value.strip() != "", \
        "IFSC Code should not be empty"


    # ==========================================================
    # AADHAAR NUMBER
    # ==========================================================

    aadhaar_number = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Aadhar Number' "
                "or @placeholder='Aadhaar Number']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        aadhaar_number
    )

    aadhaar_number.clear()

    aadhaar_number.send_keys(
        aadhaar_number_value
    )

    assert aadhaar_number.get_attribute("value") == \
        aadhaar_number_value, \
        "Aadhaar Number was not entered correctly"


    # ==========================================================
    # BANK NAME
    # ==========================================================

    bank_name = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Bank Name']"
            )
        )
    )

    bank_name.clear()

    bank_name.send_keys(
        bank_name_value
    )

    assert bank_name.get_attribute("value") == \
        bank_name_value, \
        "Bank Name was not entered correctly"


    # ==========================================================
    # BANK BRANCH
    # ==========================================================

    bank_branch = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Bank Branch']"
            )
        )
    )

    bank_branch.clear()

    bank_branch.send_keys(
        bank_branch_value
    )

    assert bank_branch.get_attribute("value") == \
        bank_branch_value, \
        "Bank Branch was not entered correctly"


    # ==========================================================
    # BANK ACCOUNT NUMBER
    # ==========================================================

    bank_account_number = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//input[@placeholder='Bank Account Number']"
            )
        )
    )

    bank_account_number.clear()

    bank_account_number.send_keys(
        bank_account_number_value
    )

    assert bank_account_number.get_attribute("value") == \
        bank_account_number_value, \
        "Bank Account Number was not entered correctly"


    # ==========================================================
    # IFSC CODE
    # ==========================================================

    ifsc_code = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "ifsc_code"
            )
        )
    )


    ifsc_code.send_keys(
        ifsc_code_value
    )

    assert ifsc_code.get_attribute("value") == \
        ifsc_code_value, \
        "IFSC Code was not entered correctly"


    # ==========================================================
    # PAN CARD - FILE UPLOAD
    # ==========================================================

    # pan_card = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//input[@type='file'])[1]"
    #         )
    #     )
    # )

    # pan_card.send_keys(
    #     pan_card_file
    # )

    # assert pan_card.get_attribute("value") != "", \
    #     "PAN Card file was not uploaded"


    # ==========================================================
    # BIRTH CERTIFICATE - FILE UPLOAD
    # ==========================================================

    # birth_certificate = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//input[@type='file'])[2]"
    #         )
    #     )
    # )

    # birth_certificate.send_keys(
    #     birth_certificate_file
    # )

    # assert birth_certificate.get_attribute("value") != "", \
    #     "Birth Certificate file was not uploaded"


    # ==========================================================
    # FEE PAYMENT RECEIPT - FILE UPLOAD
    # ==========================================================

    # fee_payment_receipt = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//input[@type='file'])[3]"
    #         )
    #     )
    # )

    # fee_payment_receipt.send_keys(
    #     fee_payment_receipt_file
    # )

    # assert fee_payment_receipt.get_attribute("value") != "", \
    #     "Fee Payment Receipt file was not uploaded"


    # ==========================================================
    # CASTE CERTIFICATE - FILE UPLOAD
    # ==========================================================

    # caste_certificate = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//input[@type='file'])[4]"
    #         )
    #     )
    # )

    # caste_certificate.send_keys(
    #     caste_certificate_file
    # )

    # assert caste_certificate.get_attribute("value") != "", \
    #     "Caste Certificate file was not uploaded"


    # ==========================================================
    # DISABILITY CERTIFICATE - FILE UPLOAD
    # ==========================================================

    # disability_certificate = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//input[@type='file'])[5]"
    #         )
    #     )
    # )

    # disability_certificate.send_keys(
    #     disability_certificate_file
    # )

    # assert disability_certificate.get_attribute("value") != "", \
    #     "Disability Certificate file was not uploaded"


    # ==========================================================
    # REQUIRED FIELD VALIDATION
    # ==========================================================

    assert aadhaar_number.get_attribute("value").strip() != "", \
        "Aadhaar Number is required"

    assert bank_name.get_attribute("value").strip() != "", \
        "Bank Name is required"

    assert bank_branch.get_attribute("value").strip() != "", \
        "Bank Branch is required"

    assert bank_account_number.get_attribute("value").strip() != "", \
        "Bank Account Number is required"

    assert ifsc_code.get_attribute("value").strip() != "", \
        "IFSC Code is required"


    # ==========================================================
    # VERIFY DOCUMENT INFORMATION
    # ==========================================================

    print(
        "Aadhaar Number:",
        aadhaar_number.get_attribute("value")
    )

    print(
        "Bank Name:",
        bank_name.get_attribute("value")
    )

    print(
        "Bank Branch:",
        bank_branch.get_attribute("value")
    )

    print(
        "Bank Account Number:",
        bank_account_number.get_attribute("value")
    )

    print(
        "IFSC Code:",
        ifsc_code.get_attribute("value")
    )

    # print(
    #     "PAN Card uploaded:",
    #     pan_card.get_attribute("value")
    # )

    # print(
    #     "Birth Certificate uploaded:",
    #     birth_certificate.get_attribute("value")
    # )

    # print(
    #     "Fee Payment Receipt uploaded:",
    #     fee_payment_receipt.get_attribute("value")
    # )

    # print(
    #     "Caste Certificate uploaded:",
    #     caste_certificate.get_attribute("value")
    # )

    # print(
    #     "Disability Certificate uploaded:",
    #     disability_certificate.get_attribute("value")
    # )


    # ==========================================================
    # NEXT BUTTON
    # ==========================================================

    next_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(normalize-space(),'Next')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        next_button
    )

    time.sleep(1)

    try:
        next_button.click()

    except ElementClickInterceptedException:
        driver.execute_script(
            "arguments[0].click();",
            next_button
        )

    time.sleep(3)

    print(
        "Student Add - Document Information "
        "completed successfully"
    )
    
    # ==========================================================
# 10TH QUALIFICATION TEST DATA
# ==========================================================

    education_board_10th_value = "CBSE"
    institute_school_10th_value = "Don Bosco School"
    stream_specialization_10th_value = "Science"
    passing_year_10th_value = "2024"
    examination_seat_no_10th_value = "SEAT001"
    percentage_cgpa_10th_value = "85"
    
        # ==========================================================
    # QUALIFICATION DETAIL OF 10TH
    # ==========================================================

    # ==========================================================
    # EDUCATION BOARD 10TH
    # ==========================================================

    education_board_10th = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//label[contains(normalize-space(),'Education Board 10th')]"
                "/following::div[contains(@class,'nice-select')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        education_board_10th
    )

    education_board_10th.click()

    education_board_10th_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{education_board_10th_value}']"
            )
        )
    )

    education_board_10th_option.click()
    
        # ==========================================================
    # INSTITUTE / SCHOOL NAME 10TH
    # ==========================================================

    institute_school_10th = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[contains(@placeholder,'Institute / School Name of 10th')]"
            )
        )
    )

    institute_school_10th.clear()

    institute_school_10th.send_keys(
        institute_school_10th_value
    )

    assert institute_school_10th.get_attribute("value") == \
        institute_school_10th_value
        
        # ==========================================================
    # STREAM SPECIALIZATION 10TH
    # ==========================================================

    stream_specialization_10th = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[contains(@placeholder,'Stream Specialization of 10th')]"
            )
        )
    )

    stream_specialization_10th.clear()

    stream_specialization_10th.send_keys(
        stream_specialization_10th_value
    )

    assert stream_specialization_10th.get_attribute("value") == \
        stream_specialization_10th_value
        
        # ==========================================================
    # PASSING YEAR 10TH
    # ==========================================================

    passing_year_10th = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//label[contains(normalize-space(),'Passing Year 10th')]"
                "/following::div[contains(@class,'nice-select')][1]"
            )
        )
    )

    passing_year_10th.click()

    passing_year_10th_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{passing_year_10th_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        passing_year_10th_option
    )
    
        # ==========================================================
    # EXAMINATION SEAT NO 10TH
    # ==========================================================

    examination_seat_no_10th = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[contains(@placeholder,'Examination Seat No. of 10th')]"
            )
        )
    )

    examination_seat_no_10th.clear()

    examination_seat_no_10th.send_keys(
        examination_seat_no_10th_value
    )

    assert examination_seat_no_10th.get_attribute("value") == \
        examination_seat_no_10th_value
        
        # ==========================================================
    # PERCENTAGE / CGPA / GRADE 10TH
    # ==========================================================

    percentage_cgpa_10th = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[contains(@placeholder,'Percentage CGPA Grade of 10th')]"
            )
        )
    )

    percentage_cgpa_10th.clear()

    percentage_cgpa_10th.send_keys(
        percentage_cgpa_10th_value
    )

    assert percentage_cgpa_10th.get_attribute("value") == \
        percentage_cgpa_10th_value
    
        # ==========================================================
    # REQUIRED FIELD VALIDATION
    # ==========================================================

    assert institute_school_10th.get_attribute("value").strip() != "", \
        "Institute / School Name 10th is required"

    assert stream_specialization_10th.get_attribute("value").strip() != "", \
        "Stream Specialization 10th is required"

    assert examination_seat_no_10th.get_attribute("value").strip() != "", \
        "Examination Seat No 10th is required"

    assert percentage_cgpa_10th.get_attribute("value").strip() != "", \
        "Percentage / CGPA 10th is required"
        
    
    
        
    # # ==========================================================
    # # 12TH TEST DATA
    # # ==========================================================

    # education_board_12th_value = "Education Board Of 12th"
    # institute_12th = "ABC Junior College"
    # stream_12th = "Science"
    # passing_year_12th_value = "2024"
    # seat_no_12th = "123456"
    # percentage_12th = "85.50"


    # # ==========================================================
    # # SCROLL TO 12TH EDUCATION SECTION
    # # ==========================================================

    # driver.execute_script(
    #     "window.scrollBy(0, 1000);"
    # )

    # time.sleep(1)


    # # ==========================================================
    # # EDUCATION BOARD 12TH
    # # ==========================================================

    # education_board_dropdown = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[30]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     education_board_dropdown
    # )

    # time.sleep(1)

    # education_board_dropdown.click()

    # education_board_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') and contains(@class,'open')]"
    #             f"//li[normalize-space()='{education_board_12th_value}']"
    #         )
    #     )
    # )

    # education_board_option.click()


    # # ==========================================================
    # # INSTITUTE / SCHOOL NAME 12TH
    # # ==========================================================

    # institute_12th_field = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Institute / School Name of 12th']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     institute_12th_field
    # )

    # institute_12th_field.clear()
    # institute_12th_field.send_keys(institute_12th)


    # # ==========================================================
    # # STREAM / SPECIALIZATION 12TH
    # # ==========================================================

    # stream_12th_field = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Stream Specialization of 12th']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     stream_12th_field
    # )

    # stream_12th_field.clear()
    # stream_12th_field.send_keys(stream_12th)


    # # ==========================================================
    # # PASSING YEAR 12TH
    # # ==========================================================

    # passing_year_dropdown = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//label[contains(normalize-space(),'PASSING YEAR 12TH')]/following-sibling::div[contains(@class,'nice-select')]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     passing_year_dropdown
    # )

    # time.sleep(1)

    # passing_year_dropdown.click()


    # passing_year_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             f"//li[normalize-space()='{passing_year_12th_value}']"
    #         )
    #     )
    # )

    # passing_year_option.click()


    # # ==========================================================
    # # EXAMINATION SEAT NO 12TH
    # # ==========================================================

    # seat_no_12th_field = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Examination Seat No. of 12th']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     seat_no_12th_field
    # )

    # seat_no_12th_field.clear()
    # seat_no_12th_field.send_keys(seat_no_12th)


    # # ==========================================================
    # # PERCENTAGE / CGPA 12TH
    # # ==========================================================

    # percentage_12th_field = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@placeholder='Percentage CGPA Grade of 12th']"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     percentage_12th_field
    # )

    # percentage_12th_field.clear()
    # percentage_12th_field.send_keys(percentage_12th)


    # # ==========================================================
    # # VERIFY 12TH DATA
    # # ==========================================================

    # assert institute_12th_field.get_attribute("value") == institute_12th

    # assert stream_12th_field.get_attribute("value") == stream_12th

    # assert seat_no_12th_field.get_attribute("value") == seat_no_12th

    # assert percentage_12th_field.get_attribute("value") == percentage_12th

    # assert education_board_dropdown.text.strip() == education_board_12th_value

    # assert passing_year_dropdown.text.strip() == passing_year_12th_value
    
        # ==========================================================
    # MARKSHEET SEMESTER YEAR WISE RESULTS POST GRADUATION
    # ==========================================================

    # marksheet_post_graduation_file = (
    #     r"C:\Users\Snehal Ninawe\OneDrive\Desktop\guhjn.jpg"
    # )

    # # ==========================================================
    # # WAIT FOR POST GRADUATION MARKSHEET FILE INPUT
    # # ==========================================================

    # marksheet_post_graduation = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@type='text' "
    #             "and @id='placeholder_marksheets_all_semester_year_wise_results_post_graduation']"
    #         )
    #     )
    # )

    # ==========================================================
    # SCROLL UNTIL POST GRADUATION MARKSHEET IS VISIBLE
    # ==========================================================

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center', behavior:'smooth'});",
    #     marksheet_post_graduation
    # )

    time.sleep(2)

    # ==========================================================
    # VERIFY POST GRADUATION MARKSHEET IS VISIBLE
    # ==========================================================

    # wait.until(
    #     lambda driver: marksheet_post_graduation.is_displayed()
    # )

    # ==========================================================
    # MAKE FILE INPUT VISIBLE
    # ==========================================================

    # driver.execute_script(
    #     "arguments[0].style.display='block';"
    #     "arguments[0].style.visibility='visible';"
    #     "arguments[0].style.opacity='1';",
    #     marksheet_post_graduation
    # )

    # ==========================================================
    # UPLOAD POST GRADUATION MARKSHEET
    # ==========================================================
    

    # marksheet_post_graduation.send_keys(
    #     marksheet_post_graduation_file
    # )
    
        # ==========================================================
    # SCROLL TO BROWSE BUTTON
    # ==========================================================

    # browse_btn = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "(//button[@type='button'])[42]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     browse_btn
    # )

    # time.sleep(1)

    # ==========================================================
    # CLICK BROWSE BUTTON
    # ==========================================================

    # wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//button[@type='button'])[42]"
    #         )
    #     )
    # ).click()

    # time.sleep(1)

    # ==========================================================
    # GET ACTUAL FILE INPUT
    # ==========================================================

    # file_input = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//input[@type='file']"
    #         )
    #     )
    # )

    # ==========================================================
    # UPLOAD FILE
    # ==========================================================

    # file_input.send_keys(
    #     marksheet_post_graduation_file
    # )

    # ==========================================================
    # VERIFY FILE UPLOAD
    # ==========================================================

#     assert file_input.get_attribute("value") != "", \
#     "Post Graduation Marksheet was not uploaded"

#     print(
#     "Post Graduation Marksheet uploaded successfully"
# )
    # ==========================================================
        # NEXT
        # ==========================================================
    
    next_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(.,'Next')]"
                )
            )
        )
    
    driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            next_button
        )
    
    time.sleep(1)
    
    try:
            next_button.click()
    
    except ElementClickInterceptedException:
            driver.execute_script(
                "arguments[0].click();",
                next_button
            )
    
    time.sleep(3)
    
    #CHECKBOX
    # checkbox = driver.find_element(By.XPATH,"//label[.='Checkbox 1']")
    # checkbox.click()
    
    # time.sleep(2)
    
    # #input
    # input = driver.find_element(By.NAME,"customF[Label 3]")
    # input.send_keys("sds")
    
    # # ==========================================================
    #         # NEXT
    #         # ==========================================================
        
    # next_button = wait.until(
    #             EC.element_to_be_clickable(
    #                 (
    #                     By.XPATH,
    #                     "//button[contains(.,'Next')]"
    #                 )
    #             )
    #         )
        
    # driver.execute_script(
    #             "arguments[0].scrollIntoView({block:'center'});",
    #             next_button
    #         )
        
    # time.sleep(1)
        
    # try:
    #             next_button.click()
        
    # except ElementClickInterceptedException:
    #             driver.execute_script(
    #                 "arguments[0].click();",
    #                 next_button
    #             )
        
    # time.sleep(3)
        
    # #Preview btn
    # preview_btn = driver.find_element(By.XPATH,"//button[@class='primary-btn fix-gr-bg btn-success nxgn_secondary_btn admission-preview-btn-success']")
    # preview_btn.click()
        
    # time.sleep(3)
        
    # #submit-btn
    # submit_btn = driver.find_element(By.XPATH,"//button[@id='previewFieldsSubmitBtn']")
    # submit_btn.click()
    
    