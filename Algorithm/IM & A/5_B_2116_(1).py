def func(top):
    global max_sum

    for i in range(1, N):
        max_num = 0
        flag = False

        # i번째 주사위의 위, 아래 결정
        for j in range(3):
            if flag:    break

            for k in range(2):
                if dices[i][j][k] == top:
                    bottom = dices[i][j][k]

                    if k == 0:
                        top = dices[i][j][1]
                    else:
                        top = dices[i][j][0]
                    
                    flag = True
                    break
        
        # i번째 주사위의 위, 아래를 제외한 가장 큰 수 찾기
        for j in range(3):
            for k in range(2):
                if not (dices[i][j][k] == top or dices[i][j][k] == bottom):
                    if dices[i][j][k] > max_num:
                        max_num = dices[i][j][k]

        # 가장 큰 수를 더하기
        max_sum += max_num

    # 경우의 수 별로 주사위마다 가장 큰 수를 다 더한 값 저장
    sum_list.append(max_sum)
    
    return


N = int(input())
dices = [[] for _ in range(N)]


# i번째 주사위의 윗면, 아랫면 쌍들
for i in range(N):
    A, B, C, D, E, F = map(int, input().split())

    dices[i].append([A, F])
    dices[i].append([B, D])
    dices[i].append([C, E])

# for i in range(N):
#     print(dices[i])

sum_list = list()

# 첫 번째 주사위의 위, 아래 결정
for i in range(3):
    for j in range(2):
        top = dices[0][i][j]    # 위

        if j == 0:
            bottom = dices[0][i][1] # 아래
        else:
            bottom = dices[0][i][0]

        max_num = 0 # 위, 아래를 제외한 가장 큰 수
        max_sum = 0 # 경우의 수 별 주사위 별 가장 큰 수를 더해나간 합

        # 위, 아래를 제외한 가장 큰 수 찾기
        for k in range(3):
            for l in range(2):
                if not (dices[0][k][l] == top or dices[0][k][l] == bottom):
                    if dices[0][k][l] > max_num:
                        max_num = dices[0][k][l]

        max_sum += max_num

        # 첫 번째 주사위의 윗면이 결정되었으니,
        # 그걸 기준으로 두 번째 주사위부터 반복하는 함수
        func(top)

# print(sum_list)

# 모든 경우의 수에 대해 가장 큰 수 출력
print(max(sum_list))