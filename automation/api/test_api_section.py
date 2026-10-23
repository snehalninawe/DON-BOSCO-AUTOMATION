# import os
# import sys
# import requests
# from datetime import datetime
# from excel_reader import get_api_data

# # Find the main automation folder
# automation_path = os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__))
# )
# sys.path.insert(0, automation_path)

# from excel_report import create_report


# def test_get_staff_section_filter(auth_token):

#     # Read test data from API_Test_Data.xlsx
#     api_data = get_api_data("Api test data")

#     api_results = []

#     for test_case in api_data:

#         # Run only Staff Section Filter test cases
#         if test_case["API Name"] != "Get Staff Section Filter":
#             continue

#         test_case_id = test_case["Test Case ID"]
#         scenario = test_case["Test Scenario"]
#         section_url = (
#             "https://devops.evolutionco.in/nextgen/api"
#             + test_case["Endpoint"]
#         )

#         # Read the ID from Excel
#         section_payload = {
#             "semester_label_id": test_case["semester_label_id"]
#         }

#         headers = {
#             "Authorization": auth_token,
#             "Content-Type": "application/json",
#             "User-Agent": "insomnia/12.3.1"
#         }

#         try:
#             response = requests.post(
#                 section_url,
#                 json=section_payload,
#                 headers=headers,
#                 timeout=30
#             )

#             expected_status = test_case["Expected Status"]
#             expected_status = int(expected_status) if str(expected_status).isdigit() else None

#             status = (
#                 "PASS"
#                 if expected_status is not None
#                 and response.status_code == expected_status
#                 else "FAIL"
#             )

#             api_results.append({
#                 "API Name": "Staff Section Filter",
#                 "Test Case ID": test_case_id,
#                 "Test Scenario": scenario,
#                 "Method": "POST",
#                 "Endpoint": section_url,
#                 "Test Data / Payload": section_payload,
#                 "Status Code": response.status_code,
#                 "Expected Result": f"HTTP status code {expected_status}",
#                 "Actual Result": response.text,
#                 "Status": status,
#                 "Response Time (ms)": round(
#                     response.elapsed.total_seconds() * 1000, 2
#                 ),
#                 "Error": "" if status == "PASS" else response.text,
#                 "Execution Date & Time": datetime.now().strftime(
#                     "%d-%m-%Y %H:%M:%S"
#                 )
#             })

#             print(f"\nTest Case: {test_case_id}")
#             print(f"Scenario: {scenario}")
#             print(f"Expected Status: {expected_status}")
#             print(f"Actual Status: {response.status_code}")
#             print(f"Response: {response.text}")
#             print(f"Result: {status}")

#         except requests.RequestException as error:
#             api_results.append({
#                 "API Name": "Staff Section Filter",
#                 "Test Case ID": test_case_id,
#                 "Test Scenario": scenario,
#                 "Method": "POST",
#                 "Endpoint": section_url,
#                 "Test Data / Payload": section_payload,
#                 "Status Code": "",
#                 "Expected Result": f"HTTP status code {expected_status}",
#                 "Actual Result": "API request failed",
#                 "Status": "FAIL",
#                 "Response Time (ms)": "",
#                 "Error": str(error),
#                 "Execution Date & Time": datetime.now().strftime(
#                     "%d-%m-%Y %H:%M:%S"
#                 )
#             })

#     # Generate the API-only Excel report
#     create_report([], api_results=api_results, api_only=True)

#     print("\nAPI Excel report generated.")

#     # Fail the pytest test if any API case failed
#     failed_cases = [
#         result for result in api_results
#         if result["Status"] == "FAIL"
#     ]

#     assert api_results, "No matching API test cases found in Excel."
#     assert not failed_cases, f"{len(failed_cases)} API test case(s) failed."







import os
import sys
import json
import requests
from datetime import datetime

# Find the main automation folder
automation_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.insert(0, automation_path)

from excel_reader import get_api_data
from excel_report import create_report

BASE_URL = "https://devops.evolutionco.in/nextgen/api"
SECTION_ENDPOINT = "/v2/get-staff-section-filter"


def test_get_staff_section_filter(get_auth_token):

    # Read all test cases from Excel
    api_data = get_api_data("Api test data")
    api_results = []

    for test_case in api_data:

        if test_case.get("API Name") != "Get Staff Section Filter":
            continue

        test_case_id = str(
            test_case.get("Test Case ID", "")
        ).strip()

        scenario = str(
            test_case.get("Test Scenario", "")
        ).strip()

        endpoint = test_case.get("Endpoint") or SECTION_ENDPOINT

        # Read test details from Excel
        staff_number = int(test_case.get("Staff Number") or 1)
        test_type = str(test_case.get("Test Type") or "").strip()
        priority = str(test_case.get("Priority") or "").strip()

        section_url = BASE_URL + endpoint
        token = get_auth_token(staff_number)

        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "insomnia/12.3.1"
        }

        # Expected results
        expected_status_value = test_case.get("Expected Status")

        expected_status = (
            int(expected_status_value)
            if expected_status_value is not None
            and str(expected_status_value).strip().isdigit()
            else None
        )

        expected_section = str(
            test_case.get("Expected Section") or ""
        ).strip()

        semester_label_id = test_case.get("semester_label_id")

        # Build payload
        payload = {}

        if (
            semester_label_id is not None
            and str(semester_label_id).strip() != ""
        ):
            payload["semester_label_id"] = semester_label_id

        # Default report values
        actual_status = ""
        actual_result = ""
        response_message = ""
        response_time = ""
        speed = "Not Measured"
        report_payload = payload
        error_message = ""
        status = "FAIL"

        try:
            # Send request according to scenario
            if "empty request body" in scenario.lower():

                response = requests.post(
                    section_url,
                    data="",
                    headers=headers,
                    timeout=30
                )

                report_payload = "<Empty request body>"

            elif "invalid data type" in scenario.lower():

                response = requests.post(
                    section_url,
                    json="abc",
                    headers=headers,
                    timeout=30
                )

                report_payload = '"abc"'

            else:

                response = requests.post(
                    section_url,
                    json=payload,
                    headers=headers,
                    timeout=30
                )

                report_payload = payload

            # Response status and time
            actual_status = response.status_code

            response_time = round(
                response.elapsed.total_seconds() * 1000,
                2
            )

            # Categorize speed
            if response_time < 500:
                speed = "Fast"
            elif response_time < 1000:
                speed = "Normal"
            else:
                speed = "Slow"

            # Read response safely
            try:
                response_data = response.json()
            except ValueError:
                response_data = response.text

            # Extract response message
            if isinstance(response_data, dict):

                message_value = (
                    response_data.get("message")
                    or response_data.get("detail")
                    or response_data.get("error")
                    or ""
                )

                if isinstance(message_value, (dict, list)):
                    response_message = json.dumps(
                        message_value,
                        ensure_ascii=False
                    )
                else:
                    response_message = str(message_value)

            elif isinstance(response_data, str):
                response_message = response_data

            actual_result = (
                f"HTTP {actual_status}; "
                f"Response: "
                f"{json.dumps(response_data, ensure_ascii=False)}"
            )

            # Validate expected HTTP status
            if (
                expected_status is not None
                and actual_status == expected_status
            ):
                status = "PASS"
            else:
                status = "FAIL"
                error_message = (
                    f"Expected HTTP {expected_status}, "
                    f"received HTTP {actual_status}"
                )

            # Validate expected section
            actual_sections = []

            if isinstance(response_data, dict):

                response_sections = response_data.get("data", [])

                if isinstance(response_sections, list):
                    actual_sections = [
                        item.get("section_name")
                        for item in response_sections
                        if isinstance(item, dict)
                        and item.get("section_name")
                    ]

            if expected_section:

                if expected_section in actual_sections:

                    if status == "PASS":
                        error_message = ""

                else:
                    status = "FAIL"
                    error_message = (
                        f"Expected section '{expected_section}', "
                        f"received {actual_sections}"
                    )

            # API_SEC_002: verify empty data for ID 188
            if test_case_id == "API_SEC_002":

                if (
                    not isinstance(response_data, dict)
                    or response_data.get("data") != []
                ):
                    status = "FAIL"
                    error_message = (
                        "Expected empty data for semester_label_id 188"
                    )

            print(f"\nTest Case: {test_case_id}")
            print(f"Staff Number: {staff_number}")
            print(f"Test Type: {test_type}")
            print(f"Priority: {priority}")
            print(f"Status Code: {actual_status}")
            print(f"Response Message: {response_message}")
            print(f"Response Time: {response_time} ms")
            print(f"Speed: {speed}")
            print(f"Status: {status}")
            print(f"Error: {error_message}")

        except requests.RequestException as error:

            report_payload = (
                "<Empty request body>"
                if "empty request body" in scenario.lower()
                else '"abc"'
                if "invalid data type" in scenario.lower()
                else payload
            )

            actual_result = "API request failed"
            response_message = "Request failed"
            error_message = str(error)
            status = "FAIL"

        # Store result for Excel report
        api_results.append({
            "API Name": "Get Staff Section Filter",
            "Staff Number": staff_number,
            "Test Case ID": test_case_id,
            "Test Type": test_type,
            "Priority": priority,
            "Test Scenario": scenario,
            "Method": test_case.get("Method") or "POST",
            "Endpoint": endpoint,
            "Test Data / Payload": report_payload,
            "Status Code": actual_status,
            "Expected Result": (
                f"HTTP {expected_status}"
                + (
                    f"; Section: {expected_section}"
                    if expected_section else ""
                )
                + (
                    "; Empty data"
                    if test_case_id == "API_SEC_002" else ""
                )
            ),
            "Actual Result": actual_result,
            "Response Message": response_message,
            "Speed": speed,
            "Status": status,
            "Response Time (ms)": response_time,
            "Error": error_message,
            "Execution Date & Time": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        })

    # Generate report once
    create_report(
        [],
        api_results=api_results,
        api_only=True
    )

    print(f"\nTotal test cases executed: {len(api_results)}")
    print("API test execution report generated.")

    failed_cases = [
        result for result in api_results
        if result["Status"] == "FAIL"
    ]

    assert api_results, "No matching API test cases found in Excel."

    assert not failed_cases, (
        f"{len(failed_cases)} test case(s) failed. "
        "Please check the Excel report."
    )
