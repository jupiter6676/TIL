''' 전역 변수 '''
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
stack = list()

cnt = 0 # 그림 개수
max_area = 0    # 최대 그림 넓이


# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

''' DFS '''
def dfs(y, x):
    area = 0

    stack.append((y, x))
    visited[y][x] = True

    while stack:
        pop = stack.pop()
        area += 1

        for d in range(4):
            ny = pop[0] + dy[d]
            nx = pop[1] + dx[d]

            if not (0 <= ny < N and 0 <= nx < M):
                continue
            
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                stack.append((ny, nx))
                visited[ny][nx] = True

    return area


''' 메인 '''
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            area = dfs(i, j)

            if max_area < area:
                max_area = area
            cnt += 1

print(cnt)
print(max_area)

# for i in graph:
#     for j in i:
#         print(j, end=' ')
#     print()