N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

for row in lst:
    for elem in row[::-1]:
        print(elem, end='')
    print()