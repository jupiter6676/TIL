# https://yabmoons.tistory.com/364
import sys
import heapq    # 최소 힙
input = sys.stdin.readline

def dijkstra():
    pq = [[0, K]]   # [가중치, 인접노드]의 쌍
    dists[K] = 0

    while pq:
        # 현재 노드와 연결된 노드 중 가장 가중치가 작은 노드(v1)를 꺼냄
        w1, v1 = heapq.heappop(pq)

        # 그 노드와 연결된 노드(v2)를 확인
        for v2, w2 in graph[v1]:
            # v1을 거치는 경우의 비용이 더 적을 경우 값을 갱신
            if dists[v2] > w1 + w2:
                dists[v2] = w1 + w2
                heapq.heappush(pq, [w1 + w2, v2])

    return


'''main'''
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
dists = [int(1e9)] * (V + 1)

for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append([v2, w])

dijkstra()
for i in range(1, V + 1):
    print('INF' if dists[i] == int(1e9) else dists[i])

'''
4 5
1
1 2 4
2 3 3
1 3 1
1 3 2
3 4 1
답: 0 4 1 2

4 3
1
1 2 10
2 3 10
3 4 10
답: 0 10 20 30

10 9
1
1 2 9
2 8 9
7 3 10
5 6 6
3 4 7
4 5 2
6 10 8
8 5 4
2 3 10
답: 0 9 19 26 22 28 INF 18 INF 36
'''