# 3888ms??

cnt = 0
dic = dict()

N = int(input())

for _ in range(N):
    s = input()

    # 새로 들어온 사람 → 새로 딕셔너리 생성
    if s == 'ENTER':
        dic = dict()
    
    else:
        # 딕셔너리에 없는 사람이면
        if dic.get(s, 0) == 0:
            cnt += 1    # 곰곰티콘 +1
            # 해당 이름을 key로 가지는 value에 +1
            dic[s] = dic.get(s, 0) + 1

print(cnt)