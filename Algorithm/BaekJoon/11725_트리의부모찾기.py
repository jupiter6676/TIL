import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1

    for adj in graph[v]:
        if not visited[adj]:
            dfs(adj)
            parent[adj] = v


'''main'''
N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

parent = [0] * (N + 1)
visited = [0] * (N + 1)
dfs(1)

for i in range(2, N + 1):
    print(parent[i])