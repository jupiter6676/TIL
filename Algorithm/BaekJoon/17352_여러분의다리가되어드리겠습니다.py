import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1

    for adj in graph[v]:
        if not visited[adj]:
            dfs(adj)

    group[curr].append(v)

'''main'''
N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 2):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

group = [[] for _ in range(2)]
curr = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        curr += 1

# print(group)
print(group[0][0], group[1][0])