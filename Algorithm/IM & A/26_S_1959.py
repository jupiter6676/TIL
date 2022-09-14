# import sys

# sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    # A와 B의 길이
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_ = -99999    # 20^3 = 80000

    # A가 더 길면
    if N >= M:
        for i in range(N - M + 1):
            tmp = 0

            for j in range(M):
                tmp += A[i + j] * B[j]
            
            max_ = max(max_, tmp)

    # B가 더 길면
    else:
        for i in range(M - N + 1):
            tmp = 0

            for j in range(N):
                tmp += B[i + j] * A[j]

            max_ = max(max_, tmp)

    print(f'#{t} {max_}')