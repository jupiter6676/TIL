# 02. 텍스트 데이터 활용 - 특정 단어 추출
# 과일 데이터 fruits.txt를 활용하여 berry로 '끝나는' 과일의 갯수와 목록을 02.txt에 기록하시오.

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    fruit_dict = dict()
    
    for fruit in f:
        fruit = fruit.strip()
        fruit_dict[fruit] = fruit_dict.get(fruit, 0) + 1

    for k, v in fruit_dict.items():
        print(k, v)