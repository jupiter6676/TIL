import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v):
    global cnt

    visited[v] = 1
    adj = nums[v]   # 인접 노드

    # 1. 인접 노드를 방문하지 않은 경우, dfs 수행
    if not visited[adj]:
        dfs(adj)

    # 2. 인접 노드를 방문했는데, 해당 노드의 dfs가 아직 끝나지 않은 경우
    #    = 순환해서 돌아온 경우, 사이클의 개수를 카운팅
    elif not finished[adj]:
        i = adj

        while i != v:
            cnt += 1
            i = nums[i]

        cnt += 1    # 자기 자신의 개수를 포함
 
    finished[v] = 1 # dfs가 모두 끝나면, 해당 노드의 dfs가 종료했음을 기록


'''main'''
for _ in range(int(input())):
    N = int(input())

    nums = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    finished = [0] * (N + 1)
    
    cnt = 0
    for v in range(1, N + 1):
        if not visited[v]:
            dfs(v)

    print(N - cnt)