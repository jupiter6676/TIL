import sys
from collections import deque
input = sys.stdin.readline

def bfs(root):
    q = deque([root])
    order = 1

    while q:
        v = q.popleft()
        visited[v] = order
        order += 1

        for adj in graph[v]:
            if not visited[adj]:
                visited[adj] = order
                q.append(adj)


'''main'''
V, E, R = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)

for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, V + 1):
    graph[i].sort()

bfs(R)
for i in range(1, V + 1):
    print(visited[i])