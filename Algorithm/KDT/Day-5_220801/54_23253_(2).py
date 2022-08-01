import sys
input = sys.stdin.readline

N, M = map(int, input().split())
flag = True

# 총 M개의, 각 더미의 정보
for _ in range(M):
    m = int(input())    # 한 더미의 책 권수

    # m권의 책 번호 ki 입력
    k = list(map(int, input().split()))

    for i in range(m - 1):
        # 내림차순이 아니면 책을 순서대로 뺄 수 X
        if k[i] < k[i + 1]:
            flag = False
            break

    if flag == False:
        break

if flag:
    print('Yes')
else:
    print('No')