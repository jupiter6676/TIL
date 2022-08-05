import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for test_case in range(1, T + 1):
    # N은 총 학생, K는 과제 제출한 학생
    N, K = map(int, input().split())
    # 과제를 제출한 학생 입력 (0 ~ N - 1)
    lst = list(map(int, input().split()))

    # 과제한 학생 체크 (1 ~ N)
    check = [0] * (N + 1)

    # 과제한 학생 번호 → check 배열 idx
    for stu in lst:
        check[stu] = 1

    # check 출력
    print(f'#{test_case}', end=' ')
    for i in range(1, N + 1):
        if check[i] == 0:
            print(i, end=' ')
    print()