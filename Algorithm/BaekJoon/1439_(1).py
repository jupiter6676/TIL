S = input()

cnt_0 = 0
cnt_1 = 0

is_continued_0 = False   # 0이 연속되었는지
is_continued_1 = False   # 1이 연속되었는지

for c in S:
    if c == '0':
        is_continued_0 = True

        if is_continued_1:
            cnt_1 += 1
            is_continued_1 = False

        is_continued_1 = False
    
    else:
        is_continued_1 = True

        if is_continued_0:
            cnt_0 += 1
            is_continued_0 = False

if is_continued_1:
    cnt_1 += 1

if is_continued_0:
    cnt_0 += 1

print(min(cnt_0, cnt_1))