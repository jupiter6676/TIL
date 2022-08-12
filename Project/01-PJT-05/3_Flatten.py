import sys

sys.stdin = open("_Flatten.txt")

for tc in range(1, 11):
    dump = int(input())
    num_list = list(map(int, input().split()))

    num_list.sort()

    for _ in range(dump):
        num_list[99] -= 1
        num_list[0] += 1

        num_list.sort()

    res = num_list[99] - num_list[0]

    print(f'#{tc} {res}')