import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = set()

for _ in range(N):
    coins.add(int(input()))

# 최솟값을 구하기 위해, 불가능한 값으로 초기화 (k는 최대 10000, 최대 10000개의 동전만 가능)
dp = [10001] * (K + 1)
dp[0] = 0   # 0원을 만드는 동전의 수는 0개

for c in coins:
    for i in range(c, K + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

# print(dp)
print(dp[K] if dp[K] != 10001 else -1)

'''
dp = [-1] * (K + 1)
for c in coins:
    for i in range(c, K + 1):
        if i % c == 0:
            dp[i] = i // c

        if dp[i - c] > 0:
            if dp[i] == -1:
                dp[i] = dp[i - c] + 1
            else:
                dp[i] = min(dp[i], dp[i - c] + 1)
'''
                
# print(dp)
print(dp[K])

'''
2 10
2
3
답: 4
'''