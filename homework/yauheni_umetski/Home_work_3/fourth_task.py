from math import sqrt, pow

side_a = 17
side_b = 22

print(f'Катет а: {side_a}, катет b: {side_b} прямоугольного треугольника. Гипотенуза: '
      f'{sqrt(pow(side_a, 2) + pow(side_b, 2))} ')

print(f'Катет а: {side_a}, катет b: {side_b} прямоугольного треугольника. Площадь: '
      f'{(side_a * side_b) / 2}')
