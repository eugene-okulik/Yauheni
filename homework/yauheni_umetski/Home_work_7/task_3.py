text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'
text_4 = 'результат: 2'


def sum_numbers_text(*args):
    for row in args:
        print(int(row.split(": ")[1]) + 10)


sum_numbers_text(text_1, text_2, text_3, text_4)
