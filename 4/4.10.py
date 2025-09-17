n = int(input("Введите N: "))
k = int(input("Введите K: "))

if n <= 0 or k <= 0:
    print("Ошибка: N и K должны быть положительными числами")
else:
    a, b = 0, 1
    fib_sum = 0
    count = 0
    
    for i in range(k + n - 1):
        if i >= k - 1:
            fib_sum += a
            count += 1
        a, b = b, a + b
    
    print(fib_sum)