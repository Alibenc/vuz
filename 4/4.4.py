n = int(input('Введите количество чисел: '))
res = 0;

for i in range(n):
  res += int(input(f'Введите число №{(i + 1)}: '))

print(res)