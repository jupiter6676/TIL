a, b = map(int, input().split())

# 가위 1, 바위 2, 보 3
winner = 'B'

# A 가위, B 보
if a == 1 and b == 3:
    winner = 'A'
# A 바위, B 가위
elif a == 2 and b == 1:
    winner = 'A'
# A 보, B 바위
elif a == 3 and b == 2:
    winner = 'A'

print(winner)