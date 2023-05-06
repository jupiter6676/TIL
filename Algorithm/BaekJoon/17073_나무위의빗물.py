import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(n):
    visited[n] = 1

    c_cnt = 0   # 자식 노드 카운트
    for adj in tree[n]:
        if not visited[adj]:
            c_cnt += 1
            dfs(adj)

    if c_cnt == 0:
        no_child.append(n)   # 자식이 없는 노드


'''main'''
N, W = map(int, input().split())
tree = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
no_child = list()

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1)
print(W / len(no_child))