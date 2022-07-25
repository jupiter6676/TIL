n, x = map(int, input().split())
numbers = map(int, input().split())

for num in numbers:
    if num < x:
        print(num, end=' ')