'''과거의 나'''
lst = list()

total = 0
for i in range(9):
    lst.append(int(input()))
    total += lst[i]

N = len(lst)
flag = False

# 총 9 난쟁이에, 진짜 난쟁이는 7명이니까
# 9명의 키를 다 더한 다음 2명의 키를 빼서 100이 되는지 확인
for i in range(N - 1):
    if flag:    break

    for j in range(i + 1, N):
        tmp = lst[i] + lst[j]
        
        if total - tmp == 100:
            lst[i] = -1
            lst[j] = -1
            
            flag = True
            break

lst.sort()

for num in lst:
    if num != -1:
        print(num)