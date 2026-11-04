from typing import Any
from db_connection import MySQLConnector


class BaseDatabase:
    def __init__(self, db: MySQLConnector, table: str) -> None:
        self.__db = db
        self.__table = table

    def get_by_id(self, item_id: int) -> dict | None:
        sql = f"SELECT * FROM `{self.__table}` WHERE id= %s"
        return self.__db.fetch_one(sql, (item_id,))

    def insert_one(self, columns: tuple[str, ...], items: tuple) -> int | None:
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["%s"] * len(columns))
        sql = f"INSERT INTO `{self.__table}` ({columns_str}) VALUES({placeholders})"

        return self.__db.execute(sql, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: str,
            column_value: Any,
            id_column: str = "id"
    ) -> int | None:
        sql = f"UPDATE `{self.__table}` set `{column}` = %s WHERE `{id_column}`= %s"
        return self.__db.execute(sql, (column_value, item_id))

    def get_by_filter(
            self,
            item: int | str,
            filter_column: str = "id"
    ) -> list[dict]:
        sql = f"SELECT * FROM `{self.__table}` WHERE `{filter_column}`= %s"
        return self.__db.fetch_all(sql, (item,))

    def get_by_two_filters(
            self,
            item_1: int | str,
            filter_column_1: str,
            item_2: int | str,
            filter_column_2: str = "id"
    ) -> list[dict]:
        sql = f"SELECT * FROM `{self.__table}` WHERE `{filter_column_1}`= %s and `{filter_column_2}`= %s"
        return self.__db.fetch_all(sql, (item_1, item_2))

    def get_by_three_filters(
            self,
            item_1: int | str,
            filter_column_1: str,
            item_2: int | str,
            filter_column_2: str,
            item_3: int | str,
            filter_column_3: str = "id"
    ) -> list[dict]:
        sql = (
            f'SELECT * FROM `{self.__table}` '
            f'WHERE `{filter_column_1}`= %s '
            f'and `{filter_column_2}`= %s '
            f'and `{filter_column_3}`= %s'
        )
        return self.__db.fetch_all(
            sql,
            (item_1, item_2, item_3))
