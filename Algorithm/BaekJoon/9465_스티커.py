import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stickers = [[0] + list(map(int, input().split())) for _ in range(2)]    # 2 × (N + 1)

    dp = [[0] * (N + 1) for _ in range(2)]

    dp[0][1] = stickers[0][1]
    dp[1][1] = stickers[1][1]
    
    for i in range(2, N + 1):
        # 한 칸 대각선 vs 두 칸 대각선
        # (3칸 대각선은 1칸 대각선으로 3번 이동한 것과 같음)
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + stickers[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + stickers[1][i]

    print(max(dp[0][N], dp[1][N]))