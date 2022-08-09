from collections import deque


'''전역 변수'''
V = int(input())    # 컴퓨터(정점)의 수
E = int(input())    # 간선의 수

# 인덱스 1 ~ V까지
graph = [[] for _ in range(V + 1)]  # 인접 리스트
visited = [False] * (V + 1) # 정점 방문 체크

queue = deque()


'''BFS 탐색'''
def bfs(root):
    # 1번 정점을 큐에 추가, 방문 체크
    queue.append(root)
    visited[root] = True

    while queue:
        # 맨 앞 정점 큐에서 제거
        pop = queue.popleft()

        # 제거한 정점과 연결된 노드 탐색
        for adj in graph[pop]:
            # 해당 노드를 방문하지 않았으면
            if not visited[adj]:
                # 큐에 추가 후, 방문 체크
                queue.append(adj)
                visited[adj] = True

    # 1번 정점을 제외한
    # 방문한 모든 정점의 수가 곧 감염된 컴퓨터의 수이다.
    return sum(visited) - 1


'''메인'''
if __name__ == '__main__':
    # 인접 리스트 요소 입력
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)    # 방향으로 하면 틀리네..

    print(bfs(1))