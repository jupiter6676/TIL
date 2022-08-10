N = int(input())

dic = dict()

for _ in range(N):
    cow, d = map(int, input().split())

    # key: 소 번호, value: (왼/오, 길 건넌 횟수)
    dic[cow] = dic.get(cow, [d, 0])
    
    # 입력 받은 방향 d와, 기존에 저장된 방향이 다른 경우
    # 길을 한 번 건넌 것 → +1
    # 방향도 갱신
    if dic[cow][0] != d:
        dic[cow][1] += 1
        dic[cow][0] = d

sum_ = 0
for v in dic.values():
    if v[1] != 0:
        sum_ += v[1]

print(sum_)