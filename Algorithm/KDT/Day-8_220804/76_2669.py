area = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] += 1

cnt = 0
for row in area:
    for elem in row:
        if elem >= 1:
            cnt += 1

print(cnt)