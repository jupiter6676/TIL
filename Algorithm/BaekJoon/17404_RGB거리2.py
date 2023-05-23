import sys
input = sys.stdin.readline

def pprint():
    print('=================')
    for row in dp:
        for elem in row:
            print(elem, end=' ')
        print()


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]    # dp[i][j]: i번째 집의 색(j)

MAX = 10000 ** 2 + 1
res = MAX

# 첫 번째 집의 색
for c in range(3):
    # 첫 번째 집에 칠한 색에만 비용 저장, 나머지는 최댓값으로
    for i in range(3):
        dp[0][i] = MAX

    dp[0][c] = costs[0][c]

    # 두 번째 ~ N번째 집 색칠
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

    # N번째 집의 색(i)이 첫 번째 집의 색(c)와 같지 않은 경우만 체크
    for i in range(3):
        if i != c:
            res = min(res, dp[N - 1][i])

    # pprint()
    
print(res)

# 1. 이웃 집과 색이 같으면 X
# 2. 첫 집과 마지막 집의 색이 같으면 X