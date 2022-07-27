N = int(input())

res = 0
for c in range(N):
    sum_digits = sum(list(map(int, str(c))))
    d = c + sum_digits

    if d == N:
        res = c
        break

print(res)