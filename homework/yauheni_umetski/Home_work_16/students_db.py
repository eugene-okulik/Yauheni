from typing import Any
from typing import Literal
from enum import StrEnum
from homework.yauheni_umetski.Home_work_16.base_db import BaseDatabase
from homework.yauheni_umetski.Home_work_16.db_connection import MySQLConnector


class StudentsColumns(StrEnum):
    NAME = "name"
    SECOND_NAME = "second_name"
    GROUP_ID = "group_id"
    ID = "id"


StudentsColumnsType = Literal[
    "name",
    "second_name",
    "group_id",
    "id"
]

StudentsColumn = StudentsColumns | StudentsColumnsType


class StudentsTable(BaseDatabase):
    COLUMNS = StudentsColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="students")

    def insert_one(
            self,
            columns: tuple[StudentsColumn, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: StudentsColumn,
            column_value: Any,
            id_column: StudentsColumn = StudentsColumns.ID
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)
