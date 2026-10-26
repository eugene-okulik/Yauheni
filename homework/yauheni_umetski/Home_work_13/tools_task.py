from datetime import datetime, timedelta
import os


INPUT_FORMAT: str = "%Y-%m-%d %H:%M:%S.%f"
CURR_DIR = os.path.dirname(__file__)
READ_FILE_DIR = os.path.join(os.path.dirname(os.path.dirname(CURR_DIR)), "eugene_okulik", "hw_13", "data.txt")
DAY_WEEK_FORMAT = "%A"


def parse_date(date_str, input_format) -> datetime:
    return datetime.strptime(date_str, input_format)


def cut_date_from_row(row) -> str:
    return row.split(" - ")[0].split(". ")[1]


def read_file_by_line(file_path):
    with open(file_path, "r") as read_file:
        for line_number, line in enumerate(read_file, start=1):
            yield line_number, line


for line_number, data_line in read_file_by_line(READ_FILE_DIR):
    date = parse_date(cut_date_from_row(data_line), INPUT_FORMAT)
    if line_number == 1:
        print(date + timedelta(days=7))
    elif line_number == 2:
        print(date.strftime(DAY_WEEK_FORMAT))
    elif line_number == 3:
        now = datetime.now().date()
        print((now - date.date()).days)
