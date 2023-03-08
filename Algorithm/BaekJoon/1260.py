from collections import deque

def dfs(root):
    dfs_visited[root] = True

    for adj in graph[root]:
        if not dfs_visited[adj]:
            dfs_visited[adj] = True
            dfs_path.append(adj)
            dfs(adj)


def bfs(root):
    bfs_visited[root] = True
    q.append(root)

    while q:
        pop = q.popleft()

        for adj in graph[pop]:
            if not bfs_visited[adj]:
                bfs_visited[adj] = True
                bfs_path.append(adj)
                q.append(adj)


'''main'''
V, E, root = map(int, input().split())
graph = [[] for _ in range(V + 1)]

dfs_visited = [False] * (V + 1)
dfs_path = [root]

bfs_visited = [False] * (V + 1)
bfs_path = [root]
q = deque()

for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, V + 1):
    graph[i].sort()

# print(graph)

dfs(root)
print(*dfs_path)

bfs(root)
print(*bfs_path)