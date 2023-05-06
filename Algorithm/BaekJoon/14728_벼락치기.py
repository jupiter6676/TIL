import sys
input = sys.stdin.readline

N, T = map(int, input().split())
chaps = [list(map(int, input().split())) for _ in range(N)]

# dp = [[0] * N for _ in range(N)]
# dp = [0] * 1001
dp = [0] * (T + 1)

for i in range(N):
    K, S = chaps[i] # 단원 공부 시간, 배점
    
    for j in range(T, K - 1, -1):   # 한 단원은 한 번만 공부
        dp[j] = max(dp[j], dp[j - K] + S)

print(dp[T])

'''
3 31
5 40
10 70
20 150
'''