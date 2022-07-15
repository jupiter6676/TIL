n, x = map(int, input().split())
numbers = map(int, input().split())  # n은 안 쓰는데..

for num in numbers:
    if num < x:
        print(num, end=' ')