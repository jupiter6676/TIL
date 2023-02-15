N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]   # 0일 ~ N - 1일까지 상담, 퇴사일은 N일
dp = [0] * (N + 1)  # 해당 상담이 있는 날 전까지의 누적 금액 (상담 X)

# 1. Bottom-up
for i in range(N):
    end = i + lst[i][0]

    # 퇴사일은 N
    for j in range(end, N + 1):
        # 1. j 상담 이전까지의 모든 금액
        # 2. i 상담 이전까지의 모든 금액 + i 상담의 금액
        dp[j] = max(dp[j], dp[i] + lst[i][1])

'''
# 2. Top-down
for i in range(N - 1, -1, -1):
    end = i + lst[i][0]

    if end > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[end] + lst[i][1])
'''

# print(dp)
print(dp[-1])