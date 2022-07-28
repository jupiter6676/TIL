a_card = list(map(int, input().split()))
b_card = list(map(int, input().split()))

a_score = 0
b_score = 0
last_winner = ''   # 동점일 때, 마지막 승자로 승부 가르기

for i in range(10):
    if a_card[i] > b_card[i]:
        a_score += 3
        last_winner = 'A'
    elif a_card[i] < b_card[i]:
        b_score += 3
        last_winner = 'B'
    else:
        a_score += 1
        b_score += 1

print(a_score, b_score)

if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
# A, B 동점일 경우
else:
    # 마지막에 이긴 사람이 승자
    if last_winner == 'A':
        print('A')
    elif last_winner == 'B':
        print('B')
    else:
        print('D')