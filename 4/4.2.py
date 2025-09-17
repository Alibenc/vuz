A = int(input('Число A: '))
B = int(input('Число B: '))

def fn(A, B):
  if B > A:
    for i in range(A, B + 1):
      print(i)
  else:
    print('test')
    for i in range(A, B - 1, -1):
      print(i)

fn(A, B)