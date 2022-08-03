T = int(input())
for t in range(T):
    a, b = map(int, input().split())

    money = 0
    
    if a != 0:
        if a == 1:
            money += 5000000
        elif a <= 3:
            money += 3000000
        elif a <= 6:
            money += 2000000
        elif a <= 10:
            money += 500000
        elif a <= 15:
            money += 300000
        elif a <= 21:
            money += 100000

    if b != 0:
        if b == 1:
            money += 5120000
        elif b <= 3:
            money += 2560000
        elif b <= 7:
            money += 1280000
        elif b <= 15:
            money += 640000
        elif b <= 31:
            money += 320000

    print(money)