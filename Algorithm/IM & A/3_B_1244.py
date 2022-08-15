# 스위치의 개수
N = int(input())
# 스위치의 상태
status = list(map(int, input().split()))
# 학생 수
M = int(input())
# 성별, 받은 수 저장
control = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    # 현재 학생이 남학생
    if control[i][0] == 1:
        tmp = control[i][1] # 받은 수

        # 받은 수의 배수 번호에 있는 스위치 상태를 바꿈
        # 스위치 인덱스가 0부터 시작하므로, 마지막에 -1
        j = 1   # j 배수
        while True:
            if tmp * j - 1 >= N:    break

            status[tmp * j - 1] = int(not status[tmp * j - 1])
            j += 1
    
    # 현재 학생이 여학생
    else:
        tmp = control[i][1] - 1 # 받은 수

        # 받은 수를 기준으로, 양 옆이 대칭이면 상태를 바꿈 (최대)
        # 대칭이 아니면 받은 수에 해당하는 스위치 상태를 바꿈
        # 스위치 인덱스가 0부터 시작하므로, 마지막에 -1
        j = 1
        while True:
            # 인덱스 범위 벗어나는 즉시 반복 종료
            if tmp - j < 0 or tmp + j >= N:
                status[tmp] = int(not status[tmp])
                break

            # 처음에 받은 수 기준으로 양옆이 대칭이 아니면 반복 종료
            if j == 1 and status[tmp - j] != status[tmp + j]:
                status[tmp] = int(not status[tmp])
                break
            
            # 대칭이 아니면 즉시 반복 종료
            if status[tmp - j] != status[tmp + j]:
                status[tmp] = int(not status[tmp])
                break

            status[tmp - j] = int(not status[tmp - j])
            status[tmp + j] = int(not status[tmp + j])

            j += 1

cnt = 0
for i in range(len(status)):
    print(status[i], end=' ')
    cnt += 1

    if cnt % 20 == 0:
        print()

'''
25
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
1
1 1
'''