import random

while True:
    print("Please enter your salary")
    salary_raw: str = input()
    if salary_raw.isdigit():
        salary: int = int(salary_raw)
        break
    print("Please enter your salary as a number")

bonus = random.choice([True, False])
total_salary = salary
if bonus:
    total_salary += random.randrange(1, 10000)
print(f"{salary}, {bonus} - '${total_salary}'")
