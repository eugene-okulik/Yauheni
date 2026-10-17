import sys
sys.set_int_max_str_digits(0)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 1
for number in fibonacci():
    if count in (5, 200, 1000, 100000):
        print(number)
        if count == 100000:
            break
    count += 1
