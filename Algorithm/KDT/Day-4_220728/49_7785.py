N = int(input())

dic = dict()
for _ in range(N):
    name, log = input().split()

    if log == 'enter':
        dic[name] = dic.get(name, 1)
    
    if log == 'leave':
        dic.pop(name)

# 회사에 남은 사람들 명단
# 이름을 사전의 역순으로 출력 (-x[0]이 안 되네)
res = sorted(dic.items(), key=lambda x: x[0], reverse=True)

for tuple in res:
    print(tuple[0])