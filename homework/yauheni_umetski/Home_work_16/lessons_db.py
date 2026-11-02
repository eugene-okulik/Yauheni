from typing import Any
from typing import Literal
from enum import StrEnum
from base_db import BaseDatabase
from db_connection import MySQLConnector


class LessonsColumns(StrEnum):
    TITLE = "title"
    SUBJECT_ID = "subject_id"
    ID = "id"


LessonsColumnsType = Literal[
    "title",
    "subject_id",
    "id"
]

LessonsColumn = LessonsColumns | LessonsColumnsType


class LessonsTable(BaseDatabase):
    COLUMNS = LessonsColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="lessons")

    def insert_one(
            self,
            columns: tuple[LessonsColumn, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: LessonsColumn,
            column_value: Any,
            id_column: LessonsColumn = LessonsColumns.ID
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)
