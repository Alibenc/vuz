n = int(input("Введите число n: "))

res = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i 
    res += factorial 

print(res)