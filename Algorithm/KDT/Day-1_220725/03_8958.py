T = int(input())

for test_case in range(1, T + 1):
    ox = input()
    total_score = 0
    plus_score = 1

    for curr in ox:
        if curr == 'O':
            total_score += plus_score
            plus_score += 1 # 연속 정답이면 더해지는 점수도 1씩 증가
            continue

        plus_score = 1  # X가 나올 경우, 더해지는 점수 1로 초기화

    print(total_score)