import sys
input = sys.stdin.readline

N = int(input())

lst = list()
dic = dict()

for _ in range(N):
    num = int(input())
    lst.append(num)
    dic[num] = dic.get(num, 0) + 1

lst.sort()
dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

mean = round(sum(lst) / N)
median = lst[N // 2]
range_ = lst[N - 1] - lst[0]

if N > 1:
    mode = dic[1][0] if dic[0][1] == dic[1][1] else dic[0][0]
else:
    mode = dic[0][0]

print(mean)     # 산술평균 (첫째자리 반 올림)
print(median)   # 중앙값
print(mode)     # 최빈값 (여러 개는 두 번째로 작은 값)
print(range_)   # 범위 (최댓값과 최솟값의 차)