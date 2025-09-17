n = int(input("Введите количество чисел из ряда Фибоначчи: "))

if n <= 0:
    print("Ошибка: введите положительное число")
else:
    a, b = 0, 1
    fib_sum = 0
    
    for i in range(n):
        fib_sum += a 
        a, b = b, a + b  
    
    print(fib_sum)