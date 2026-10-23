
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


def test_get_staff_topic_filter(auth_token):

    # ==========================================================
    # API DETAILS
    # ==========================================================

    topic_url = (
        "https://devops.evolutionco.in/nextgen/api/v2/"
        "get-staff-topic-filter"
    )

    topic_payload = {
        "lesson_id": 304
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
            topic_url,
            json=topic_payload,
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
        # STORE API RESULT FOR EXCEL REPORT
        # ======================================================

        api_results.append({
            "API Name": "Staff Topic Filter",
            "Test Case ID": "API-TOPIC-001",
            "Test Scenario": (
                "Verify staff topic filter API "
                "using lesson ID"
            ),
            "Method": "POST",
            "Endpoint": topic_url,
            "Test Data / Payload": topic_payload,
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

        print("\nAPI Name: Staff Topic Filter")
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
            "API Name": "Staff Topic Filter",
            "Test Case ID": "API-TOPIC-001",
            "Test Scenario": "Verify staff topic filter API",
            "Method": "POST",
            "Endpoint": topic_url,
            "Test Data / Payload": topic_payload,
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