N = int(input())
way = list(map(int, input().split()))

height = list()  # 오르막길 높이들을 기록할 리스트
tmp = 0 # 오르막길의 높이를 증가시켜 나갈 임시 변수

for i in range(1, N):
    # 오르막 진행중
    if way[i] > way[i - 1]:
        tmp += way[i] - way[i - 1]

        # 오르막 진행중인데 길이 끝나면
        if i == N - 1:
            height.append(tmp)

    # 오르막이 끊기면
    else:
        height.append(tmp)   # 높이를 기록
        tmp = 0 # 높이 초기화

print(max(height))