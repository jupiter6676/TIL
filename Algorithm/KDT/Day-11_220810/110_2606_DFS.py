''' 변수 선언 '''
V = int(input())
E = int(input())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
stack = list()


''' dfs 함수 '''
def dfs(start):
    stack.append(start)
    visited[start] = True

    while stack:
        pop = stack.pop()

        for adj in graph[pop]:
            if not visited[adj]:
                stack.append(adj)
                visited[adj] = True

    return sum(visited) - 1


''' 메인 '''
# 그래프 정보 입력
for _ in range(E):
    v1, v2 =  map(int, input().split())

    graph[v1].append(v2)
    graph[v2].append(v1)

print(dfs(1))