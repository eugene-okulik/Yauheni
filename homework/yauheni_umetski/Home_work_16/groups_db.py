from typing import Any
from typing import Literal
from enum import StrEnum
from homework.yauheni_umetski.Home_work_16.base_db import BaseDatabase
from homework.yauheni_umetski.Home_work_16.db_connection import MySQLConnector


class GroupsColumns(StrEnum):
    TITLE = "title"
    START_DATE = "start_date"
    END_DATE = "end_date"
    ID = "id"


GroupsColumnsType = Literal[
    "title",
    "start_date",
    "end_date",
    "id"
]

GroupsColumn = GroupsColumns | GroupsColumnsType


class GroupsTable(BaseDatabase):
    COLUMNS = GroupsColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="groups")

    def insert_one(
            self,
            columns: tuple[GroupsColumn, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: GroupsColumn,
            column_value: Any,
            id_column: GroupsColumn = GroupsColumns.ID
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)
