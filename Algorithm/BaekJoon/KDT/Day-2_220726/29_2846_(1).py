N = int(input())
way = list(map(int, input().split()))

ascent_height = list()

min_height = way[0]
max_height = 0
for i in range(1, N - 1):
    # 오르막길 끝
    if way[i] >= way[i + 1]:
        max_height = way[i]
        diff = max_height - min_height
        ascent_height.append(diff)

        min_height = way[i + 1]

    # 오르막은 아직 안 끝났는데,
    # 다음이 배열 끝일 때
    elif way[i] < way[i + 1] and i + 1 == N - 1:
        max_height = way[i + 1]
        diff = max_height - min_height
        ascent_height.append(diff)

print(max(ascent_height))