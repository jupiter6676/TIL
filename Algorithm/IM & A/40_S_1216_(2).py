import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    t = int(input())

    graph = [list(input()) for _ in range(100)]
    t_graph = [[0] * 100 for _ in range(100)] # graph 전치
    
    for i in range(100):
        for j in range(100):
            t_graph[i][j] = graph[j][i]

    max_len = 0
    is_found = False

    # N은 회문의 길이 (100부터 1까지)
    for N in range(100, 0, -1):
        # 회문을 찾으면 반복문 종료
        if is_found:
            break

        # 1. 가로
        for row in graph:
            # 회문을 찾으면 반복문 종료
            if is_found:
                break

            for j in range(100 - (N - 1)):
                # 회문의 길이(N)만큼 회문 만들기
                str_ = row[j : j + N]

                if str_ == str_[::-1]:
                    # print(str_)
                    max_len = max(max_len, N)
                    is_found = True
                    break
    
    # 2. 세로
    is_found = False
    
    for N in range(100, 0, -1):
        if is_found:
            break

        for row in t_graph:
            if is_found:
                break

            for j in range(100 - (N - 1)):
                # 회문의 길이(N)만큼 회문 만들기
                # 반복문은 너무 느리기 때문에 전치 행렬을 활용
                # join도 너무 느리다.. 그냥 하면 될 걸
                str_ = row[j : j + N]

                if str_ == str_[::-1]:
                    # print(str_)
                    max_len = max(max_len, N)
                    is_found = True
                    break

    print(f'#{t} {max_len}')