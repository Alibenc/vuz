import math

def fn(a, b, l, N):
  return 2 * l + (2 * N - 1) * math.sqrt(a**2 + b**2)

a = int(input('Расстояние между рядами: '))
b = int(input('Расстояние между дырками в ряду: '))
l = int(input('Длина свободного конца шнурка: '))
N = int(input('Кол-во дырок в ряду: '))


print('Длина шнурка: ', fn(a, b, l, N))