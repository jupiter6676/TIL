import sys
input = sys.stdin.readline

def pprint():
    print('=================')
    for row in dp:
        for elem in row:
            print(elem, end=' ')
        print()
    # for mat in dp:
    #     for row in mat:
    #         for elem in row:
    #             print(elem, end=' ')
    #         print()
    #     print()

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j][2]: i번 집을 j색으로 칠했을 때의 최소비용, 그 때의 첫번째 집의 색
dp = [[9999] * N for _ in range(N)]
dp[0][0] = (costs[0][0], 0)
dp[0][1] = (costs[0][1], 1)
dp[0][2] = (costs[0][2], 2)

for i in range(1, N):
    if i < N - 1:
        # i번째 집 빨간색(0)
        if dp[i - 1][1][0] < dp[i - 1][2][0]:
            dp[i][0] = (dp[i - 1][1][0] + costs[i][0], dp[i - 1][1][1])
        else:
            dp[i][0] = (dp[i - 1][2][0] + costs[i][0], dp[i - 1][2][1])

        # i번째 집 초록색(1)
        if dp[i - 1][0][0] < dp[i - 1][2][0]:
            dp[i][1] = (dp[i - 1][0][0] + costs[i][1], dp[i - 1][0][1])
        else:
            dp[i][1] = (dp[i - 1][2][0] + costs[i][1], dp[i - 1][2][1])

        # i번째 집 파란색(2)
        if dp[i - 1][0][0] < dp[i - 1][1][0]:
            dp[i][2] = (dp[i - 1][0][0] + costs[i][2], dp[i - 1][0][1])
        else:
            dp[i][2] = (dp[i - 1][1][0] + costs[i][2], dp[i - 1][1][1])
    
    else:
        # 1. N - 1번째 집 빨간색(0)
        # → N - 2번째 집 1, 2 and 첫번째 집 not 0
        if dp[i - 1][1][1] != 0:
            dp[i][0] = min(dp[i][0], dp[i - 1][1][0] + costs[i][0])
        if dp[i - 1][2][1] != 0:
            dp[i][0] = min(dp[i][0], dp[i - 1][2][0] + costs[i][0])

        # 2. N - 1번째 집 초록색(1)
        # → N - 2번째 집 0, 2 and 첫번째 집 not 1
        if dp[i - 1][0][1] != 1:
            dp[i][1] = min(dp[i][1], dp[i - 1][0][0] + costs[i][1])
        if dp[i - 1][2][1] != 1:
            dp[i][1] = min(dp[i][1], dp[i - 1][2][0] + costs[i][1])

        # 3. N - 1번째 집 파란색(2)
        # → N - 2번째 집 0, 1 and 첫번째 집 not 2
        if dp[i - 1][0][1] != 2:
            dp[i][2] = min(dp[i][2], dp[i - 1][0][0] + costs[i][2])
        if dp[i - 1][1][1] != 2:
            dp[i][2] = min(dp[i][2], dp[i - 1][1][0] + costs[i][2])

    # dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    # dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    # dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

pprint()


# dp[i][j]: i번 집을 j색으로 칠했을 때의 최소비용?
# dp = [[0] * N for _ in range(N)]
# dp[0][0] = costs[0][0]
# dp[0][1] = costs[0][1]
# dp[0][2] = costs[0][2]

# for i in range(1, N):
#     if i < N - 1:
#         dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
#         dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
#         dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

#     else:

'''
# dp[k][i][j]: i번 집을 j색으로 칠했을 때의 최소비용, k는 0번 집의 색
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

dp[0][0][0] = costs[0][0]
dp[1][0][1] = costs[0][1]
dp[2][0][2] = costs[0][2]

dp[0][1][1] = dp[0][0][0] + costs[1][1]
dp[0][1][2] = dp[0][0][0] + costs[1][2]
dp[1][1][0] = dp[1][0][0] + costs[1][0]
dp[1][1][2] = dp[1][0][1] + costs[1][2]
dp[2][1][0] = dp[2][0][2] + costs[1][0]
dp[2][1][1] = dp[2][0][2] + costs[1][1]

for i in range(2, N):
    if i < N - 1:
        for k in range(3):
            dp[k][i][0] = min(dp[k][i - 1][1], dp[k][i - 1][2]) + costs[i][0]
            dp[k][i][1] = min(dp[k][i - 1][0], dp[k][i - 1][2]) + costs[i][1]
            dp[k][i][2] = min(dp[k][i - 1][0], dp[k][i - 1][1]) + costs[i][2]

    else:
        dp[0][i][1] = min(dp[0][i - 1][0], dp[0][i - 1][2]) + costs[i][1]
        dp[0][i][2] = min(dp[0][i - 1][0], dp[0][i - 1][1]) + costs[i][2]

        dp[1][i][0] = min(dp[1][i - 1][1], dp[1][i - 1][2]) + costs[i][0]
        dp[1][i][2] = min(dp[1][i - 1][0], dp[1][i - 1][1]) + costs[i][2]

        dp[2][i][0] = min(dp[2][i - 1][1], dp[2][i - 1][2]) + costs[i][0]
        dp[2][i][1] = min(dp[2][i - 1][0], dp[2][i - 1][2]) + costs[i][1]
'''

# 1. 이웃 집과 색이 같으면 X
# 2. 첫 집과 마지막 집의 색이 같으면 X