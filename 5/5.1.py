def print_squares(n):
    i = 1
    while i * i <= n:
        print(i * i)
        i += 1

N = int(input("Введите число N: "))
print_squares(N)