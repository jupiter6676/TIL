N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# dp[i][0]: i번째 집을 빨간색으로 칠할 때의 최소비용
# dp[i][1]: i번째 집을 초록색으로 칠할 때의 최소비용
# dp[i][2]: i번째 집을 파란색으로 칠할 때의 최소비용
dp = [[0] * 3 for _ in range(N + 1)]

# dp[0]은 사용하지 X, costs는 [0]부터 시작
for i in range(1, N + 1):
    # 1. i번째 집을 빨간색으로 칠할 때의 최소비용
    # → (i - 1)번째 집을 초록색 혹은 파란색으로 칠할 때의 최소비용 중 더 작은 값
    # → + 현재 집을 빨간색으로 칠하는 비용 costs[i - 1][0]
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i - 1][0]

    # 2. i번째 집을 초록색으로 칠할 때의 최소비용
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i - 1][1]

    # 3. i번째 집을 파란색으로 칠할 때의 최소비용
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i - 1][2]

print(min(dp[N][0], dp[N][1], dp[N][2]))