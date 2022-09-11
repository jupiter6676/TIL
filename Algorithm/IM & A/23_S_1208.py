# import sys

# sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))

    lst.sort()

    for _ in range(dump):
        lst[-1] -= 1
        lst[0] += 1

        lst.sort()

    print(f'#{t} {lst[-1] - lst[0]}')