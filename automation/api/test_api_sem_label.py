
import os
import sys
import requests
from datetime import datetime

# Import the API report function
automation_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.insert(0, automation_path)

from excel_report import create_report


def test_get_staff_semester_label_filter(auth_token):

    # ==========================================================
    # API URL
    # ==========================================================

    semester_label_url = (
        "https://devops.evolutionco.in/nextgen/api/v2/"
        "get-staff-semester-label-filter"
    )

    # ==========================================================
    # TEST DATA
    # ==========================================================

    semester_label_payload = {
        "semester_id": 335
    }

    # ==========================================================
    # HEADERS
    # ==========================================================

    headers = {
        "Authorization": auth_token,
        "Content-Type": "application/json"
    }

    api_results = []

    try:
        # ======================================================
        # SEND POST REQUEST
        # ======================================================

        response = requests.post(
            semester_label_url,
            json=semester_label_payload,
            headers=headers,
            timeout=30
        )

        response_time = round(
            response.elapsed.total_seconds() * 1000,
            2
        )

        # ======================================================
        # VERIFY STATUS CODE
        # ======================================================

        status = (
            "PASS"
            if response.status_code == 200
            else "FAIL"
        )

        # ======================================================
        # STORE API RESULT FOR EXCEL REPORT
        # ======================================================

        api_results.append({
            "API Name": "Staff Semester Label Filter",
            "Test Case ID": "API-SEMESTER-LABEL-001",
            "Test Scenario": (
                "Verify semester label filter using semester ID"
            ),
            "Method": "POST",
            "Endpoint": semester_label_url,
            "Test Data / Payload": semester_label_payload,
            "Status Code": response.status_code,
            "Expected Result": "HTTP status code 200",
            "Actual Result": response.text,
            "Status": status,
            "Response Time (ms)": response_time,
            "Error": (
                ""
                if status == "PASS"
                else response.text
            ),
            "Execution Date & Time": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        })

        # Generate API-only Excel report
        create_report(
            [],
            api_results=api_results,
            api_only=True
        )

        # ======================================================
        # PRINT RESULTS
        # ======================================================

        print("\nAPI Name: Staff Semester Label Filter")
        print("Status Code:", response.status_code)
        print("Result:", status)
        print("Response Time:", response_time, "ms")
        print("API Response:", response.text)

        # Fail the test if the status code is not 200
        assert response.status_code == 200, (
            f"Expected status code 200, "
            f"but received {response.status_code}. "
            f"Response: {response.text}"
        )

    except requests.RequestException as error:

        # Record API connection/request errors
        api_results.append({
            "API Name": "Staff Semester Label Filter",
            "Test Case ID": "API-SEMESTER-LABEL-001",
            "Test Scenario": (
                "Verify semester label filter using semester ID"
            ),
            "Method": "POST",
            "Endpoint": semester_label_url,
            "Test Data / Payload": semester_label_payload,
            "Status Code": "",
            "Expected Result": "HTTP status code 200",
            "Actual Result": "API request failed",
            "Status": "FAIL",
            "Response Time (ms)": "",
            "Error": str(error),
            "Execution Date & Time": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        })

        create_report(
            [],
            api_results=api_results,
            api_only=True
        )

        raise