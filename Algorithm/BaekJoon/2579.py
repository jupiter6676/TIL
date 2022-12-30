N = int(input())
stairs = list()

for _ in range(N):
    stairs.append(int(input()))

# dp[n]: n번째 계단까지 도달할 때의 최대 점수
dp = [0] * N
dp[0] = stairs[0]

if N > 1:
    dp[1] = max(stairs[1], stairs[1] + stairs[0])
if N > 2:
    dp[2] = max(stairs[2] + stairs[1], stairs[2] + stairs[0])

for i in range(3, N):
    dp[i] = max(stairs[i] + stairs[i - 1] + dp[i - 3], stairs[i] + dp[i - 2])
    
print(dp[N - 1])