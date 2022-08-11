M, n = map(int, input().split())

y, x = 0, 0

right_cnt = 1   # 우회전 횟수
flag = True

for _ in range(n):
    command, num = input().split()
    num = int(num)

    if command == 'MOVE':
        # y좌표 증가
        if right_cnt % 4 == 0:
            ny = y + num
            nx = x

        # x좌표 증가
        if right_cnt % 4 == 1:
            ny = y
            nx = x + num

        # y좌표 감소
        if right_cnt % 4 == 2:
            ny = y - num
            nx = x

        # x좌표 감소
        if right_cnt % 4 == 3:
            ny = y
            nx = x - num

        if not (0 <= nx <= M and 0 <= ny <= M):
            flag = False
            break

        x = nx
        y = ny

    else:
        if num == 0:
            right_cnt -= 1
        else:
            right_cnt += 1

if flag:
    print(x, y)
else:
    print(-1)