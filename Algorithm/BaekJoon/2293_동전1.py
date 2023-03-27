import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()

dp = [0] * (K + 1)
dp[0] = 1   # 0원을 만드는 경우의 수: 1 (아무 동전도 사용하지 X)

for c in coins:
    for i in range(c, K + 1):
        # 현재 c원 → i원을 만드려면 i - c원을 만드는 경우에서 c원을 더하면 된다.
        # 기존의 i원을 만드는 경우의 수에, i - c원을 만드는 경우의 수를 더해준다.
        dp[i] += dp[i - c]

# print(dp)
print(dp[K])

'''
5 1000
1
2
5
10
25
답: 18140751
'''