from typing import Any
from typing import Literal
from enum import StrEnum
from base_db import BaseDatabase
from db_connection import MySQLConnector


class MarksColumns(StrEnum):
    VALUE = "value"
    LESSON_ID = "lesson_id"
    STUDENT_ID = "student_id"
    ID = "id"


MarksColumnsType = Literal[
    "value",
    "lesson_id",
    "student_id",
    "id"
]

MarksColumn = MarksColumns | MarksColumnsType


class MarksTable(BaseDatabase):
    COLUMNS = MarksColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="marks")

    def insert_one(
            self,
            columns: tuple[MarksColumn, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: MarksColumn,
            column_value: Any,
            id_column: MarksColumn = MarksColumns.ID
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)
