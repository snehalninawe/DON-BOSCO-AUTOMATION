from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException
import time


def test_topic(driver):

    wait = WebDriverWait(driver, 15)

    # # ==========================================================
    # # TEST DATA
    # # ==========================================================

    # branch_value = "RTM,Marol(West),Mumbai-400021"
    # department_value = "CSE-2026"
    # program_value = "new-btech"
    # semester_value = "SEM-4-CSE"
    # subject_value = "COMPUTERSSSSS"
    # unit_value = "Introduction of computer"

    # topic_number_value = "1.1"
    # topic_name_value = "Basics of computerss"
    # planned_lectures_value = "5"
    # planned_completion_date_value = "2026-08-22"

    # bloom_value = "ANALYZE"
    # co_value = "CO1"

    # # ==========================================================
    # # TEST DATA VALIDATION / EDGE CASES
    # # ==========================================================

    # # Topic number should not be empty
    # assert topic_number_value.strip(), \
    #     "Topic number should not be empty"

    # # Topic name should not be empty
    # assert topic_name_value.strip(), \
    #     "Topic name should not be empty"

    # # Planned lectures should be numeric
    # assert planned_lectures_value.isdigit(), \
    #     "Planned lectures should contain only numbers"

    # # Planned lectures should be greater than zero
    # assert int(planned_lectures_value) > 0, \
    #     "Planned lectures should be greater than zero"

    # # Date should not be empty
    # assert planned_completion_date_value.strip(), \
    #     "Planned completion date should not be empty"

    # # Bloom level should not be empty
    # assert bloom_value.strip(), \
    #     "Bloom taxonomy level should not be empty"

    # # CO should not be empty
    # assert co_value.strip(), \
    #     "Course outcome should not be empty"

    # # ==========================================================
    # # OPEN UNIT PLAN
    # # ==========================================================

    leave_menu = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div//span[normalize-space()='Leave']"
            )
        )
    )

    leave_menu.click()

    time.sleep(1)

    # ==========================================================
    # OPEN Leave Type
    # ==========================================================

    leave_type = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space()='Leave Type']")
        )
    )

    leave_type.click()

    time.sleep(2)

    # # ==========================================================
    # # ADD TOPIC
    # # ==========================================================

    add_btn = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "addRowsBtn")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        add_btn
    )

    time.sleep(1)

    driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

    time.sleep(2)
    
    #Input field
    type_field = driver.find_element(By.NAME,"type")
    type_field.send_keys("Sick Leave")
    
    time.sleep(3)
    
    #SUBMIT BTN
    save_btn = driver.find_element(By.ID,"submitButton")
    save_btn.click()