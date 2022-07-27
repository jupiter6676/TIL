max_score = 0
winner = 0

for i in range(1, 6):
    scores = list(map(int, input().split()))
    total = sum(scores)

    if total > max_score:
        max_score = total
        winner = i

print(winner, max_score)