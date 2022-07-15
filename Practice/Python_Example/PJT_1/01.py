# 01. 텍스트 데이터 입력 (연습)
# 과일 데이터 fruits.txt를 활용하여 총 과일의 갯수를 01.txt에 기록하시오.
# 과일은 하나당 한 줄에 기록되어 있습니다.

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    cnt = 0
    for fruit in f:
        cnt += 1

    print(cnt)