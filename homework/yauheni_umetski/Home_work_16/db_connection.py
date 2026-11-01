import mysql.connector as mysql


class MySQLConnector:
    def __init__(self, config: dict) -> None:
        self.__connection = mysql.connect(**config)

    def close(self):
        if self.__connection.is_connected():
            self.__connection.close()

    def fetch_one(self, query: str, params: tuple | list | None = None) -> dict | None:
        cursor = self.__connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            return cursor.fetchone()
        finally:
            cursor.close()

    def fetch_all(self, query: str, params: tuple | list | None = None) -> list[dict]:
        cursor = self.__connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        finally:
            cursor.close()

    def execute(self, query: str, params: tuple | list | None = None) -> int | None:
        cursor = self.__connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            self.__connection.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
