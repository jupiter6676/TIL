H, M = map(int, input().split())

if M >= 45:
    print(H, M - 45)

else:
    if H == 0:
        print(23, M + 15)   # 60 + M - 45
    else:
        print(H - 1, M + 15)