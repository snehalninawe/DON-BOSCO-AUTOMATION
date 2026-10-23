
import time
import traceback


def retry_test(
    test_function,
    max_retries=3,
    retry_test="YES"
):
    """
    Run a Selenium test with retry support.

    max_retries=3 means a maximum of 3 total attempts.
    retry_test="YES" enables retries.
    """

    results = []
    max_attempts = max_retries if retry_test.upper() == "YES" else 1

    for attempt in range(1, max_attempts + 1):
        start_time = time.perf_counter()

        result = {
            "Attempt": attempt,
            "Status": "PASS",
            "Error": "",
            "Execution Time (seconds)": 0
        }

        try:
            test_function()

        except Exception:
            result["Status"] = "FAIL"
            result["Error"] = traceback.format_exc()

        result["Execution Time (seconds)"] = round(
            time.perf_counter() - start_time, 2
        )

        results.append(result)

        if result["Status"] == "PASS":
            break

    final_status = results[-1]["Status"]

    for result in results:
        result["Final Status"] = final_status

    return results
