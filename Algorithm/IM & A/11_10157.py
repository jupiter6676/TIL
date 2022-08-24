C, R = map(int, input().split())
K = int(input())

lst = [[0] * C for _ in range(R)]

flag = False    # K번째 좌석을 찾으면 flag = True, 모든 반복 종료

cnt = 0
last_i = 0  # 상/하로 이동한 후, 마지막 y좌표 저장
last_j = 0  # 좌/우로 이동한 후, 마지막 x좌표 저장

while True:
    if flag:    break

    # 모든 좌석을 탐색할 동안 flag가 false
    # 즉, 모든 좌석이 배정되어, 해당 관객에게 좌석을 배정할 수 없는 경우
    # 0을 출력
    elif cnt == R * C:
        print(0)
        break

    # 1. 위로 (리스트 상에서는 아래로)
    # 마지막으로 저장된 y좌표 ~ y좌표의 끝까지 반복
    for i in range(last_i, R):
        # x좌표는 마지막으로 저장된 x좌표로 고정, y좌표만 변동되며
        # 이미 배정된 좌석(1)인 경우 위로 이동 종료
        if lst[i][last_j] == 1:
            # 마지막 검사를 위해 의도보다 한 칸 더 이동했으므로,
            # 마지막에 i에 -1을 해준다.
            i -= 1
            break
        
        lst[i][last_j] = 1  # 좌석 배정
        cnt += 1    # 배정된 좌석 수 +1

        # 반복 중, 배정된 좌석 수가 K와 일치하면
        if cnt == K:
            # 그 때의 x좌표와 y좌표를 출력하고 반복을 종료한다.
            print(last_j + 1, i + 1)
            flag = True
            break
    
    # 변동된 y좌표의 마지막 위치를 저장하고,
    # 다음 반복의 시작 지점을 오른쪽으로 한 칸 이동시킨다.
    last_i = i
    last_j += 1

    # 2. 오른쪽으로
    for j in range(last_j, C):
        if lst[last_i][j] == 1:
            j -= 1
            break

        lst[last_i][j] = 1
        cnt += 1

        if cnt == K:
            print(j + 1, last_i + 1)
            flag = True
            break

    last_j = j
    last_i -= 1

    # 3. 아래로 (리스트 상에서는 위로)
    for i in range(last_i, -1, -1):
        if lst[i][last_j] == 1:
            i += 1
            break

        lst[i][last_j] = 1
        cnt += 1

        if cnt == K:
            print(last_j + 1, i + 1)
            flag = True
            break

    last_i = i
    last_j -= 1

    # 4. 왼쪽으로
    for j in range(last_j, -1, -1):
        if lst[last_i][j] == 1:
            j += 1
            break

        lst[last_i][j] = 1
        cnt += 1

        if cnt == K:
            print(j + 1, last_i + 1)
            flag = True
            break

    last_j = j
    last_i += 1