import sys, heapq
input = sys.stdin.readline

def dijkstra(is_rev):   # 정방향: 0, 역방향: 1
    q = [[0, X]]
    dists[is_rev][X] = 0

    while q:
        w1, v = heapq.heappop(q)

        for adj, w2 in graph[is_rev][v]:
            if dists[is_rev][adj] > w1 + w2:
                dists[is_rev][adj] = w1 + w2
                heapq.heappush(q, [w1 + w2, adj])


'''main'''
V, E, X = map(int, input().split())

# [0] 정방향: 각 마을 → X 최단 거리, [1] 역방향: X → 각 마을 최단 거리
graph = [[[] for _ in range(V + 1)] for _ in range(2)]

# # [0] 정방향, [1] 역방향
dists = [[int(1e9)] * (V + 1) for _ in range(2)]

for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[0][v1].append([v2, w])    # 정방향
    graph[1][v2].append([v1, w])    # 역방향

dijkstra(0) # 정방향
dijkstra(1) # 역방향

res = 0
for i in range(1, V + 1):
    res = max(res, dists[0][i] + dists[1][i])
print(res)