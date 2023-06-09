# https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-16197%EB%B2%88-%EB%91%90-%EB%8F%99%EC%A0%84-1-Python
# https://yabmoons.tistory.com/61
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y1, x1, y2, x2, cnt = q.popleft()

        if cnt >= 10:
            return -1

        for d in range(4):
            ny1 = y1 + dy[d]
            nx1 = x1 + dx[d]
            ny2 = y2 + dy[d]
            nx2 = x2 + dx[d]
            
            if (-1 < ny1 < R and -1 < nx1 < C) and (-1 < ny2 < R and -1 < nx2 < C):
                # 벽일 경우 → 되돌아가기
                if graph[ny1][nx1] == '#':
                    ny1 = y1
                    nx1 = x1

                if graph[ny2][nx2] == '#':
                    ny2 = y2
                    nx2 = x2

                # 벽이든 아니든 이동
                q.append([ny1, nx1, ny2, nx2, cnt + 1])

            # 2번 동전이 떨어질 경우 (= 1번 동전만 범위 내)
            elif -1 < ny1 < R and -1 < nx1 < C:
                return cnt + 1
            
            # 1번 동전이 떨어질 경우 (= 2번 동전만 범위 내)
            elif -1 < ny2 < R and -1 < nx2 < C:
                return cnt + 1

            # 1번 2번 동전이 모두 떨어질 경우
            else:
                continue

    return -1


'''main'''
R, C = map(int, input().split())
graph = list()
q = deque()
tmp = list()

for i in range(R):
    graph.append(list(input().rstrip()))

    for j in range(C):
        if graph[i][j] == 'o':
            tmp.append([i, j])

q.append([tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1], 0])
print(bfs())