a = int(input('Число A: '))
b = int(input('Число B: '))

def fn(a, b):
  for i in range(a, b - 1, -1):
    if i % 2 == 0:
      print(i)

fn(a, b)