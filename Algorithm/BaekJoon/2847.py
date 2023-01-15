N = int(input())
scores = [int(input()) for _ in range(N)]
res = 0

for i in range(N - 1, 0, -1):
    tmp = 0

    while scores[i] <= scores[i - 1]:
        scores[i - 1] -= 1
        tmp += 1

    res += tmp

print(res)