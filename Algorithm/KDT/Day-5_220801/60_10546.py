import sys
input = sys.stdin.readline

N = int(input())    # 참가자의 수

p = dict()  # 참가자

# N명의 참가자 입력
for _ in range(N):
    name = input()
    p[name] = p.get(name, 0) + 1

# N - 1명의 완주자 입력
for _ in range(N - 1):
    name = input()
    p[name] -= 1

    if p[name] == 0:
        del p[name] # 완주했으면 이름 지우기

# 완주 안 한(= 딕셔너리에 남아 있는)
# 사람의 이름(= key) 출력
print(list(p.keys())[0])