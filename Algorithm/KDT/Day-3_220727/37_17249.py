taebo = input() # @===@==@=@==(^0^)==@=@===@

# 얼굴 기준으로 왼손 오른손 나누기
left_hand, right_hand = taebo.split('(^0^)')

cnt_left = 0
cnt_right = 0

if left_hand:
    for i in left_hand:
        if i == '@':
            cnt_left += 1

if right_hand:
    for i in right_hand:
        if i == '@':
            cnt_right += 1

print(cnt_left, cnt_right)