N = int(input())

for _ in range(N):
    # 그림이 나온 개수
    # 세모 1, 네모 2, 동그라미 3, 별 4
    a_score = [0] * 5
    b_score = [0] * 5

    # a와 b가 낸 그림들
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    # 별, 동그라미, 네모, 세모 개수 세기
    for i in range(1, len(a_list)):
        a_score[a_list[i]] += 1
    
    for i in range(1, len(b_list)):
        b_score[b_list[i]] += 1

    # 별의 개수가 다르면, 별이 많은 쪽이 승리
    if a_score[4] != b_score[4]:
        print('A' if a_score[4] > b_score[4] else 'B')

    # 동그라미의 개수가 다르면, 동그라미가 많은 쪽이 승리
    elif a_score[3] != b_score[3]:
        print('A' if a_score[3] > b_score[3] else 'B')

    # 네모의 개수가 다르면, 네모가 많은 쪽이 승리
    elif a_score[2] != b_score[2]:
        print('A' if a_score[2] > b_score[2] else 'B')

    # 세모의 개수가 다르면, 세모가 많은 쪽이 승리
    elif a_score[1] != b_score[1]:
        print('A' if a_score[1] > b_score[1] else 'B')

    # 별, 동그라미, 네모, 세모가 모두 같으면 무승부
    # *_score[0]은 다를 수가 없으니까 신경 안 써도 O
    else:
        print('D')