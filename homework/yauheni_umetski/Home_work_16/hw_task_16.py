import os
from csv_reader import CsvReader
from homework.yauheni_umetski.Home_work_16.db_connection import MySQLConnector
from homework.yauheni_umetski.Home_work_16.db_config import DB_CONFIG
from homework.yauheni_umetski.Home_work_16.students_db import StudentsTable
from homework.yauheni_umetski.Home_work_16.groups_db import GroupsTable
from homework.yauheni_umetski.Home_work_16.books_db import BooksTable
from homework.yauheni_umetski.Home_work_16.subject_db import SubjectsTable
from homework.yauheni_umetski.Home_work_16.lessons_db import LessonsTable
from homework.yauheni_umetski.Home_work_16.marks_db import MarksTable


CURR_DIR = os.path.dirname(__file__)
CSV_FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(CURR_DIR)),
    "eugene_okulik",
    "Lesson_16",
    "hw_data",
    "data.csv"
)

reader = CsvReader(file_path=CSV_FILE_PATH)
db = MySQLConnector(config=DB_CONFIG)
students_table = StudentsTable(db=db)
group_table = GroupsTable(db=db)
books_table = BooksTable(db=db)
subject_table = SubjectsTable(db=db)
lessons_table = LessonsTable(db=db)
marks_table = MarksTable(db=db)

csv_data = reader.dict_read_csv()


def check_row_exists_in_db(
        student_name: str,
        student_second_name: str,
        group_title: str,
        book_title: str,
        subject_title: str,
        lesson_title: str,
        mark_value: str
) -> bool:
    students = students_table.get_by_two_filters(
        student_name,
        students_table.COLUMNS.NAME,
        student_second_name,
        students_table.COLUMNS.SECOND_NAME
    )
    if not students:
        return False

    group = group_table.get_by_filter(
        group_title,
        group_table.COLUMNS.TITLE
    )
    if not group:
        return False

    subjects = subject_table.get_by_filter(
        subject_title,
        subject_table.COLUMNS.TITLE
    )
    if not subjects:
        return False

    for student in students:
        student_id = student[students_table.COLUMNS.ID]
        book = books_table.get_by_two_filters(
            student_id,
            books_table.COLUMNS.TAKEN_BY_STUDENT_ID,
            book_title,
            books_table.COLUMNS.TITLE
        )
        if not book:
            continue

        for subject in subjects:
            subject_id = subject[subject_table.COLUMNS.ID]
            lessons = lessons_table.get_by_two_filters(
                lesson_title,
                lessons_table.COLUMNS.TITLE,
                subject_id,
                lessons_table.COLUMNS.SUBJECT_ID
            )
            for lesson in lessons:
                lesson_id = lesson[lessons_table.COLUMNS.ID]
                mark = marks_table.get_by_three_filters(
                    mark_value,
                    marks_table.COLUMNS.VALUE,
                    student_id,
                    marks_table.COLUMNS.STUDENT_ID,
                    lesson_id,
                    marks_table.COLUMNS.LESSON_ID
                )
                if mark:
                    return True
    return False


for row in csv_data:
    student_name = row["name"]
    student_second_name = row["second_name"]
    group_title = row["group_title"]
    book_title = row["book_title"]
    subject_title = row["subject_title"]
    lesson_title = row["lesson_title"]
    mark_value = row["mark_value"]
    if not check_row_exists_in_db(
            student_name=student_name,
            student_second_name=student_second_name,
            group_title=group_title,
            book_title=book_title,
            subject_title=subject_title,
            lesson_title=lesson_title,
            mark_value=mark_value
    ):
        print(row)


db.close()
