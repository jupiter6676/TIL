total = 0
lst = list()

for _ in range(9):
    n = int(input())

    total += n
    lst.append(n)

lst.sort()

flag = False

for i in range(8):
    for j in range(i + 1, 9):
        if total - lst[i] - lst[j] == 100:
            flag = True
            break
    
    # i가 한 번 더 +1 되는 걸 막음.
    if flag:    break

for k in range(9):
    if not (k == i or k == j):
        print(lst[k])