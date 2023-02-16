import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]   # 0일 ~ N - 1일까지 상담, 퇴사일은 N일
dp = [0] * (N + 1)  # 해당 상담을 했을 때의 누적 금액

for i in range(N - 1, -1, -1):
    end = i + lst[i][0]

    if end > N:
        # 오늘 상담 X → 다음날에 저장된 수익 오늘로 땡기기
        dp[i] = dp[i + 1]
        
    else:
        # 1. 오늘 상담 X → 다음날에 저장된 수익 오늘로 땡기기
        # 2. 오늘 상담 O → 상담이 끝난 날에 저장된 수익 + 오늘 상담의 수익
        dp[i] = max(dp[i + 1], dp[end] + lst[i][1])

print(dp[0])