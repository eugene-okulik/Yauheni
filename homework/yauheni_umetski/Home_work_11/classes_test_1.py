class Book:
    material: str = "бумага"
    has_text: bool = True

    def __init__(self, name: str, author: str, number: int, isbn_number: int,
                 reservation: bool = False):
        self.name = name
        self.author = author
        self.number = number
        self.isbn_number = isbn_number
        self.reservation = reservation

    def book_info(self):
        print(f"Название: {self.name}, Автор: {self.author}, "
              f"страниц: {self.number}, "
              f"материал: {self.material}"
              f"{', зарезервирована' if self.reservation else ''}")


class SchoolBook(Book):

    def __init__(self, name: str, author: str, number: int, isbn_number: int, subject: str,
                 school_class: str, homework: bool = False):
        super().__init__(name, author, number, isbn_number)
        self.subject = subject
        self.school_class = school_class
        self.homework = homework

    def book_info(self):
        print(f"Название: {self.name}, Автор: {self.author}, "
              f"страниц: {self.number}, "
              f"предмет: {self.subject}, класс: {self.school_class}"
              f"{', зарезервирована' if self.reservation else ''}")


python_book = Book("Python", "Python_author", 123, 1234567)
js_book = Book("JS", "JS_author", 23, 2234567)
java_book = Book("Java", "Java_author", 1230, 3234567)
test_book = Book("Testing", "Test_author", 1123, 4234567)
selenium_book = Book("Selenium", "Selenium_author", 1423, 5234567)

python_book.reservation = True

for book in [python_book, js_book, java_book, selenium_book, test_book]:
    book.book_info()

math = SchoolBook("Math", "Math_author", 123, 3234567, "Math_sbj", "1", True)
biology = SchoolBook("Biology", "BIOLOGY_author", 1123, 4234567, "Biology_sbj", "2")
geology = SchoolBook("Geology", "Geology_author", 1423, 34234567, "Geo_sbj", "9", True)

geology.reservation = True

for sbj in [math, biology, geology]:
    sbj.book_info()
