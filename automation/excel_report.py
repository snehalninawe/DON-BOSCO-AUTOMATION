
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
from datetime import datetime
import os


# ==========================================================
# DOWNLOAD FOLDER
# ==========================================================

DOWNLOAD_FOLDER = os.path.join(
    os.path.expanduser("~"),
    "Downloads"
)

os.makedirs(
    DOWNLOAD_FOLDER,
    exist_ok=True
)


# ==========================================================
# REPORT FILE
# ==========================================================

timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

REPORT_FILE = os.path.join(
    DOWNLOAD_FOLDER,
    f"test_execution_report_{timestamp}.xlsx"
)


# ==========================================================
# CREATE REPORT
# ==========================================================

def create_report(results):

    workbook = Workbook()

    # ======================================================
    # SUMMARY SHEET
    # ======================================================

    summary = workbook.active
    summary.title = "Summary"

    # ======================================================
    # GET MODULES DYNAMICALLY
    # ======================================================

    modules = []

    for result in results:

        module = result.get(
            "Module",
            result.get(
                "Test Case",
                "Unknown"
            )
        )

        if module not in modules:

            modules.append(module)

    # ======================================================
    # SUMMARY TITLE
    # ======================================================

    summary["A1"] = "Test Execution Summary"

    summary["A1"].font = Font(
        bold=True,
        size=14
    )

    summary.merge_cells(
        "A1:I1"
    )

    summary["A1"].alignment = Alignment(
        horizontal="center"
    )

    # ======================================================
    # SUMMARY HEADER
    # ======================================================

    summary.append([])

    summary.append([
        "Module",
        "Total Test Cases",
        "Passed",
        "Failed",
        "First Attempt Failures",
        "Retry Attempts",
        "Passed After Retry",
        "Total Attempts",
        "Pass %"
    ])

    # ======================================================
    # MODULE-WISE SUMMARY
    # ======================================================

    for module in modules:

        module_results = [
            result
            for result in results
            if result.get(
                "Module",
                result.get(
                    "Test Case",
                    "Unknown"
                )
            ) == module
        ]

        # --------------------------------------------------
        # UNIQUE TEST DATA
        # --------------------------------------------------

        test_cases = []

        for result in module_results:

            test_data = result.get(
                "Test Data",
                ""
            )

            if test_data not in test_cases:

                test_cases.append(
                    test_data
                )

        total = len(test_cases)

        # --------------------------------------------------
        # FINAL STATUS
        # --------------------------------------------------

        final_status = {}

        for result in module_results:

            test_data = result.get(
                "Test Data",
                ""
            )

            status = result.get(
                "Final Status",
                ""
            )

            if status == "PASS":

                final_status[
                    test_data
                ] = "PASS"

            elif status == "FAIL":

                final_status[
                    test_data
                ] = "FAIL"

        # --------------------------------------------------
        # PASSED
        # --------------------------------------------------

        passed = sum(
            1
            for status in final_status.values()
            if status == "PASS"
        )

        # --------------------------------------------------
        # FAILED
        # --------------------------------------------------

        failed = sum(
            1
            for status in final_status.values()
            if status == "FAIL"
        )

        # --------------------------------------------------
        # FIRST ATTEMPT FAILURES
        # --------------------------------------------------

        first_attempt_failures = sum(
            1
            for result in module_results
            if result.get("Attempt") == 1
            and result.get("Status") == "FAIL"
        )

        # --------------------------------------------------
        # RETRY ATTEMPTS
        # --------------------------------------------------

        retry_attempts = sum(
            1
            for result in module_results
            if result.get("Final Status") == "RETRY"
        )

        # --------------------------------------------------
        # PASSED AFTER RETRY
        # --------------------------------------------------

        passed_after_retry = 0

        for test_data in test_cases:

            if final_status.get(
                test_data
            ) == "PASS":

                retry_pass = any(
                    result.get(
                        "Test Data"
                    ) == test_data
                    and result.get(
                        "Attempt",
                        1
                    ) > 1
                    and result.get(
                        "Status"
                    ) == "PASS"

                    for result in module_results
                )

                if retry_pass:

                    passed_after_retry += 1

        # --------------------------------------------------
        # TOTAL ATTEMPTS
        # --------------------------------------------------

        total_attempts = len(
            module_results
        )

        # --------------------------------------------------
        # PASS %
        # --------------------------------------------------

        if total > 0:

            pass_percentage = (
                passed / total
            ) * 100

        else:

            pass_percentage = 0

        # --------------------------------------------------
        # ADD SUMMARY ROW
        # --------------------------------------------------

        summary.append([
            module,
            total,
            passed,
            failed,
            first_attempt_failures,
            retry_attempts,
            passed_after_retry,
            total_attempts,
            f"{pass_percentage:.2f}%"
        ])

    # ======================================================
    # SUMMARY HEADER STYLE
    # ======================================================

    for cell in summary[3]:

        cell.font = Font(
            bold=True
        )

        cell.alignment = Alignment(
            horizontal="center",
            vertical="center"
        )

    # ======================================================
    # SUMMARY DATA ALIGNMENT
    # ======================================================

    for row in summary.iter_rows(
        min_row=4
    ):

        for cell in row:

            cell.alignment = Alignment(
                horizontal="center",
                vertical="center",
                wrap_text=True
            )

    # ======================================================
    # EXECUTION INFORMATION
    # ======================================================

    execution_row = (
        summary.max_row + 2
    )

    summary.cell(
        execution_row,
        1
    ).value = "Execution Information"

    summary.cell(
        execution_row,
        1
    ).font = Font(
        bold=True,
        size=12
    )

    summary.cell(
        execution_row + 1,
        1
    ).value = "Execution Date"

    summary.cell(
        execution_row + 1,
        2
    ).value = datetime.now().strftime(
        "%d-%m-%Y"
    )

    summary.cell(
        execution_row + 2,
        1
    ).value = "Execution Time"

    summary.cell(
        execution_row + 2,
        2
    ).value = datetime.now().strftime(
        "%H:%M:%S"
    )

    # ======================================================
    # OVERALL REPORT STATUS
    # ======================================================

    all_final_statuses = list(
        result
        for result in results
        if result.get(
            "Final Status"
        ) in [
            "PASS",
            "FAIL"
        ]
    )

    overall_failed = any(
        result.get(
            "Final Status"
        ) == "FAIL"

        for result in all_final_statuses
    )

    if not results:

        report_status = "NO DATA"

    elif overall_failed:

        report_status = "FAILED"

    else:

        report_status = "PASSED"

    summary.cell(
        execution_row + 3,
        1
    ).value = "Overall Status"

    summary.cell(
        execution_row + 3,
        2
    ).value = report_status

    summary.cell(
        execution_row + 4,
        1
    ).value = "Report File"

    summary.cell(
        execution_row + 4,
        2
    ).value = os.path.basename(
        REPORT_FILE
    )

    for row in range(
        execution_row + 1,
        execution_row + 5
    ):

        summary.cell(
            row,
            1
        ).font = Font(
            bold=True
        )

    # ======================================================
    # TEST RESULTS SHEET
    # ======================================================

    details = workbook.create_sheet(
        "Test Results"
    )

    details.append([
        "Module",
        "Test Case",
        "Test Data",
        "Attempt",
        "Status",
        "Error",
        "Final Status"
    ])

    # ======================================================
    # ADD RESULTS
    # ======================================================

    for result in results:

        module = result.get(
            "Module",
            result.get(
                "Test Case",
                "Unknown"
            )
        )

        details.append([
            module,
            result.get(
                "Test Case",
                ""
            ),
            result.get(
                "Test Data",
                ""
            ),
            result.get(
                "Attempt",
                ""
            ),
            result.get(
                "Status",
                ""
            ),
            result.get(
                "Error",
                ""
            ),
            result.get(
                "Final Status",
                ""
            )
        ])

    # ======================================================
    # DETAILS HEADER
    # ======================================================

    for cell in details[1]:

        cell.font = Font(
            bold=True
        )

        cell.alignment = Alignment(
            horizontal="center",
            vertical="center"
        )

    # ======================================================
    # DETAILS ALIGNMENT
    # ======================================================

    for row in details.iter_rows(
        min_row=2
    ):

        for cell in row:

            cell.alignment = Alignment(
                vertical="top",
                wrap_text=True
            )

    # ======================================================
    # FILTER
    # ======================================================

    if details.max_row > 1:

        details.auto_filter.ref = (
            details.dimensions
        )

    # ======================================================
    # FREEZE PANES
    # ======================================================

    summary.freeze_panes = "A4"

    details.freeze_panes = "A2"

    # ======================================================
    # AUTO COLUMN WIDTH
    # ======================================================

    for sheet in workbook.worksheets:

        for column in sheet.columns:

            max_length = 0

            column_letter = (
                get_column_letter(
                    column[0].column
                )
            )

            for cell in column:

                if cell.value is not None:

                    length = len(
                        str(cell.value)
                    )

                    if length > max_length:

                        max_length = length

            sheet.column_dimensions[
                column_letter
            ].width = min(
                max_length + 3,
                50
            )

    # ======================================================
    # SAVE REPORT
    # ======================================================

    workbook.save(
        REPORT_FILE
    )

    # ======================================================
    # CONSOLE OUTPUT
    # ======================================================

    print(
        "\n===================================="
    )

    print(
        "REPORT GENERATED SUCCESSFULLY"
    )

    print(
        "===================================="
    )

    print(
        f"Total Results : {len(results)}"
    )

    print(
        f"Report Status : {report_status}"
    )

    print(
        f"Report Path   : "
        f"{os.path.abspath(REPORT_FILE)}"
    )

    print(
        "===================================="
    )

