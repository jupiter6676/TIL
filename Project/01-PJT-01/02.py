# 02. 텍스트 데이터 활용 - 특정 단어 추출
# 과일 데이터 fruits.txt를 활용하여 berry로 '끝나는' 과일의 갯수와 목록을 02.txt에 기록하시오.

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    berry_lst = list()
    berry_lst2 = list()

    for fruit in f:
        # 마지막 5글자 
        fruit = fruit.strip()   # 맨 뒤 개행 제거
        last_5_letters = ''.join(fruit[-5:])
        
        if last_5_letters == 'berry':
            berry_lst.append(fruit.strip())

    berry_lst2 = list(set(berry_lst))   # 중복 제거
    
    print(len(berry_lst2))
    for berry in berry_lst2:
        print(berry)