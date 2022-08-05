import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for test_case in range(1, T + 1):
    # N은 총 학생, K는 등급 알고 싶은 학생
    N, K = map(int, input().split())
    # N * 3의 리스트
    scores = [list(map(int, input().split())) for _ in range(N)]
    
    x = N // 10 # N은 10의 x배수
    grade = ['A+'] * x + ['A0'] * x + ['A-'] * x + ['B+'] * x + ['B0'] * x + ['B-'] * x + ['C+'] * x + ['C0'] * x + ['C-'] * x + ['D0'] * x

    # 학생 별 총점
    total = list()

    for i in range(N):
        tmp = scores[i][0] * 0.35 + scores[i][1] * 0.45 + scores[i][2] * 0.2
        total.append((i + 1, tmp))  # (학생 번호, 총점)

    total = sorted(total, key=lambda x: x[1], reverse=True)

    # K번째 학생이 
    # 정렬 후 리스트의 어느 idx에 위치해 있는지 찾기
    for i in range(N):
        # 학생 번호와 K를 비교
        if total[i][0] == K:
            K = i   # 해당 idx 반환
            break
    
    # 해당 등수에 맞는 등급 출력
    print(f'#{test_case} {grade[K]}')