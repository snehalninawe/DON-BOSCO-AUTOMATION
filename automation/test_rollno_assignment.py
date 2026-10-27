from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

from excel_reader import get_all_data
from excel_reader import get_data


# ==========================================================
# TEST DATA
# ==========================================================


# TEST DATA
data = get_data("Roll no")

branch_value = data["Branch"]
department_value = data["Department"]
program_value = data["Program"]
semester_value = data["Semester"]
semester_label_value = data["Semester Label"]
sort_by_value = data["Sort By"]
section_value = data["Section"]
prefix_value = data["Prefix"]
start_from_value = str(data["Start From"])



def test_rollno_assignment(driver):

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
    # OPEN Roll No ASSIGNMENT
    # ==========================================================

    rollno_assignment = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//li[contains(.,'Roll Number Assignment')])[2]"
            )
        )
    )

    rollno_assignment.click()

    # ==========================================================
    # RESET BUTTON
    # ==========================================================

    # reset_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.ID,
    #             "resetbtn"
    #         )
    #     )
    # )

    # reset_button.click()

    # ==========================================================
    # BRANCH DROPDOWN
    # ==========================================================

    branch = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[1]"
            )
        )
    )

    branch.click()

    branch_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{branch_value}']"
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

    # branch_option.click()

    # ==========================================================
    # DEPARTMENT DROPDOWN
    # ==========================================================

    department = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[2]"
            )
        )
    )

    department.click()

    department_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{department_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        department_option
    )

    department_option.click()

    # ==========================================================
    # PROGRAM DROPDOWN
    # ==========================================================

    program = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[3]"
            )
        )
    )

    program.click()

    program_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{program_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        program_option
    )

    program_option.click()

    # ==========================================================
    # SEMESTER DROPDOWN
    # ==========================================================

    semester = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[4]"
            )
        )
    )

    semester.click()

    semester_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{semester_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester_option
    )

    semester_option.click()

    # ==========================================================
    # SEMESTER LABEL DROPDOWN
    # ==========================================================

    semester_label = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[5]"
            )
        )
    )

    semester_label.click()

    semester_label_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{semester_label_value}']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        semester_label_option
    )

    semester_label_option.click()

    # ==========================================================
# SEARCH
# ==========================================================

    search_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.ID,
            "searchBtn"
        )
    )
)

    search_button.click()

# ==========================================================
# WAIT FOR SEARCH RESULTS
# ==========================================================

    driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)

# ==========================================================
# ASSIGN SECTION BUTTON
# ==========================================================

    time.sleep(2)  # Wait for the page to load completely

    assign_rollno_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.ID,
            "openRollNumberModalButton"
        )
    )
)

# ==========================================================
# CLICK ASSIGN ROLL NUMBER
# ==========================================================

    assign_rollno_button.click()


    # ==========================================================
    # SORT BY
    # ==========================================================

    sort_by_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[7]"
            )
        )
    )

    sort_by_dropdown.click()

    sort_by_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//li[normalize-space()='{sort_by_value}']"
            )
        )
    )
    
    driver.execute_script(
        "arguments[0].click();",
        sort_by_option
    )

    # sort_by_option.click()

        # ==========================================================
    # SECTION DROPDOWN
    # ==========================================================

    section_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='nice-select primary_select form-control'])[8]"
            )
        )
    )
    
    driver.execute_script(
        "arguments[0].click();",
        section_dropdown
    )

    section_dropdown.click()

    # ==========================================================
    # SECTION OPTION
    # ==========================================================

    # section_option = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//li[contains(normalize-space(), 'CSE-Section A')]"
    #         )
    #     )
    # )

    # driver.execute_script(
    #     "arguments[0].scrollIntoView({block:'center'});",
    #     section_option
    # )

    # section_option.click()

    # ==========================================================
    # PREFIX
    # ==========================================================

    prefix_field = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "prefix"
            )
        )
    )


    prefix_field.send_keys(prefix_value)
    
    #-------Roll Number Starts from -------
    roll_from_field = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "start_from"
            )
        )
    )

    roll_from_field.clear()
    roll_from_field.send_keys(start_from_value)
    
    
    #--------GENERATE and PREVIEW BUTTONS--------
    generate_preview_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "generateBtn"
            )
        )
    )   
    generate_preview_button.click()

    # ==========================================================
    # SAVE
    # ==========================================================

    save_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "saveBtn"
            )
        )
    )

    save_button.click()
    
    #modal-confirmation popup
    modal_confirmation = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@aria-describedby='swal2-html-container']"
            )
        )
    )
    
    #confirm button
    confirm_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@class='swal2-confirm swal2-styled']"
            )
        )
    )
    confirm_button.click()
    
    #not-confirm button
    # not_confirm_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//button[@class='swal2-cancel swal2-styled']"
    #         )
    #     )
    # )
    # not_confirm_button.click()

    time.sleep(2)  

