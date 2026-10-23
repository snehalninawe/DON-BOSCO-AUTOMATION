from openpyxl import load_workbook
import os

EXCEL_FILE = "test_data.xlsx"
API_EXCEL_FILE = "Api_Test_Data.xlsx"


def get_all_data(sheet_name):
    # Selenium automation
    return read_excel(EXCEL_FILE, sheet_name)


def get_api_data(sheet_name):
    # API automation
    return read_excel(API_EXCEL_FILE, sheet_name)


def read_excel(file_name, sheet_name):
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        file_name
    )

    workbook = load_workbook(file_path)

    try:
        sheet = workbook[sheet_name]
        headers = [cell.value for cell in sheet[1]]
        all_data = []

        for row in sheet.iter_rows(min_row=2, values_only=True):

            # Skip completely empty rows
            if all(value is None for value in row):
                continue

            data = {}

            for column, header in enumerate(headers):
                data[header] = row[column]

            all_data.append(data)

        return all_data

    finally:
        workbook.close()
