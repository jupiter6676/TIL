def fibo(n):
    for i in range(2, n + 1):
        tmp_list = list()
        tmp_list.append(dp[i - 1][0] + dp[i - 2][0])    # 전 수, 전전 수의 0이 호출된 횟수를 더함
        tmp_list.append(dp[i - 1][1] + dp[i - 2][1])    # 전 수, 전전 수의 1이 호출된 횟수를 더함

        dp.append(tmp_list)


T = int(input())
for t in range(T):
    N = int(input())
    # 0, 1일 때의 0과 1이 호출된 횟수 (ex. 0 → 0이 1개, 1이 0개)
    # dp[n] → n일 때 총 0과 1이 호출된 횟수
    dp = [[1, 0], [0, 1]]

    fibo(N)
    print(*dp[N])