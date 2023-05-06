import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v):
    global v_id

    stack.append(v)
    visited[v] = v_id   # v 노드를 방문한 순서
    v_id += 1

    p = visited[v]      # 부모 = SCC 중 제일 처음 방문한 노드 (우선은 v 노드의 방문 순서를 저장)
    for adj in graph[v]:
        # 인접 노드를 방문하지 않았다면
        if not visited[adj]:
            # 인접 노드의 방문 순서와 비교해서, 더 작은 값을 저장
            p = min(p, dfs(adj))

        # 인접 노드가 이미 방문한 곳이고, dfs가 끝나지 않았으면
        elif not finished[adj]:
            # 해당 인접 노드의 p와 내 방문 순서 중 더 작은 값을 저장
            # 만약 인접 노드의 p가 더 작으면, 그 노드가 나의 부모이다.
            p = min(p, visited[adj])

    # 인접 노드들의 dfs 종료 후, 부모가 자신이라면 SCC를 찾은 것
    if p == visited[v]:
        scc = list()

        while True:
            pop = stack.pop()
            
            scc.append(pop)
            finished[pop] = True

            if pop == v:
                break

        scc.sort()
        scc.append(-1)
        scc_all.append(scc)

    return p        


'''main'''
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

v_id = 1    # 정점의 고유 id
visited = [0] * (V + 1)     # 정점 방문 여부
finished = [0] * (V + 1)    # 해당 정점에서의 dfs가 끝났는지의 여부
stack = list()

for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

    graph[v1].sort()

scc_all = list()

for i in range(1, V + 1):
    if not visited[i]:
        dfs(i)

scc_all.sort()

print(len(scc_all))
for scc in scc_all:
    print(*scc)