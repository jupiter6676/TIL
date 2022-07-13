n = int(input())

i = 1
while i <= n:
    if i % 3 != 0:
        print(i, end=' ')
    i += 1

'''
for i in range(1, n+1) :
    if i%2==0 :
        continue
    print(i, end=' ')
'''