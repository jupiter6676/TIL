N = int(input())
lst = list()

for _ in range(N):
    num = int(input())
    lst.append(num)

lst.sort()

for num in lst:
    print(num)