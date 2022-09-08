N = int(input())
lst = list(map(int, input().split()))

asc = [1] * N
desc = [1] * N

for i in range(1, N):
    if lst[i] >= lst[i - 1]:
        asc[i] = asc[i - 1] + 1
    if lst[i] <= lst[i - 1]:
        desc[i] = desc[i - 1] + 1

max_asc = max(asc)
max_desc = max(desc)

print(max(max_asc, max_desc))