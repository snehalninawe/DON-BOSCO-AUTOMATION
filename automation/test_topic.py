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

    unit_plan_menu = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div//span[normalize-space()='Unit Plan']"
            )
        )
    )

    unit_plan_menu.click()

    time.sleep(1)

    # ==========================================================
    # OPEN TOPIC
    # ==========================================================

    topic = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space()='Topic']")
        )
    )

    topic.click()

    time.sleep(2)

    # # ==========================================================
    # # ADD TOPIC
    # # ==========================================================

    # add_btn = wait.until(
    #     EC.element_to_be_clickable(
    #         (By.ID, "attnAjaxAddRowsBtn")
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     add_btn
    # )

    # time.sleep(1)

    # try:
    #     add_btn.click()
    # except ElementClickInterceptedException:
    #     driver.execute_script(
    #         "arguments[0].click();",
    #         add_btn
    #     )

    # time.sleep(2)

    # # ==========================================================
    # # BRANCH
    # # ==========================================================

    # branch = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[1]"
    #         )
    #     )
    # )

    # branch.click()

    # time.sleep(1)

    # branch_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{branch_value}']"
    #         )
    #     )
    # )

    # branch_option.click()

    # time.sleep(1)

    # # Verify branch selection
    # branch_selected = driver.find_element(
    #     By.XPATH,
    #     "(//div[contains(@class,'nice-select') "
    #     "and contains(@class,'primary_select')])[1]"
    # )

    # assert branch_value in branch_selected.text, \
    #     "Branch was not selected correctly"

    # # ==========================================================
    # # DEPARTMENT
    # # ==========================================================

    # department = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[2]"
    #         )
    #     )
    # )

    # department.click()

    # time.sleep(1)

    # department_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{department_value}']"
    #         )
    #     )
    # )

    # department_option.click()

    # time.sleep(1)

    # # ==========================================================
    # # PROGRAM
    # # ==========================================================

    # program_dropdown = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[3]"
    #         )
    #     )
    # )

    # program_dropdown.click()

    # time.sleep(1)

    # program_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{program_value}']"
    #         )
    #     )
    # )

    # program_option.click()

    # time.sleep(1)

    # # ==========================================================
    # # SEMESTER
    # # ==========================================================

    # semester_dropdown = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[4]"
    #         )
    #     )
    # )

    # semester_dropdown.click()

    # time.sleep(1)

    # semester_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{semester_value}']"
    #         )
    #     )
    # )

    # semester_option.click()

    # time.sleep(1)

    # # ==========================================================
    # # SUBJECT
    # # ==========================================================

    # subject_dropdown = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[5]"
    #         )
    #     )
    # )

    # subject_dropdown.click()

    # time.sleep(1)

    # subject_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{subject_value}']"
    #         )
    #     )
    # )

    # subject_option.click()

    # time.sleep(1)

    # # ==========================================================
    # # UNIT
    # # ==========================================================

    # unit_dropdown = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'select_unit_plan_option')]"
    #         )
    #     )
    # )

    # unit_dropdown.click()

    # time.sleep(1)

    # unit_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{unit_value}']"
    #         )
    #     )
    # )

    # unit_option.click()

    # time.sleep(1)

    # # ==========================================================
    # # FETCH
    # # ==========================================================

    # fetch_btn = wait.until(
    #     EC.element_to_be_clickable(
    #         (By.ID, "fetchTopicBtn")
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     fetch_btn
    # )

    # time.sleep(1)

    # fetch_btn.click()

    # # Give UI time to create/fetch topic row
    # time.sleep(2)

    # # Verify topic fields appeared
    # topic_number = wait.until(
    #     EC.visibility_of_element_located(
    #         (By.NAME, "topic_no[]")
    #     )
    # )

    # topic_name = wait.until(
    #     EC.visibility_of_element_located(
    #         (By.NAME, "topic_title[]")
    #     )
    # )

    # planned_lectures = wait.until(
    #     EC.visibility_of_element_located(
    #         (By.NAME, "planned_lectures[]")
    #     )
    # )

    # # ==========================================================
    # # TOPIC NUMBER
    # # ==========================================================

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     topic_number
    # )

    # topic_number.send_keys(topic_number_value)

    # time.sleep(1)

    # # Edge case
    # assert topic_number.get_attribute("value").strip() != "", \
    #     "Topic number should not be empty"

    # # ==========================================================
    # # TOPIC NAME
    # # ==========================================================

    # topic_name.send_keys(topic_name_value)

    # time.sleep(1)

    # # Edge case
    # assert topic_name.get_attribute("value").strip() != "", \
    #     "Topic name should not be empty"

    # # ==========================================================
    # # PLANNED LECTURES
    # # ==========================================================

    # planned_lectures.send_keys(planned_lectures_value)

    # time.sleep(1)

    # # Edge cases
    # actual_lectures = planned_lectures.get_attribute("value")

    # assert actual_lectures.isdigit(), \
    #     "Planned lectures must be numeric"

    # assert int(actual_lectures) > 0, \
    #     "Planned lectures must be greater than zero"

    # # ==========================================================
    # # PLANNED COMPLETION DATE
    # # ==========================================================

    # planned_completion_date = wait.until(
    #     EC.presence_of_element_located(
    #         (By.NAME, "planned_completion_date[]")
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     planned_completion_date
    # )

    # time.sleep(1)

    # driver.execute_script(
    #     "arguments[0].value = arguments[1];",
    #     planned_completion_date,
    #     planned_completion_date_value
    # )

    # driver.execute_script(
    #     """
    #     arguments[0].dispatchEvent(
    #         new Event('input', {bubbles:true})
    #     );

    #     arguments[0].dispatchEvent(
    #         new Event('change', {bubbles:true})
    #     );
    #     """,
    #     planned_completion_date
    # )

    # time.sleep(1)

    # # Edge case
    # assert planned_completion_date.get_attribute("value") == \
    #        planned_completion_date_value, \
    #        "Planned completion date was not entered correctly"

    # # ==========================================================
    # # BLOOM TAXONOMY
    # # ==========================================================

    # bloom = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[8]"
    #         )
    #     )
    # )

    # bloom.click()

    # time.sleep(1)

    # bloom_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{bloom_value}']"
    #         )
    #     )
    # )

    # bloom_option.click()

    # time.sleep(1)

    # # ==========================================================
    # # COURSE OUTCOME
    # # ==========================================================

    # course_outcome = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//div[contains(@class,'nice-select') "
    #             "and contains(@class,'primary_select')])[9]"
    #         )
    #     )
    # )

    # course_outcome.click()

    # time.sleep(1)

    # course_outcome_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//div[contains(@class,'nice-select') "
    #             "and contains(@class,'open')]"
    #             f"//li[normalize-space()='{co_value}']"
    #         )
    #     )
    # )

    # course_outcome_option.click()

    # time.sleep(1)

    # # ==========================================================
    # # FINAL VALIDATION BEFORE SAVE
    # # ==========================================================

    # assert topic_number.get_attribute("value") == \
    #        topic_number_value, \
    #        "Topic number value is incorrect"

    # assert topic_name.get_attribute("value") == \
    #        topic_name_value, \
    #        "Topic name value is incorrect"

    # assert planned_lectures.get_attribute("value") == \
    #        planned_lectures_value, \
    #        "Planned lectures value is incorrect"

    # assert planned_completion_date.get_attribute("value") == \
    #        planned_completion_date_value, \
    #        "Completion date is incorrect"

    # assert bloom_value in bloom.text, \
    #        "Bloom taxonomy value was not selected"

    # assert co_value in course_outcome.text, \
    #        "Course outcome was not selected"

    # time.sleep(2)

    # # ==========================================================
    # # SAVE
    # # ==========================================================

    # save = wait.until(
    #     EC.element_to_be_clickable(
    #         (By.ID, "submitButton")
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     save
    # )

    # time.sleep(2)

    # try:
    #     save.click()
    # except ElementClickInterceptedException:
    #     driver.execute_script(
    #         "arguments[0].click();",
    #         save
    #     )

    # time.sleep(3)

    # print("Topic created successfully")
    
    
    
        # ==========================================================
    # EDIT TOPIC
    # ==========================================================

    # ----------------------------------------------------------
    # EDIT TEST DATA
    # ----------------------------------------------------------

    updated_topic_number_value = "1.2"
    updated_topic_name_value = "Advanced Computer Networks"
    updated_planned_lectures_value = "8"
    updated_planned_completion_date_value = "2026-08-25"
    updated_bloom_value = "EVALUATE"
    updated_co_value = "CO2"


    # ==========================================================
    # VALIDATE EDIT TEST DATA
    # ==========================================================

    assert updated_topic_number_value.strip(), \
        "Updated topic number should not be empty"

    assert updated_topic_name_value.strip(), \
        "Updated topic name should not be empty"

    assert updated_planned_lectures_value.isdigit(), \
        "Updated planned lectures must be numeric"

    assert int(updated_planned_lectures_value) > 0, \
        "Updated planned lectures must be greater than zero"

    assert updated_planned_completion_date_value.strip(), \
        "Updated completion date should not be empty"

    assert updated_bloom_value.strip(), \
        "Updated Bloom level should not be empty"

    assert updated_co_value.strip(), \
        "Updated CO should not be empty"


    # ==========================================================
    # LOCATE CREATED TOPIC ROW
    # ==========================================================

    # topic_row = wait.until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             f"//tr[.//td[normalize-space()='{topic_name_value}']]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     topic_row
    # )

    # time.sleep(1)


    # ==========================================================
    # OPEN THREE-DOT MENU
    # ==========================================================

    three_dots = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//button[@class='attn-ajax-action_button'])[8]"
            )
        )
    )
    driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    three_dots
)

    three_dots.click()

    time.sleep(1)


    # ==========================================================
    # CLICK EDIT
    # ==========================================================

    edit_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[@class='attn-ajax-action_item_list asign-btn'])[8]"
            )
        )
    )
    driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    edit_button
)

    edit_button.click()

    time.sleep(2)


    # ==========================================================
    # VERIFY EDIT FORM LOADED
    # ==========================================================
    
    
    

    edit_topic_number = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "topic_no[]")
        )
    )

    edit_topic_name = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "topic_title[]")
        )
    )

    edit_planned_lectures = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "planned_lectures[]")
        )
    )

    edit_completion_date = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "planned_completion_date[]")
        )
    )

    time.sleep(1)


    # ==========================================================
    # EDIT TOPIC NUMBER
    # ==========================================================
    
    driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    edit_topic_number
)
    
    time.sleep(1)

    edit_topic_number.click()
    edit_topic_number.send_keys(Keys.CONTROL, "a")
    edit_topic_number.send_keys(updated_topic_number_value)

    time.sleep(1)

    assert edit_topic_number.get_attribute("value") == \
        updated_topic_number_value, \
        "Updated topic number was not entered correctly"


    # ==========================================================
    # EDIT TOPIC NAME
    # ==========================================================

    edit_topic_name.click()
    edit_topic_name.send_keys(Keys.CONTROL, "a")
    edit_topic_name.send_keys(updated_topic_name_value)

    time.sleep(1)

    assert edit_topic_name.get_attribute("value") == \
        updated_topic_name_value, \
        "Updated topic name was not entered correctly"


    # ==========================================================
    # EDIT PLANNED LECTURES
    # ==========================================================
    
    driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    edit_completion_date
)

    time.sleep(1)
    
    driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    edit_planned_lectures
)

    time.sleep(1)

    edit_planned_lectures.click()
    edit_planned_lectures.send_keys(Keys.CONTROL, "a")
    edit_planned_lectures.send_keys(updated_planned_lectures_value)

    time.sleep(1)

    actual_lectures = edit_planned_lectures.get_attribute("value")

    assert actual_lectures.isdigit(), \
        "Updated planned lectures must contain only numbers"

    assert int(actual_lectures) > 0, \
        "Updated planned lectures must be greater than zero"

    assert actual_lectures == updated_planned_lectures_value, \
        "Updated planned lectures value is incorrect"


    # ==========================================================
    # EDIT COMPLETION DATE
    # ==========================================================

    driver.execute_script(
        "arguments[0].value = arguments[1];",
        edit_completion_date,
        updated_planned_completion_date_value
    )

    driver.execute_script(
        """
        arguments[0].dispatchEvent(
            new Event('input', {bubbles:true})
        );

        arguments[0].dispatchEvent(
            new Event('change', {bubbles:true})
        );
        """,
        edit_completion_date
    )

    time.sleep(1)

    assert edit_completion_date.get_attribute("value") == \
        updated_planned_completion_date_value, \
        "Updated completion date is incorrect"


    # ==========================================================
    # EDIT BLOOM TAXONOMY
    # ==========================================================

    edit_bloom = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[8]"
            )
        )
    )
    driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    edit_bloom
)

    time.sleep(1)

    edit_bloom.click()

    time.sleep(1)

    edit_bloom_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{updated_bloom_value}']"
            )
        )
    )

    edit_bloom_option.click()

    time.sleep(1)

    assert updated_bloom_value in edit_bloom.text, \
        "Updated Bloom taxonomy was not selected"


    # ==========================================================
    # EDIT COURSE OUTCOME
    # ==========================================================

    edit_co = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[contains(@class,'nice-select') "
                "and contains(@class,'primary_select')])[9]"
            )
        )
    )
    driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    edit_co
)

    time.sleep(1)


    edit_co.click()

    time.sleep(1)

    edit_co_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'nice-select') "
                "and contains(@class,'open')]"
                f"//li[normalize-space()='{updated_co_value}']"
            )
        )
    )

    edit_co_option.click()

    time.sleep(1)

    assert updated_co_value in edit_co.text, \
        "Updated Course Outcome was not selected"


    # ==========================================================
    # FINAL EDIT VALIDATION
    # ==========================================================

    assert edit_topic_number.get_attribute("value") == \
        updated_topic_number_value

    assert edit_topic_name.get_attribute("value") == \
        updated_topic_name_value

    assert edit_planned_lectures.get_attribute("value") == \
        updated_planned_lectures_value

    assert edit_completion_date.get_attribute("value") == \
        updated_planned_completion_date_value

    assert updated_bloom_value in edit_bloom.text

    assert updated_co_value in edit_co.text


    # ==========================================================
    # SAVE EDIT
    # ==========================================================

    update_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "submitButton")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        update_button
    )

    time.sleep(1)

    try:
        update_button.click()

    except ElementClickInterceptedException:
        driver.execute_script(
            "arguments[0].click();",
            update_button
        )

    time.sleep(3)
    
        # ==========================================================
    # TOPIC DETAIL (EYE)
    # ==========================================================

    # topic_detail = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "(//a[contains(@class,'topic-detail-trigger')])[8]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     topic_detail
    # )

    # time.sleep(1)

    # try:
    #     topic_detail.click()
    # except ElementClickInterceptedException:
    #     driver.execute_script(
    #         "arguments[0].click();",
    #         topic_detail
    #     )

    # time.sleep(2)
    
   # ==========================================================
# DELETE TOPIC
# ==========================================================

    delete = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "(//a[contains(@class,'attn-ajax-delete-button-datatable')])[8]"
        )
    )
)

    driver.execute_script(
    "arguments[0].scrollIntoView();",
    delete
)

    time.sleep(1)

    driver.execute_script(
    "arguments[0].click();",
    delete
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

    confirm_button = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//button[contains(@class,'swal2-confirm') "
            "and contains(@class,'swal2-styled')]"
        )
    )
)

    driver.execute_script(
    "arguments[0].scrollIntoView();",
    confirm_button
)

    time.sleep(1)

    try:
        confirm_button.click()
    except ElementClickInterceptedException:
        driver.execute_script(
            "arguments[0].click();",
            confirm_button
        )

    time.sleep(2)   


   # ==========================================================
# VERIFY EDIT WAS SAVED
# ==========================================================

    # time.sleep(2)

# Wait until updated topic appears
#     updated_topic = wait.until(
#     EC.visibility_of_element_located(
#         (
#             By.XPATH,
#             f"//*[contains(normalize-space(),"
#             f"'{updated_topic_name_value}')]"
#         )
#     )
# )

#     driver.execute_script(
#     "arguments[0].scrollIntoView({block:'center'});",
#     updated_topic
# )

#     time.sleep(1)

#     assert updated_topic_name_value in updated_topic.text, \
#     "Edited topic name was not saved"


    print("Topic created and edited successfully")