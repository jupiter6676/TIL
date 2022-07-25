d1, d2, d3 = map(int, input().split())

prize = 0

# 모두 같은 눈
if d1 == d2 == d3:
    prize = 10000 + d1 * 1000
    print(prize)

elif d1 == d2:
    prize = 1000 + d1 * 100
    print(prize)

elif d2 == d3:
    prize = 1000 + d2 * 100
    print(prize)

elif d3 == d1:
    prize = 1000 + d3 * 100
    print(prize)

# 모두 다른 눈
else:
    prize = max(d1, d2, d3) * 100
    print(prize)