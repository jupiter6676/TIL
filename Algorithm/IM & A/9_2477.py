K = int(input())

lst = list()

max_h = 0
max_w = 0

for _ in range(6):
    d, m = map(int, input().split())

    if d == 1 or d == 2:
        max_w = max(max_w, m)

    elif d == 3 or d == 4:
        max_h = max(max_h, m)
    
    lst.append(m)

big = max_w * max_h
small_h = 0
small_w = 0

for i in range(6):
    if lst[i] == max_h:
        if lst[(i + 1) % 6] == max_w:
            small_h = lst[(i + 4) % 6]
            small_w = lst[(i + 3) % 6]
        else:
            small_h = lst[(i + 2) % 6]
            small_w = lst[(i + 3) % 6]
    
    if lst[i] == max_w:
        if lst[(i + 1) % 6] == max_h:
            small_w = lst[(i + 4) % 6]
            small_h = lst[(i + 3) % 6]
        else:
            small_w = lst[(i + 2) % 6]
            small_h = lst[(i + 3) % 6]

small = small_w * small_h

print((big - small) * K)

'''
1
3 60
1 20
4 160
2 50
3 100
1 30
'''

'''
1
3 60
2 20
3 100
1 50
4 160
2 30
'''