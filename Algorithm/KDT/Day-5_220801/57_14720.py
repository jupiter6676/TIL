N = int(input())
milk = list(map(int, input().split()))
# [1, 0, 1, 2, 0, 2, 1]    # 5개

# 딸기(0) > 초코(1) > 바나나(2) > 딸기 > ...
cnt = 0
for i in range(len(milk)):
    # 처음엔 딸기 우유를 먹어야 함.
    if cnt == 0:
        if milk[i] != 0:
            continue
        else:
            prev = 0    # 마지막으로 먹은 건 딸기 우유 (0)
            cnt += 1

    # 마지막 딸기(0) 먹고, 현재 바나나(1)
    if prev == 0 and milk[i] == 1:
        prev = 1    # 바나나(1) 먹기
        cnt += 1    # 먹은 우유 개수 +1
        
    elif prev == 1 and milk[i] == 2:
        prev = 2
        cnt += 1
        
    elif prev == 2 and milk[i] == 0:
        prev = 0
        cnt += 1

print(cnt)