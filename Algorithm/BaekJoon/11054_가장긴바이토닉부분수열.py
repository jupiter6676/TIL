import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

inc = [1] * N
dec = [1] * N

for i in range(N):
    for j in range(i):      # 0 ~ (i - 1) 수들을 탐색
        if seq[j] < seq[i]: # j번째 수 < i번째 수 → 증가 부분 수열
            inc[i] = max(inc[i], inc[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):   # (i + 1) ~ (N - 1) 수들을 탐색
        if seq[j] < seq[i]:     # j번째 수 < i번째 수 → 감소 부분 수열
            dec[i] = max(dec[i], dec[j] + 1)

res = 0
for i in range(N):
    res = max(res, inc[i] + dec[i] - 1)

print(res)