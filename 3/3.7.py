n = int(input('Введите год: '))

def fn(n):
  if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    return 'Да'
  else: 
    return 'Нет'

print(fn(n))