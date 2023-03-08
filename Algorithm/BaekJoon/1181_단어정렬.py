import sys
input = sys.stdin.readline

N = int(input())
dic = dict()

for _ in range(N):
    dic[input().rstrip()] = 1

dic = sorted(dic.keys(), key=lambda x: (len(x), x))

for k in dic:
    print(k)