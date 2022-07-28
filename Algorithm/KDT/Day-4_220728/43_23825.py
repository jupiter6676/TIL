# S의 개수 n, A의 개수 m
n, m = map(int, input().split())

# print(min(n // 2, m // 2))
if n <= m:
    print(n // 2)
else:
    print(m // 2)