n = int(input('n: '))
m = int(input('m: '))
k = int(input('k: '))

def fn(n, m, k):
  if (k < n * m) and ((k % n == 0 and k <= n * m) or (k % m == 0 and k <= n * m)):
    return "Да"
  else:
    return "Нет"

print(fn(n, m, k))