N = int(input())

wh = list()    # (몸무게, 키)를 담는 리스트
rank = [1] * N   # 랭킹을 담는 리스트 (처음엔 다 1위로 초기화)

for i in range(N):
    w, h = map(int, input().split())
    wh.append((w, h))

for i in range(N):  # i는 자기 자신
    for j in range(N):  # j는 비교 대상
        # 비교 대상이 자기 자신일 경우, 건너뛰기
        if i == j:
            continue

        # 나의 몸무게와 키 모두 상대보다 작으면
        # 등수 내리기
        if wh[i][0] < wh[j][0] and wh[i][1] < wh[j][1]:
            rank[i] += 1

for i in rank:
    print(i, end=' ')