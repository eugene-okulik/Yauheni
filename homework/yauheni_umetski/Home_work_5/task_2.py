text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'

text = [text_1, text_2, text_3]
for row in text:
    match_index = row.index(": ")
    print(int(row[match_index + 2:]) + 10)