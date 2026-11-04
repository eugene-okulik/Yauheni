from typing import Any
from typing import Literal
from enum import StrEnum
from base_db import BaseDatabase
from db_connection import MySQLConnector


class BooksColumns(StrEnum):
    TITLE = "title"
    ID = "id"
    TAKEN_BY_STUDENT_ID = "taken_by_student_id"


BooksColumnsType = Literal[
    "title",
    "id",
    "taken_by_student_id"
]

BooksColumn = BooksColumns | BooksColumnsType


class BooksTable(BaseDatabase):
    COLUMNS = BooksColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="books")

    def insert_one(
            self,
            columns: tuple[BooksColumn, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: BooksColumn,
            column_value: Any,
            id_column: BooksColumn = BooksColumns.ID
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)
