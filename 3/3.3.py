def fn():
  n = int(input('Введите кол-во минут: '))

  print('Часы: ', n // 60)
  print('Минуты: ', n % 60)

fn()