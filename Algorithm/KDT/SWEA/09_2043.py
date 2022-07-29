p, k = map(int, input().split())

cnt = 1
while k < p:
    k += 1
    cnt += 1

print(cnt)