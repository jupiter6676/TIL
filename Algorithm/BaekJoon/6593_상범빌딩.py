import sys
from collections import deque
input = sys.stdin.readline

def pprint(mat):
    print('===============')
    for l in mat:
        for row in l:
            for elem in row:
                print(elem, end=' ')
            print()
        print()

def bfs():
    q = deque()
    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    visited[start[0]][start[1]][start[2]] = 1
    q.append([start[0], start[1], start[2]])

    while q:
        z, y, x = q.popleft()

        if z == end[0] and y == end[1] and x == end[2]:
            return visited[z][y][x]

        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < nz < L and -1 < ny < R and -1 < nx < C):
                continue

            if graph[nz][ny][nx] != '#' and not visited[nz][ny][nx]:
                visited[nz][ny][nx] = visited[z][y][x] + 1
                q.append([nz, ny, nx])


while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    graph = [[] for _ in range(L)]
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]

    for l in range(L):
        for r in range(R + 1):
            tmp = input().rstrip()

            if tmp:
                graph[l].append(list(tmp))

    for l in range(L):
        for r in range(R):
            for c in range(C):
                if graph[l][r][c] == 'S':
                    start = [l, r, c]

                if graph[l][r][c] == 'E':
                    end = [l, r, c]

    res = bfs()

    if res:
        print(f'Escaped in {res - 1} minute(s).')
    else:
        print('Trapped!')

'''
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E
'''