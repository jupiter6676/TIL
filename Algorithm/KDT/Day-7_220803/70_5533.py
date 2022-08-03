N = int(input())    # 참가자의 수

# N * 3의 2D list
nums = [list(map(int, input().split())) for _ in range(N)]

# 각 참가자의 최종 점수 저장 배열
scores = [0] * N

# c번째 게임
for c in range(3):
    # r번째 플레이어
    for r in range(N):
        for i in range(N):
            # 자기 자신을 제외하고,
            # 자신과 같은 숫자를 낸 사람이 있으면 break
            if nums[r][c] == nums[i][c] and r != i:
                break
        # 자신과 같은 숫자를 낸 사람이 없으면 점수 +
        else:
            scores[r] += nums[r][c]

for score in scores:
    print(score)