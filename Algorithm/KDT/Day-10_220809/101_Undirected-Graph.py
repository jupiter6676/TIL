from pprint import pprint


N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
adj_matrix = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())

    # 인접 리스트
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

    # 인접 행렬
    adj_matrix[v1][v2] = 1
    adj_matrix[v2][v1] = 1

pprint(adj_matrix)
print(adj_list)