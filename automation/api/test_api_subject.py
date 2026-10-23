
import os
import sys
import requests
from datetime import datetime

# Get automation folder path
automation_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.insert(0, automation_path)

from excel_report import create_report


def test_get_staff_subject_filter(auth_token):

    # ==========================================================
    # API DETAILS
    # ==========================================================

    subject_url = (
        "https://devops.evolutionco.in/nextgen/api/v2/"
        "get-staff-subject-filter"
    )

    subject_payload = {
        "semester_label_id": 187,
        "section_id": 107
    }

    headers = {
        "Authorization": auth_token,
        "Content-Type": "application/json"
    }

    api_results = []

    # ==========================================================
    # SEND API REQUEST
    # ==========================================================

    try:
        response = requests.post(
            subject_url,
            json=subject_payload,
            headers=headers,
            timeout=30
        )

        response_time = round(
            response.elapsed.total_seconds() * 1000,
            2
        )

        # ======================================================
        # VALIDATE STATUS CODE
        # ======================================================

        status = (
            "PASS"
            if response.status_code == 200
            else "FAIL"
        )

        # ======================================================
        # STORE RESULT FOR EXCEL REPORT
        # ======================================================

        api_results.append({
            "API Name": "Staff Subject Filter",
            "Test Case ID": "API-SUBJECT-001",
            "Test Scenario": (
                "Verify staff subject filter API "
                "using semester label ID and section ID"
            ),
            "Method": "POST",
            "Endpoint": subject_url,
            "Test Data / Payload": subject_payload,
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

        # ======================================================
        # GENERATE API-ONLY EXCEL REPORT
        # ======================================================

        create_report(
            [],
            api_results=api_results,
            api_only=True
        )

        # ======================================================
        # PRINT RESULT
        # ======================================================

        print("\nAPI Name: Staff Subject Filter")
        print("API Status Code:", response.status_code)
        print("API Result:", status)
        print("Response Time:", response_time, "ms")
        print("API Response:", response.text)

        # ======================================================
        # ASSERTION
        # ======================================================

        assert response.status_code == 200, (
            f"Expected status code 200, "
            f"but received {response.status_code}. "
            f"Response: {response.text}"
        )

    except requests.RequestException as error:

        # ======================================================
        # SAVE REQUEST ERROR IN EXCEL REPORT
        # ======================================================

        api_results.append({
            "API Name": "Staff Subject Filter",
            "Test Case ID": "API-SUBJECT-001",
            "Test Scenario": "Verify staff subject filter API",
            "Method": "POST",
            "Endpoint": subject_url,
            "Test Data / Payload": subject_payload,
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