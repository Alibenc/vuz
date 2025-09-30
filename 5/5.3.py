n = int(input('Введите число'))
power = 1
exponent = 0

while power * 2 <= n:
    power *= 2
    exponent += 1

print(exponent, power)