str1 = ' ' + input()
str2 = ' ' + input()

R = len(str1)
C = len(str2)

dp = [[0] * (C + 1) for _ in range(R + 1)]

for i in range(1, R):
    for j in range(1, C):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[R - 1][C - 1])