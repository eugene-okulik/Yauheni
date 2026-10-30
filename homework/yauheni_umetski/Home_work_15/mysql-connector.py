from typing import Any
from typing import Literal
from enum import StrEnum
import mysql.connector as mysql


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


class SubjectColumns(StrEnum):
    TITLE = "title"
    ID = "id"


SubjectColumnsType = Literal[
    "title",
    "id"
]


class LessonsColumns(StrEnum):
    TITLE = "title"
    SUBJECT_ID = "subject_id"
    ID = "id"


LessonsColumnsType = Literal[
    "title",
    "subject_id",
    "id"
]


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


class BooksColumns(StrEnum):
    TITLE = "title"
    ID = "id"
    TAKEN_BY_STUDENT_ID = "taken_by_student_id"


BooksColumnsType = Literal[
    "title",
    "id",
    "taken_by_student_id"
]


class MySQLConnector:
    def __init__(self, user: str, password: str,
                 host: str, port: int, database: str):
        self.__connection = mysql.connect(
            user=user,
            passwd=password,
            host=host,
            port=port,
            database=database
        )

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

    def fetch_all(self, query: str, params: tuple | list | None = None) -> list[dict] | None:
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
    ) -> dict | None:
        sql = f"SELECT * FROM `{self.__table}` WHERE `{filter_column}`= %s"
        return self.__db.fetch_all(sql, (item,))


class StudentsTable(BaseDatabase):
    COLUMNS = StudentsColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="students")

    def insert_one(
            self,
            columns: tuple[StudentsColumnsType, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: StudentsColumnsType,
            column_value: Any,
            id_column: str = "id"
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)


class GroupsTable(BaseDatabase):
    COLUMNS = GroupsColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="groups")

    def insert_one(
            self,
            columns: tuple[GroupsColumnsType, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: GroupsColumnsType,
            column_value: Any,
            id_column: str = "id"
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)


class SubjectsTable(BaseDatabase):
    COLUMNS = SubjectColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="subjects")

    def insert_one(
            self,
            columns: tuple[SubjectColumnsType, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: SubjectColumnsType,
            column_value: Any,
            id_column: str = "id"
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)


class LessonsTable(BaseDatabase):
    COLUMNS = LessonsColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="lessons")

    def insert_one(
            self,
            columns: tuple[LessonsColumnsType, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: LessonsColumnsType,
            column_value: Any,
            id_column: str = "id"
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)


class MarksTable(BaseDatabase):
    COLUMNS = MarksColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="marks")

    def insert_one(
            self,
            columns: tuple[MarksColumnsType, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: MarksColumnsType,
            column_value: Any,
            id_column: str = "id"
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)


class BooksTable(BaseDatabase):
    COLUMNS = BooksColumns

    def __init__(self, db: MySQLConnector) -> None:
        super().__init__(db, table="books")

    def insert_one(
            self,
            columns: tuple[BooksColumnsType, ...],
            items: tuple
    ) -> int | None:
        return super().insert_one(columns, items)

    def update_one_by_id(
            self,
            item_id: int | str,
            column: BooksColumnsType,
            column_value: Any,
            id_column: str = "id"
    ) -> int | None:
        return super().update_one_by_id(item_id, column, column_value, id_column)


db = MySQLConnector(
    user="st-onl",
    password="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port="25060",
    database="st-onl"
)

students = StudentsTable(db)
groups = GroupsTable(db)
subjects = SubjectsTable(db)
lessons = LessonsTable(db)
marks = MarksTable(db)
books = BooksTable(db)

# Insert data

student_id = students.insert_one(
    columns=(
        "name", "second_name"), items=(
            "Yauheni", "Umetski"))

group_id = groups.insert_one(
    columns=("title", "start_date", "end_date"),
    items=("Yauheni AQA Python", "September 2026", "December 2026")
)

students.update_one_by_id(student_id, students.COLUMNS.GROUP_ID, group_id)

subject_id_1 = subjects.insert_one(
    columns=(subjects.COLUMNS.TITLE, ),
    items=("Yauheni AQA Python subj 1", )
)
subject_id_2 = subjects.insert_one(
    columns=(subjects.COLUMNS.TITLE, ),
    items=("Yauheni AQA Python subj 2", )
)

lesson_id_1 = lessons.insert_one(
    columns=(lessons.COLUMNS.TITLE, lessons.COLUMNS.SUBJECT_ID),
    items=("YYauheni AQA Python lesson 1", subject_id_1)
)
lesson_id_2 = lessons.insert_one(
    columns=(lessons.COLUMNS.TITLE, lessons.COLUMNS.SUBJECT_ID),
    items=("Yauheni AQA Python lesson 1-1", subject_id_1)
)
lesson_id_3 = lessons.insert_one(
    columns=(lessons.COLUMNS.TITLE, lessons.COLUMNS.SUBJECT_ID),
    items=("YYauheni AQA Python lesson 2", subject_id_2)
)
lesson_id_4 = lessons.insert_one(
    columns=(lessons.COLUMNS.TITLE, lessons.COLUMNS.SUBJECT_ID),
    items=("Yauheni AQA Python lesson 2-1", subject_id_2)
)

book_id_1 = books.insert_one(
    columns=(books.COLUMNS.TITLE, books.COLUMNS.TAKEN_BY_STUDENT_ID),
    items=("Python AQA by Okulik. part 1", student_id)
)
book_id_2 = books.insert_one(
    columns=(books.COLUMNS.TITLE, books.COLUMNS.TAKEN_BY_STUDENT_ID),
    items=("Python AQA by Okulik. part 2", student_id)
)

mark_id_1 = marks.insert_one(
    columns=(
        marks.COLUMNS.VALUE,
        marks.COLUMNS.LESSON_ID,
        marks.COLUMNS.STUDENT_ID),
    items=(5, lesson_id_1, student_id)
)
mark_id_2 = marks.insert_one(
    columns=(
        marks.COLUMNS.VALUE,
        marks.COLUMNS.LESSON_ID,
        marks.COLUMNS.STUDENT_ID),
    items=(5, lesson_id_2, student_id)
)
mark_id_3 = marks.insert_one(
    columns=(
        marks.COLUMNS.VALUE,
        marks.COLUMNS.LESSON_ID,
        marks.COLUMNS.STUDENT_ID),
    items=(5, lesson_id_3, student_id)
)
mark_id_4 = marks.insert_one(
    columns=(
        marks.COLUMNS.VALUE,
        marks.COLUMNS.LESSON_ID,
        marks.COLUMNS.STUDENT_ID),
    items=(5, lesson_id_4, student_id)
)


# Task 1
print("Task 1")
marks_data_1 = marks.get_by_id(mark_id_1)
marks_data_2 = marks.get_by_id(mark_id_2)
marks_data_3 = marks.get_by_id(mark_id_3)
marks_data_4 = marks.get_by_id(mark_id_4)

marks_filter = marks.get_by_filter(student_id, marks.COLUMNS.STUDENT_ID)
print(
    f"Task 1 result: {marks_data_1}, {marks_data_2}, {marks_data_3}, {marks_data_4}")
print(f"Task 1 result: {marks_filter}")

# Task 2
print("Task 2")
books_data_1 = books.get_by_id(book_id_1)
books_data_2 = books.get_by_id(book_id_2)

books_data_filter = books.get_by_filter(
    student_id, books.COLUMNS.TAKEN_BY_STUDENT_ID)
print(f"Task 2 result: {books_data_1}, {books_data_2}")
print(f"Task 2 result: {books_data_filter}")

# Task 3
student_data = students.get_by_id(student_id)
group_data = groups.get_by_id(group_id)
subject_data_1 = subjects.get_by_id(subject_id_1)
subject_data_2 = subjects.get_by_id(subject_id_2)
lesson_data_1 = lessons.get_by_id(lesson_id_1)
lesson_data_2 = lessons.get_by_id(lesson_id_2)
lesson_data_3 = lessons.get_by_id(lesson_id_3)
lesson_data_4 = lessons.get_by_id(lesson_id_4)


print(f"Task 3 student: {student_data}")
print(f"Task 3 group: {group_data}")
print(f"Task 3 subj 1: {subject_data_1}")
print(f"Task 3 subj 2: {subject_data_2}")
print(f"Task 3 lesson 1: {lesson_data_1}")
print(f"Task 3 lesson 2: {lesson_data_2}")
print(f"Task 3 lesson 3: {lesson_data_3}")
print(f"Task 3 lesson 4: {lesson_data_4}")
