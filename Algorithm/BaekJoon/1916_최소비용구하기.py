import sys
import heapq
input = sys.stdin.readline

def dijkstra():
    q = [[0, start]]
    dists[start] = 0

    while q:
        w1, v = heapq.heappop(q)

        for adj, w2 in graph[v]:
            if dists[adj] > w1 + w2:
                dists[adj] = w1 + w2
                heapq.heappush(q, [w1 + w2, adj])

    return


V = int(input())
E = int(input())
graph = [[] for _ in range(V + 1)]
dists = [int(1e9)] * (V + 1)

for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append([v2, w])

for v1 in range(1, V + 1):
    # 같은 경로이지만 비용이 다른 경로 O
    # → 비용이 작은 순으로 정렬해서, 우선순위 큐에 중복으로 들어가는 걸 방지
    graph[v1].sort(key=lambda x: x[1])

start, end = map(int, input().split())

dijkstra()
print(dists[end])

'''
3
7
1 2 100
1 2 50
1 2 10
2 3 2
1 3 5
3 1 1
1 1 1
1 3
'''