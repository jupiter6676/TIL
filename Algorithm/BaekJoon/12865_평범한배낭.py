import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K + 1)

weights = list()
values = list()

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

for i in range(len(weights)):
    w = weights[i]

    for j in range(K, w - 1, -1):
        if dp[j]:
            dp[j] = max(dp[j], dp[j - w] + values[i])
        else:
            dp[j] = values[i]
        
    # print(dp)
print(dp[K])

'''
5 7
2 4
4 3
1 1
8 9
1 10
답: 17
'''