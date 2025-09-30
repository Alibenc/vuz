count = 0
prev = None

while True:
    num = int(input())
    if num == 0:
        break
    
    if prev is not None and num > prev:
        count += 1
    
    prev = num

print(count)