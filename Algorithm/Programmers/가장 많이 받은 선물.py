import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def pprint(arr):
    for row in arr:
        for elem in row:
            print(elem, end=', ')
        print()

def solution(friends, gifts):
    n = len(friends)    # 친구의 수
    idx_dict = {}       # 친구 이름 - 배열 인덱스 매핑
    for i in range(n):
        idx_dict[friends[i]] = idx_dict.get(0, i)

    gift_map = [[0] * n for _ in range(n)] # 친구 간 주고 받은 선물 개수
    gift_score = [0] * n    # 각자의 선물 지수
    gift_next = [0] * n     # 다음 달에 각자 받을 선물 개수

    # 이번 달 주고받은 선물의 개수 및 선물 지수
    for gift in gifts:
        a, b = gift.split(' ')
        a = idx_dict[a] # 선물을 준 친구의 인덱스 번호
        b = idx_dict[b] # 선물을 받은 친구의 인덱스 번호

        gift_map[a][b] += 1
        gift_score[a] += 1
        gift_score[b] -= 1

    # pprint(gift_map)
    # print(gift_score)

    # i번째 친구가 다음 달 받을 선물의 개수
    for i in range(n):
        for j in range(n):
            if i == j: continue

            # j에게 선물을 더 적게 준 경우, 선물을 받지 않음.
            if gift_map[i][j] < gift_map[j][i]:
                continue
            # j에게 선물을 더 많이 준 경우, 선물을 1개 받음.
            elif gift_map[i][j] > gift_map[j][i]:
                gift_next[i] += 1
            # j에게 선물을 주지 않았거나 같게 준 경우, 선물 지수로 비교.
            elif gift_score[i] > gift_score[j]:
                gift_next[i] += 1

    return max(gift_next)
