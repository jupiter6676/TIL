N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)    # 정렬하든 안 하든 다 똑같더라..

res = 0
for i in range(N):
    res += a[i] * b[i]

print(res)