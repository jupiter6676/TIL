N = input()
j = N

if len(N) <= 2:
    print(N)    # 1 ~ 99는 모두 한수

else:
    cnt = 0
    # 100부터 N까지 순회
    for num in range(100, int(N) + 1):
        num = str(num)

        # 초기 공차
        d0 = int(num[0]) - int(num[1])

        for j in range(1, len(num) - 1):
            d = int(num[j]) - int(num[j + 1])

            if d0 == d:
                cnt += 1
                continue
            else:
                break

    print(99 + cnt)