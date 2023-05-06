'''
1. 트리에서 임의의 정점 x를 잡는다.
2. 정점 x에서 가장 먼 정점 y를 찾는다.
3. 정점 y에서 가장 먼 정점 z를 찾는다.

트리의 지름은 정점 y와 정점 z를 연결하는 경로다.
'''

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(root, w):
    for adj in graph[root]:
        nextNode, dist = adj

        if dists[nextNode] == -1:
            dists[nextNode] = dist + w
            dfs(nextNode, dist + w)

'''main'''
N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    v1, v2, e = map(int, input().split())
    graph[v1].append([v2, e])
    graph[v2].append([v1, e])

dists = [-1] * (N + 1)   # 1 ~ 각 노드의 거리 (+ 방문 체크)
dists[1] = 0
dfs(1, 0)

start = dists.index(max(dists)) # 1번과 가장 먼 노드
dists = [-1] * (N + 1)   # 1 ~ 각 노드의 거리 (+ 방문 체크)
dists[start] = 0
dfs(start, 0)

print(max(dists))