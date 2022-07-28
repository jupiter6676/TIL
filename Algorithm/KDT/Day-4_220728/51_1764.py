n, m = map(int, input().split())

H = set()   # 듣도 못한
S = set()   # 보도 못한

for _ in range(n):
    name = input()
    H.add(name)

for _ in range(m):
    name = input()
    S.add(name)

# 듣도 보도 못한
# 사전 순으로 정렬
H_and_S = sorted(H.intersection(S))

print(len(H_and_S))
for element in H_and_S:
    print(element)