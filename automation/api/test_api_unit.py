
import os
import sys
import requests
from datetime import datetime

# Find the main automation folder
automation_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.insert(0, automation_path)

from excel_report import create_report


def test_get_staff_unit_filter(auth_token):

    # ==========================================
    # API URL
    # ==========================================

    unit_url = (
        "https://devops.evolutionco.in/nextgen/api/v2/"
        "get-staff-unit-filter"
    )

    # ==========================================
    # REQUEST PAYLOAD
    # ==========================================

    unit_payload = {
        "un_semester_label_id": 187,
        "un_subject_id": 401
    }

    # ==========================================
    # HEADERS
    # ==========================================

    headers = {
        "Authorization": auth_token,
        "Content-Type": "application/json"
    }

    api_results = []

    # ==========================================
    # SEND API REQUEST
    # ==========================================

    try:

        start_time = datetime.now()

        response = requests.post(
            unit_url,
            json=unit_payload,
            headers=headers,
            timeout=30
        )

        response_time = round(
            response.elapsed.total_seconds() * 1000,
            2
        )

        # ==========================================
        # CHECK RESPONSE STATUS
        # ==========================================

        status = (
            "PASS"
            if response.status_code == 200
            else "FAIL"
        )

        # ==========================================
        # SAVE API RESULT
        # ==========================================

        api_results.append({
            "API Name": "Staff Unit Filter",
            "Test Case ID": "API-UNIT-001",
            "Test Scenario": (
                "Verify staff unit filter API "
                "using semester label and subject"
            ),
            "Method": "POST",
            "Endpoint": unit_url,
            "Test Data / Payload": unit_payload,
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

        # ==========================================
        # GENERATE API-ONLY EXCEL REPORT
        # ==========================================

        create_report(
            [],
            api_results=api_results,
            api_only=True
        )

        print("\nAPI Name: Staff Unit Filter")
        print("API Status Code:", response.status_code)
        print("API Result:", status)
        print("Response Time:", response_time, "ms")
        print("API Excel report generated.")

        # Fail the test if the status code is not 200
        assert response.status_code == 200, (
            f"Expected status code 200, "
            f"but received {response.status_code}. "
            f"Response: {response.text}"
        )

    # ==========================================
    # HANDLE REQUEST ERRORS
    # ==========================================

    except requests.RequestException as error:

        api_results.append({
            "API Name": "Staff Unit Filter",
            "Test Case ID": "API-UNIT-001",
            "Test Scenario": (
                "Verify staff unit filter API"
            ),
            "Method": "POST",
            "Endpoint": unit_url,
            "Test Data / Payload": unit_payload,
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