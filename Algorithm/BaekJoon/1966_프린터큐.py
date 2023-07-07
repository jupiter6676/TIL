import sys
from collections import deque
input = sys.stdin.readline

def eval_max():
    max_ = 0
    for i in range(len(q)):
        if max_ < q[i][0]:
            max_ = q[i][0]

    return max_


for _ in range(int(input())):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    q = deque() # 인쇄할 문서
    
    max_ = 0    # 현재 가장 중요도가 높은 문서
    for i in range(N):
        q.append([docs[i], i])  # 문서의 중요도와 초기 순서 저장
        max_ = max(max_, docs[i])

    cnt = 1
    while q:
        doc = q.popleft()
        
        if doc[0] == max_:
            if doc[1] == M:
                break
            else:
                cnt += 1
                max_ = eval_max()

        else:
            q.append(doc)

    print(cnt)

'''
1
4 2
1 2 3 4
답: 2
'''