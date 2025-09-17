def fn():
  stolb1 = int(input('Введите первый столбец: '))
  str1 = int(input('Введите первую строку: '))

  stolb2 = int(input('Введите второй столбец: '))
  str2 = int(input('Введите вторую строку: '))

  color1 = (stolb1 + str1) % 2
  color2 = (stolb2 + str2) % 2

  if color1 == color2:
    return 'Да'
  else: 
    return 'Нет'

print(fn())