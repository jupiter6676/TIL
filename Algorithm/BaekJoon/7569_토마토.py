from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    # 상자 위, 상자 아래 / 상하좌우
    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    while q:
        z, y, x = q.popleft()

        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < nz < H and -1 < ny < R and -1 < nx < C):
                continue

            if boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = boxes[z][y][x] + 1
                q.append([nz, ny, nx])


'''main'''
C, R, H = map(int, input().split())

# 3차원 리스트
boxes = [
    [list(map(int, input().split())) for _ in range(R)] for _ in range(H)
]

q = deque()

for z in range(H):
    for y in range(R):
        for x in range(C):
            if boxes[z][y][x] == 1:
                q.append([z, y, x]) # 처음에 익은 토마토 다 담기

bfs()   # 익은 토마토 주변으로 익혀 나가기

res = 0
is_possible = True
for box in boxes:
    for row in box:
        for t in row:
            if t == 0:
                res = 0
                break

            res = max(res, t)
        else:
            continue
        break
    else:
        continue
    break

print(res - 1)

# print('=================')
# for box in boxes:
#     for row in box:
#         for t in row:
#             print(t, end=' ')
#         print()
#     print()

'''
// 이미 토마토가 다 익은 경우
1 1 1
1
정답 : 0
    
// 토마토를 처음에 한번에 몰아넣지 않은 경우
10 1 1
1 0 0 0 0 0 0 0 0 1
정답 : 4
    
// 가로 세로 입력 거꾸로 받은 경우
// 이럴 경우는 입력을 받을 때만 뒤집으면 통과합니다. 
    
    
// 3차원에 대한 고려 없음
3 3 2
0 0 1
0 -1 0
1 0 0
0 1 0
-1 0 0
0 0 0
정답 : 3
'''