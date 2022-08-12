import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    total_cards = list(input().split())

    # N이 홀수이면 먼저 놓는 쪽에 한 장이 더 들어가게
    middle = N // 2 if N % 2 == 0 else N // 2 + 1
    cards_1 = total_cards[:middle]
    cards_2 = total_cards[middle:]

    res = list()

    for i in range(len(cards_2)):
        res.append(cards_1[i])
        res.append(cards_2[i])

    if len(cards_1) > len(cards_2):
        res.append(cards_1[len(cards_1) - 1])

    print(f'#{tc}', end=' ')
    print(*res)