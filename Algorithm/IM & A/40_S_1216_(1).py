# import sys
# sys.stdin = open('input.txt', 'r')

# 시계방향으로 90도 회전
def rotate(matrix):
    rotated = [[0] * 100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            rotated[i][j] = matrix[100 - j - 1][i]

    return rotated


'''main'''
for _ in range(1, 11):
    t = int(input())

    graph = [list(input()) for _ in range(100)]
    max_len = 0

    is_found = False

    # N은 회문의 길이
    for N in range(100, 0, -1):
        # 회문을 찾으면 반복문 종료
        if is_found:
            break

        # 1. 가로
        for i in range(100):
            # 회문을 찾으면 반복문 종료
            if is_found:
                break

            for j in range(100 - (N - 1)):
                # 회문의 길이(N)만큼 회문 만들기
                str_ = ''.join(graph[i][j : j + N])

                if str_ == str_[::-1]:
                    print(str_)
                    max_len = max(max_len, N)
                    is_found = True
                    break
    
    # 2. 세로
    rotated_graph = rotate(graph)
    is_found = False

    for N in range(100, 0, -1):
        if is_found:
            break

        for i in range(100):
            if is_found:
                break

            for j in range(100 - (N - 1)):
                # 회문의 길이(N)만큼 회문 만들기
                # 반복문은 너무 느리기 때문에 아예 행렬을 회전
                str_ = ''.join(rotated_graph[i][j : j + N])

                if str_ == str_[::-1]:
                    # print(str_)
                    max_len = max(max_len, N)
                    is_found = True
                    break

    print(f'#{t} {max_len}')