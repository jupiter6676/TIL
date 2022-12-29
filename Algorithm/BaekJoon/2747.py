N = int(input())

d = [0, 1]   # 0번째, 1번째
for i in range(2, N + 1):   # N번째 수까지
    d.append(d[i - 1] + d[i - 2])

print(d[N])
