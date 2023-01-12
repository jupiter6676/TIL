# heapq (우선순위 큐)를 쓰면 더 빠름

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort()

for _ in range(M):
    tmp = cards[0] + cards[1]
    cards[0] = tmp
    cards[1] = tmp

    cards.sort()

print(sum(cards))