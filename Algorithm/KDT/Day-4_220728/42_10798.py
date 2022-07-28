'''
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''

arr2D = list()
max_len = 0 # 가장 긴 문자열의 길이

for i in range(5):
    s = input()
    arr2D.append(list(s))

    if max_len < len(s):
        max_len = len(s)

# 행(세로) 탐색 → j는 가로로 움직임
for j in range(max_len):
    # 총 5개의 문자열 → i는 세로로 움직임
    for i in range(5):
        # 만약 i번째 문자열의 길이보다
        # j가 더 많이 움직였을 경우
        # 해당 문자열을 건너뛰고 다음 문자열로 이동 → continue
        if j >= len(arr2D[i]):
            continue

        print(arr2D[i][j], end='')
        
    #print()