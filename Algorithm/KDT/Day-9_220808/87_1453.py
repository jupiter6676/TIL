N = int(input())
order = list(map(int, input().split()))

seat = dict()
cnt = 0

for num in order:
    # 자리가 공석이면, 자리 채워주기
    seat[num] = seat.get(num, 0) + 1
    
    # 거절당한 사람 카운트
    if seat[num] > 1:
        cnt += 1

print(cnt)