import sys
import heapq
input = sys.stdin.readline

def pprint(mat):
    print('================')
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            print(mat[i][j], end=' ')
        print()

def dijkstra(start):
    dists = [int(1e9)] * (V + 1)
    dists[start] = 0
    
    q = [[0, start]]
    visited = [0] * (V + 1)

    while q:
        w1, v1 = heapq.heappop(q)

        for adj, w2 in graph[v1]:
            if not visited[adj] and dists[adj] >= w1 + w2:
                dists[adj] = w1 + w2

                if v1 == start:
                    path[start][adj] = adj
                else:
                    path[start][adj] = v1

                # path[v1][adj] = adj

                # path[adj][v1] = v1
                # path[adj][start] = start
                visited[adj] = 1
                heapq.heappush(q, [w1 + w2, adj])

    print(start, dists)



V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
path = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append([v2, w])
    graph[v2].append([v1, w])

for i in range(1, V + 1):
    dijkstra(i)

for i in range(V, 0, -1):
    dijkstra(i)

pprint(path)
# dijkstar(V)