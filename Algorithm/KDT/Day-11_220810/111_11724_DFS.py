''' 시간 초과 방지 '''
import sys
input = sys.stdin.readline

''' 변수 선언 '''
V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
stack = list()

# 연결 요소
connected_cnt = 0

''' dfs 함수 '''
# dfs를 한 번 수행할 때마다, connected_cnt가 1씩 증가
def dfs(start):
    # 전역변수 connected_cnt 사용
    global connected_cnt

    stack.append(start)
    visited[start] = True

    while stack:
        pop = stack.pop()

        for adj in graph[pop]:
            if not visited[adj]:
                stack.append(adj)
                visited[adj] = True

    connected_cnt += 1

    return


''' 메인 '''
# 그래프 정보 입력
for _ in range(E):
    v1, v2 =  map(int, input().split())

    graph[v1].append(v2)
    graph[v2].append(v1)

# 연결 요소를 찾기 위해, dfs 탐색을 수행
for i in range(1, V + 1):
    # 방문하지 않은 정점이 새로운 start 정점이 된다.
    if not visited[i]:
        dfs(i)

print(connected_cnt)