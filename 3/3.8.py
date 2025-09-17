def fn():
  f = int(input('Первое: '))
  s = int(input('Второе: '))
  th = int(input('Третье: '))

  if f == s == th:
    return 3
  elif f == s or f == th or s == th:
    return 2
  else:
    return 0

print(fn())