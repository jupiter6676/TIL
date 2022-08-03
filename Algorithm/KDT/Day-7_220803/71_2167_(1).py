'''시간 초과'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr2D = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
for _ in range(K):
    # 1 이상의 자연수
    i, j, x, y = map(int, input().split())

    sum_ = 0
    for r in range(i - 1, x):
        for c in range(j - 1, y):
            sum_ += arr2D[r][c]

    print(sum_)