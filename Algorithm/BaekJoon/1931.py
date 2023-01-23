N = int(input())
confs = [tuple(map(int, input().split())) for _ in range(N)]

# 종료 시간이 빠른 순서
# 그 후 시작 시간도 빠른 순서
confs.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = confs[0][1]    # 회의 종료 시간

for i in range(1, N):
    # 다음 회의 시작 시간이, 이전 회의 종료 시간보다 늦으면
    if confs[i][0] >= end:
        cnt += 1
        end = confs[i][1]

print(cnt)


'''시간초과
tmp_list = list()
res = 0

for i in range(N):
    if not tmp_list:
        tmp_list.append(confs[i])

    for j in range(i + 1, N):
        if tmp_list[-1][1] <= confs[j][0]:
            tmp_list.append(confs[j])

    res = max(res, len(tmp_list))
    print(tmp_list)
    tmp_list = list()   # 초기화

print(res)
'''