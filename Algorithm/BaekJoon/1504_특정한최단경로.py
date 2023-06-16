import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    dists = [INF] * (V + 1)
    dists[start] = 0

    pq = [[dists[start], start]]
    
    while pq:
        w1, v1 = heapq.heappop(pq)

        for v2, w2 in graph[v1]:
            if dists[v2] > w1 + w2:
                dists[v2] = w1 + w2
                heapq.heappush(pq, [w1 + w2, v2])

    # print(f'#{start}: {dists}')
    return dists


'''main'''
INF = int(1e10)
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append([v2, w])
    graph[v2].append([v1, w])

a, b = map(int, input().split())    # 지나야 하는 두 정점
path = [0] * 2  # 1 → a → b → V, 1 → b → a → V

dists = dijkstra(1) # 1 → a, 1 → b 구하기
if path[0] != INF:
    path[0] += dists[a] # 1 → a
if path[1] != INF:
    path[1] += dists[b] # 1 → a

dists = dijkstra(a) # a → b, a → V 구하기
if path[0] != INF:
    path[0] += dists[b] # a → b
if path[1] != INF:
    path[1] += dists[V] # (b) → a → V

dists = dijkstra(b) # b → a, b → V 구하기
if path[0] != INF:
    path[0] += dists[V] # a → b → V
if path[1] != INF:
    path[1] += dists[a] # b → a → V

res = min(path)
print(res if res < INF else -1)