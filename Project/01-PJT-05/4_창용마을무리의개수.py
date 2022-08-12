import sys

sys.stdin = open("_창용마을무리의개수.txt")

def dfs(start):
    stack.append(start)
    visited[start] = True

    while stack:
        pop = stack.pop()

        for adj in graph[pop]:
            if not visited[adj]:
                stack.append(adj)
                visited[adj] = True


T = int(input())

for tc in range(1, T + 1):
    # 마을 사람 수 N, 알고 있는 관계의 수 M
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    stack = list()
    visited = [False] * (N + 1)
    
    for _ in range(M):
        v1, v2 = map(int, input().split())

        graph[v1].append(v2)
        graph[v2].append(v1)

    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(f'#{tc}', cnt)