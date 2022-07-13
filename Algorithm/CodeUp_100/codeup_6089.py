a, r, n = map(int, input().split())

i = 1
while i < n:
    a *= r
    i += 1

print(a)