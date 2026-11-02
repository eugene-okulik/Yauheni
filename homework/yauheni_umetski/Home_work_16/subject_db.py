from typing import Any
from typing import Literal
from enum import StrEnum
from base_db import BaseDatabase
from db_connection import MySQLConnector


class SubjectColumns(StrEnum):
    TITLE = "title"
    ID = "id"


SubjectColumnsType = Literal[
    "title",
    "id"
]

SubjectColumn = SubjectColumns | SubjectColumnsType


class SubjectsTable(BaseDatabase):
    COLUMNS = SubjectColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="subjects")

    def insert_one(
            self,
            columns: tuple[SubjectColumn, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: SubjectColumn,
            column_value: Any,
            id_column: SubjectColumn = SubjectColumns.ID
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)
