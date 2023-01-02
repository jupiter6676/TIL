N = int(input())

dp = [0] * (N + 1)
dp[3] = 1

if N >= 5:
    dp[5] = 1

# for i in range(3, N + 1):
#     if dp[i]:
#         if i + 3 <= N:
#             dp[i + 3] = dp[i] + 1
# print(dp)

# for i in range(3, N + 1):
#     if dp[i]:
#         if i + 5 <= N:
#             dp[i + 5] = dp[i] + 1
# print(dp)

for i in range(3, N + 1):
    # 3과 5로 수를 만들 수 있을 때만
    if dp[i]:
        if i + 3 <= N:
            if dp[i + 3] == 0:
                dp[i + 3] = dp[i] + 1
            else:
                dp[i + 3] = min(dp[i + 3], dp[i] + 1)
        
        if i + 5 <= N:
            if dp[i + 5] == 0:
                dp[i + 5] = dp[i] + 1
            else:
                dp[i + 5] = min(dp[i + 5], dp[i] + 1)
    
print(dp[N] if dp[N] else -1)