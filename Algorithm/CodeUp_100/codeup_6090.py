a, m, d, n = map(int, input().split())

i = 1
while i < n:
    a *= m
    a += d
    
    i += 1

print(a)