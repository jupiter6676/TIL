import sys

sys.stdin = open("_암호문1.txt")

# 총 10개의 테스트 케이스
for test_case in range(1, 11):
    # 입력 1. 원본 암호문의 길이
    N = int(input())
    # 입력 2. 원본 암호문
    code = list(input().split())
    # 입력 3. 명령어의 개수
    M = int(input())
    # 입력 4. 명령어
    command = input().split()

    i = 1
    while i < len(command):
        # 현재 i의 바로 전이 'I'이라면,
        # (= 명령어가 새로 시작되면,)
        if command[i - 1] == 'I':
            insert_idx = int(command[i])    # 암호문에 삽입할 위치 갱신
            insert_cnt = int(command[i + 1])    # 암호문에 삽입할 암호의 개수 갱신
            i += 2  # i 뒤 두 칸부터 삽입할 원소가 들어있음.

        # j는 삽입할 암호의 개수만큼 반복
        for j in range(insert_cnt):
            code.insert(insert_idx, command[i]) # i의 위치에 있는 원소를 code[insert_idx]에 삽입
            # i와 insert_idx 한 칸씩 뒤로 밀기
            i += 1
            insert_idx += 1

        # 반복문이 끝난 후,
        # 새로운 명령어가 나타날 때까지
        # (= command[i - 1]이 'I'가 될 때까지)
        # i를 뒤로 밀기
        i += 1

    # 변경된 암호문을 10개까지 출력
    print(f'#{test_case}', end=' ')
    for k in range(10):
        print(code[k], end=' ')
    print()