N = int(input())
seq = list(map(int, input().split()))

dp = [1] * N    # 각 지점까지의, 증가하는 수열의 최대 길이

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        
print(max(dp))