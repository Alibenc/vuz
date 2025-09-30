max_count = 0
current_count = 0
prev = None

while True:
    num = int(input())
    if num == 0:
        break
    
    if num == prev:
        current_count += 1
    else:
        current_count = 1
        prev = num
    
    if current_count > max_count:
        max_count = current_count

print(max_count)