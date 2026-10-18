from datetime import datetime

RAW_DATE: str = "Jan 15, 2023 - 12:05:33"
INPUT_FORMAT: str = "%b %d, %Y - %H:%M:%S"
OUTPUT_FORMAT: str = "%d.%m.%Y, %H:%M"

parsed_date = datetime.strptime(RAW_DATE, INPUT_FORMAT)

print(parsed_date.strftime("%B"))
print(parsed_date.strftime(OUTPUT_FORMAT))
