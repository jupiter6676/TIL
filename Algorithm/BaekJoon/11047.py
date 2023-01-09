N, K = map(int, input().split())
coins = list()
res = 0

for _ in range(N):
    coins.append(int(input()))

for i in range(N - 1, -1, -1):
    if K == 0:
        break
    
    if K >= coins[i]:
        res += K // coins[i]
        K %= coins[i]

print(res)