import csv
from pathlib import Path


class CsvReader:
    def __init__(
            self,
            file_path: str | Path,
            delimiter: str = ",",
            header: bool = True,
            encoding: str = "utf-8"
    ):
        self._file_path = file_path
        self._delimiter = delimiter
        self._header = header
        self._headers: list[str] | None = None
        self._encoding = encoding

    @property
    def headers(self) -> list[str] | None:
        return self._headers

    def dict_read_csv(self) -> list[dict]:
        with open(self._file_path, encoding=self._encoding, newline="") as csv_file:
            if not self._header:
                temp_reader = csv.reader(csv_file, delimiter=self._delimiter)
                try:
                    first_row = next(temp_reader)
                except StopIteration:
                    return []
                self._headers = [f"col_{i}" for i in range(len(first_row))]
                csv_file.seek(0)

                reader = csv.DictReader(
                    csv_file,
                    fieldnames=self._headers,
                    delimiter=self._delimiter
                )
            else:
                reader = csv.DictReader(csv_file, delimiter=self._delimiter)
                self._headers = reader.fieldnames
            return list(reader)
