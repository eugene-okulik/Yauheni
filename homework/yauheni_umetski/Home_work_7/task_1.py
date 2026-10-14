from random import randint

guess_number: int = randint(1, 10)
print("Please guess a number between 1 and 10")
while True:
    raw_input = input()
    if not raw_input.isdigit():
        print("Please enter a number between 1 and 10")
        continue
    user_input = int(raw_input)
    if user_input < 1 or user_input > 10:
        print("Please enter a number between 1 and 10")
        continue
    if user_input == guess_number:
        print("Поздравляю! Вы угадали!")
        break
    print("попробуйте снова")
