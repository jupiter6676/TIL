r, g, b = map(int, input().split())

cnt = 0
for r_ in range(r):
    for g_ in range(g):
        for b_ in range(b):
            print(r_, g_, b_)
            cnt += 1

print(cnt)