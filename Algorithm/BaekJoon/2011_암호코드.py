code = [-1] + list(map(int, input()))
N = len(code) - 1   # 입력된 수의 개수

dp = [0] * (N + 1)  # dp[i]: i번째 수 까지의 경우의 수
dp[0] = 1

for i in range(1, N + 1):
    # 1. i - 1번째 수, i번째 수를 따로따로
    # → i번째 수가 0이 아닌 한 자리 수일 때
    if 1 <= code[i] <= 9:
        # dp[i] = i - 1번째 수까지의 경우의 수
        dp[i] = dp[i - 1] % 1000000

    # 2. i - 1번째 수와 i번째 수를 합치기
    # → 합친 수가 10 ~ 26 사이일 때
    tmp = code[i - 1] * 10 + code[i]
    if 10 <= tmp <= 26:
        # dp[i] = i - 2번째 수까지의 경우의 수 (+ 위에서 저장된 dp[i])
        dp[i] = (dp[i - 2] + dp[i]) % 1000000

# print(dp)
print(dp[N])