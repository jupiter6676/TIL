import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

# 진입 차수가 0인 걸 큐에 넣는다.
# 큐에서 노드를 뺀다.
# 노드와 연결된 간선을 제거한다.
# 진입 차수가 새로 0이 된 노드를 큐에 넣는다..

'''위상 정렬'''
def topology_sort(root):
    visited = [False] * (V + 1)
    q = deque()
    seq = list()    # 순서를 담을 리스트
    
    visited[root] = True
    q.append(root)
    
    while q:
        pop = q.popleft()

        # 해당 노드와 연결 된 간선 모두 제거
        # 즉, 인접 노드의 진입 차수를 1씩 깎는다.
        for adj in graph[pop]:
            indegree[adj] -= 1

        for v in range(1, V + 1):
            if indegree[v] == 0 and not visited[v]:
                q.append(v)
                visited[v] = True

        seq.append(pop)

    return seq

'''main'''
for t in range(1, 11):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    
    graph = [[] for _ in range(V + 1)]  # 인접 리스트, 방향 그래프
    indegree = [0] * (V + 1)  # 각 정점의 진입 차수

    # 0 ~ (E * 2 - 1)까지 총 (E * 2)개의 간선, i += 2
    for i in range(0, E * 2, 2):
        v1 = edges[i]
        v2 = edges[i + 1]
        
        graph[v1].append(v2)    # 방향 그래프
        indegree[v2] += 1


    # 모든 정점에 대해서 위상 정렬 실행
    print(f'#{t}', end=' ')
    for v in range(1, V + 1):
        # 처음에 진입 차수가 0인 정점을 큐에 넣어준다.
        if indegree[v] == 0:
            seq = topology_sort(v)
            print(*seq)
            break