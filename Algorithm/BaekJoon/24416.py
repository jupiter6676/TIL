# 재귀호출
def fibo_rec(n):
    if n == 1 or n == 2:
        # 여기 실행 횟수 = n번째 피보나치 수
        # 귀납법 → https://freshmath.tistory.com/6
        return 1
    
    return fibo_rec(n - 1) + fibo_rec(n - 2)


# DP
def fibo_dp(n):
    global cnt_dp
    dp = [0, 1, 1]

    for i in range(3, n + 1):
        cnt_dp += 1
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


'''main'''
N = int(input())
cnt_dp = 0

print(fibo_dp(N), cnt_dp)