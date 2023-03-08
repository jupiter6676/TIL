N = int(input())
lst_a = list(map(int, input().split()))

cnt = 0
while sum(lst_a) > 0:
    for i in range(N):
        if lst_a[i] % 2:
            lst_a[i] -= 1  # 원소 하나를 1 감소
            cnt += 1
            break
    else:
        # 모든 원소를 1/2배
        for i in range(N):
            lst_a[i] //= 2
        cnt += 1

    # print(lst_a)

print(cnt)