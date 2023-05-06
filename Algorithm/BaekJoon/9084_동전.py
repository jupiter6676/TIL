import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())    # 목표 금액 (1 ~ 10,000)

    dp = [0] * (M + 1)
    dp[0] = 1

    for c in coins:
        for i in range(c, M + 1):
            dp[i] += dp[i - c]
    
    print(dp[M])

'''
1
3
1 5 10
12
'''