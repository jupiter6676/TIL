N = int(input())
dists = list(map(int, input().split()))     # 0 ~ (N - 2)
prices = list(map(int, input().split()))    # 0 ~ (N - 1)

min_price = prices[0]   # 주유소 값이 내릴 때 갱신
path = [min_price]

for i in range(1, N - 1):
    # 주유소 값이 내릴 때 갱신
    if min_price >= prices[i]:
        min_price = prices[i]

    path.append(min_price)  # 마을을 거쳐가면서, 그 때의 기름값을 기록

res = 0
for i in range(len(path)):
    res += path[i] * dists[i]

# print(path)
print(res)

'''
4
2 3 1
5 2 4 5

답: 10 + 8 = 18
'''