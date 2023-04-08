import math

N = int(input())
dp = [0] * (N + 1)

# for i in range(math.sqrt(N)):
#     dp[i] = 1

for i in range(1, N + 1):
    for j in range(1, int(math.sqrt(N)) + 1):
        tmp = pow(j, 2)

        if i > tmp:
            if dp[i]:
                dp[i] = min(dp[i], dp[tmp] + dp[i - tmp])
            else:
                dp[i] = dp[tmp] + dp[i - tmp]
        
        elif i == tmp:
            dp[i] = 1
            break

print(dp[N])
# print(dp)

'''
18
답: 2
'''