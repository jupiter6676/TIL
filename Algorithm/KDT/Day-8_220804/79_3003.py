# 킹, 퀸, 룩, 비숍, 나이트, 폰
# 1, 1, 2, 2, 2, 8
pieces = list(map(int, input().split()))
res = [1, 1, 2, 2, 2, 8]

for i in range(len(pieces)):
    res[i] -= pieces[i]

print(*res)