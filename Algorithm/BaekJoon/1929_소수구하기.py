M, N = map(int, input().split())
lst = [1] * (N + 1)
lst[0] = 0
lst[1] = 0

for i in range(2, N + 1):
    j = 2
    while True:
        if i * j > N:
            break

        lst[i * j] = 0
        j += 1

for i in range(M, N + 1):
    if lst[i]:
        print(i)