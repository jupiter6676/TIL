import sys
from collections import deque
input = sys.stdin.readline

def pprint(mat):
    print('=========')
    for row in mat:
        for elem in row:
            print('%2d' % elem, end=' ')
        print()

def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    time = 0    # 현재 진행 시간

    # 상근이만 탈출하면 끝
    while q_sk:
        time += 1

        # 현재 진행 시간까지 불을 번지게 한다.
        while q_fire and q_fire[0][2] < time:
            fy, fx, ft = q_fire.popleft()   # ft: 해당 불이 번질 때의 시간
            
            for d in range(4):
                nfy = fy + dy[d]
                nfx = fx + dx[d]

                if -1 < nfy < H and -1 < nfx < W:
                    if graph[nfy][nfx] == '.' or graph[nfy][nfx] == '@':
                        graph[nfy][nfx] = '*'
                        q_fire.append([nfy, nfx, ft + 1])

        # 현재 진행 시간까지 상근이를 이동시킨다.
        while q_sk and q_sk[0][2] < time:
            sy, sx, st = q_sk.popleft()

            for d in range(4):
                nsy = sy + dy[d]
                nsx = sx + dx[d]

                if -1 < nsy < H and -1 < nsx < W:
                    if graph[nsy][nsx] == '.' and not visited[nsy][nsx]:
                        visited[nsy][nsx] = visited[sy][sx] + 1
                        q_sk.append([nsy, nsx, st + 1])

                else:   # 탈출했으면 그 때의 시간을 출력한다.
                    return time

    return 'IMPOSSIBLE'


'''main'''
for _ in range(int(input())):
    W, H = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]

    q_sk = deque()
    q_fire = deque()

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '@':
                visited[i][j] = 1
                q_sk.append([i, j, 0])
            if graph[i][j] == '*':
                q_fire.append([i, j, 0])

    print(bfs())

'''
1
7 6
#######
#..@..#
#.....#
#....*#
#.#.#*#
###.###
IMPOSSIBLE
'''

'''
1
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
5
'''

'''
1
7 7
#.#####
#.....#
#####.#
#....*#
####.##
#@....#
#####.#
impossible
'''

'''
1
12 5
############
#.#....@..##
#....#.#...#
.#..##...##.
.#..#####.#.
8
'''

'''
1
7 4
###.###
#.....#
#@....#
*######
'''

'''
1
5 5
###.#
*...#
##..#
#.@.#
#####
'''