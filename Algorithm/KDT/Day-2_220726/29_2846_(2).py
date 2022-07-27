N = int(input())
way = list(map(int, input().split()))

ascent_height = list()  # 오르막의 크기
sum_ = 0
for i in range(1, N):
    if way[i - 1] < way[i]:
        diff = way[i] - way[i - 1]
        sum_ += diff

        # 다음이 오르막 끝인데 아직 증가중인 경우
        if i + 1 == N - 1 and way[i] < way[i + 1]:
            sum_ += way[i + 1] - way[i]
            ascent_height.append(sum_)
    else:
        ascent_height.append(sum_)
        sum_ = 0

print(max(ascent_height))