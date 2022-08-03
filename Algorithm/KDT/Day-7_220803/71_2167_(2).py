import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 행 1 ~ N, 열 1 ~ M의 이차원 리스트
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # (0, 0) ~ (i, j) 까지의 누적합 저장
        dp[i][j] = arr[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

K = int(input())
for _ in range(K):
    # 1 이상의 자연수
    i, j, x, y = map(int, input().split())

    # (i, j) ~ (x, y) 까지의 합
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])