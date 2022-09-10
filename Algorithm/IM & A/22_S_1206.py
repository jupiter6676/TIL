import sys

sys.stdin = open("input.txt", "r")

'''
8
0 0 3 5 2 4 9 0 6 4 0 6 0 0
'''

for t in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0

    for i in range(2, len(lst) - 2):
        tmp = lst[i]

        while True:
            if lst[i - 2] < tmp and lst[i - 1] < tmp and lst[i + 1] < tmp and lst[i + 2] < tmp:
                cnt += 1
                tmp -= 1
            else:
                break

    print(f'#{t} {cnt}')