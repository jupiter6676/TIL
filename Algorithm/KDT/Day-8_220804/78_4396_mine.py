'''
8
...**..*
......*.
....*...
........
........
.....*..
...**.*.
.....*..
xxxx....
xxxx....
xxxx....
xxxxx...
xxxxx...
xxxxx...
xxx.....
xxxxx...
'''

N = int(input())

# 지뢰의 위치
mine = [list(input()) for _ in range(N)]

# 플레이어에 의해 열린 곳
opened = [list(input()) for _ in range(N)]

# 지뢰, 열린 곳의 위치
res = [list('.' * N) for _ in range(N)]

mine_cnt = 0
dir = [-1, 0, 1]
flag = False    # 지뢰를 밟았는지

for i in range(N):
    for j in range(N):
        mine_cnt = 0

        # 플레이어가 연 칸을 탐색
        if opened[i][j] == 'x':
            # 만약 지뢰를 밟았으면, flag를 True로
            if mine[i][j] == '*':
                flag = True

            # 연 칸의 8방향을 확인하여, 지뢰의 개수를 구한다.
            for dy in dir:
                for dx in dir:
                    # 배열 크기 벗어나면 건너뛰기
                    if i + dy < 0 or j + dx < 0 or i + dy >= N or j + dx >= N:
                        continue
                    
                    # 주변에 지뢰가 있으면 지뢰 카운트 증가
                    if mine[i + dy][j + dx] == '*':
                        mine_cnt += 1

                    # 지뢰의 개수를 표시
                    res[i][j] = str(mine_cnt)

# 지뢰를 밟았으면, 지도에 모든 지뢰를 표시
if flag:
    for i in range(N):
        for j in range(N):
            if mine[i][j] == '*':
                res[i][j] = '*'

# 지도 출력
for i in range(N):
    for j in range(N):
        print(res[i][j], end='')
    print()