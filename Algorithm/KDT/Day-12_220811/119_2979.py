A, B, C = map(int, input().split())
lst = [0] * 100

for _ in range(3):
    start, end = map(int, input().split())

    for i in range(start - 1, end - 1):
        lst[i] += 1

total = 0

for num in lst:
    if num == 1:
        total += num * A
    elif num == 2:
        total += num * B
    elif num == 3:
        total += num * C

print(total)