''' 변수 선언 '''
V = int(input())
a, b = map(int, input().split()) # 촌수 계산 대상
E = int(input())

graph = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)
dist = [0] * (V + 1)    # a 정점 ~ 각 정점까지의 거리를 저장할 배열


''' dfs 함수 '''
def dfs(start, end):
    visited[start] = 1

    # 현재 정점(start)의 인접 정점(adj) 탐색
    for adj in graph[start]:
        # 인접 정점을 아직 방문하지 않았다면,
        if not visited[adj]:
            visited[adj] = 1
            # start와 인접 정점의 거리 차이는 1
            # a 정점 ~ adj 정점까지의 거리
            # = a 정점 ~ start 정점까지의 거리 + 1
            dist[adj] = dist[start] + 1
            
            # start의 인접노드에 대해, dfs를 다시 수행
            dfs(adj, end)
    
    return


''' 메인 '''
# 그래프 정보 입력
for _ in range(E):
    v1, v2 =  map(int, input().split())

    graph[v1].append(v2)
    graph[v2].append(v1)

# a를 시작으로, 연결된 정점들을 모두 방문
dfs(a, b)

# dist[b]: a ~ b까지의 거리
# 만약 dist[b]가 0이면, 촌수가 없는 것이므로 -1 출력
print(dist[b] if dist[b] else -1)