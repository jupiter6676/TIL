import sys
from collections import deque
input = sys.stdin.readline

def pprint(mat):
    print('=====================')
    for row in mat:
        for elem in row:
            print(elem, end=' ')
        print()

def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while True:
        flag = False    # 성을 확장했는지

        for i in range(1, P + 1):
            if not castle[i]:
                continue

            q = castle[i]

            for _ in range(S[i]):  
                if not q:
                    break

                # while q:
                for _ in range(len(q)):
                    y, x = q.popleft()

                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if -1 < ny < N and -1 < nx < M:
                            if graph[ny][nx] == '.':
                                graph[ny][nx] = str(i)  # i번째 플레이어의 성
                                q.append([ny, nx])
                                cnt[i] += 1

                                flag = True

            pprint(graph)
            print(castle)

        if not flag:    # 한 번도 확장하지 않았으면 종료
            break


'''main'''
N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
graph = [list(input().rstrip()) for _ in range(N)]

castle = [0] + [deque() for _ in range(P)]
cnt = [0] * (P + 1)
finished = [1] * (P + 1)

for i in range(N):
    for j in range(M):
        if graph[i][j] != '.' and graph[i][j] != '#':
            p = int(graph[i][j])
            cnt[p] += 1
            castle[p].append([i, j])

bfs()
print(*cnt[1:])

'''
5 4 2
1 1
1...
###.
....
.###
..#2
'''