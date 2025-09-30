x = float(input('Введите x: '))
y = float(input('Введите y: '))

day = 1
distance = x

while distance < y:
    distance += distance * 0.1
    day += 1

print(day)