N = int(input())
dp = [0] * (abs(N) + 1)

if N == 0:
    print(0)
elif N > 0:
    print(1)
else:
    print(-1 if N % 2 == 0 else 1)

if abs(N) > 0:
    dp[1] = 1

    for i in range(2, abs(N) + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000

print(dp[abs(N)])


'''
f[n] = f[n - 1] + f[n - 2]

if n == 1:
    f[1] = f[0] + f[-1] = 0 + f[-1] = 1
    ∴ f[-1] = 1

if n == 0:
    f[0] = f[-1] + f[-2] = 1 + f[-2] = 0
    ∴ f[-2] = -1

if n == -1:
    f[-1] = f[-2] + f[-3] = -1 + f[-3] = 1
    ∴ f[-3] = 2

if n == -2:
    f[-2] = f[-3] + f[-4] = 2 + f[-4] = -1
    ∴ f[-4] = -3
'''

# … -3 2 -1 1 '0' 1 1 2 3 4 …