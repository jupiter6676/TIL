# 00. 텍스트 데이터 출력 (연습)
# 아래의 내용을 00.txt에 기록하시오

with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('3회차 최보영\n')
    f.write('Hello, Python!\n')

    for i in range(5):
        f.write(f'{i + 1}일차 파이썬 공부 중\n')