from openpyxl import load_workbook

EXCEL_FILE = "test_data.xlsx"


def get_all_data(sheet_name):
    workbook = load_workbook(EXCEL_FILE)
    sheet = workbook[sheet_name]

    headers = []

    for cell in sheet[1]:
        headers.append(cell.value)

    all_data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):

        # Skip completely empty rows
        if all(value is None for value in row):
            continue

        data = {}

        for column, header in enumerate(headers):
            data[header] = row[column]

        all_data.append(data)

    workbook.close()

    return all_data