import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([0])

    while q:
        x = q.popleft()

        for d in range(graph[x] + 1):
            nx = x + d

            if -1 < nx < N:
                if not visited[nx]:
                    visited[nx] = visited[x] + 1
                    q.append(nx)


'''main'''
N = int(input())
graph = list(map(int, input().split()))
visited = [0] * N

bfs()

if N == 1:
    print(0)
else:
    print(visited[-1] - 1 if visited[-1] != 0 else -1)