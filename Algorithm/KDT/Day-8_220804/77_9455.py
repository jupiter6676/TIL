T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(N)]
    dist = [0] * M

    tmp = 0
    # 0행부터 M행까지
    for j in range(M):
        # 떨어지는 박스가 여러개일 수 있으므로,
        # 여기서 tmp = 0으로 초기화해준다.
        tmp = 0

        # 박스를 아래로 떨어뜨리기
        # 바닥에서 위로 거슬러 올라가기
        for i in range(N - 1, -1, -1):
            # 0은 곧 박스가 이동해야 하는 거리
            if boxes[i][j] == 0:
                tmp += 1
            # 1은 바닥에서 올라가다가 박스를 만났을 때
            # 해당 상자가 이동한 거리를 저장
            else:
                dist[j] += tmp

    print(sum(dist))