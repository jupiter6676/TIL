arr2D = [list(input()) for _ in range(8)]

cnt = 0

for i in range(8):
    for j in range(8):
        # 두 인덱스의 합이 짝수면, 하얀 칸
        if (i + j) % 2 == 0 and arr2D[i][j] == 'F':
            cnt += 1

print(cnt)