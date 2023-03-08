S = int(input())

'''
1 = 1
1 + 2 = 3
1 + 2 + 3 + 4 = 10
'''

N = 0
sum_ = 0
while True:
    if sum_ >= S:
        break

    N += 1
    sum_ += N

    # print(N, sum_)

res = N if sum_ == S else N - 1

print(res if N > 1 else 1)