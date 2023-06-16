import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    pq = [[dists[start], start]]
    
    while pq:
        w1, v1 = heapq.heappop(pq)

        for v2, w2 in graph[v1]:
            if dists[v2] > w1 + w2:
                dists[v2] = w1 + w2
                heapq.heappush(pq, [w1 + w2, v2])


'''main'''
INF = int(1e10)
V, E, K, start = map(int, input().split())
graph = [[] for _ in range(V + 1)]
dists = [INF] * (V + 1)
dists[start] = 0

for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append([v2, 1])

dijkstra(start)
res = list()
for i in range(1, V + 1):
    if dists[i] == K:
        res.append(i)

if res:
    for elem in res:
        print(elem)
else:
    print(-1)