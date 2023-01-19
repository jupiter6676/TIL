import sys
input = sys.stdin.readline

N = int(input())

flowers = list()
for _ in range(N):
    s_month, s_day, e_month, e_day = map(int, input().split())
    flowers.append([s_month * 100 + s_day, e_month * 100 + e_day])

flowers.sort(key=lambda x: (x[0], -x[1]))

prev_end = 301  # 정원의 마지막 꽃이 지는 날짜
cnt = 0 # 심은 꽃의 개수

# 더이상 확인할 꽃이 없을 때까지
while flowers:
    # 정원의 마지막 꽃이 지는 날짜가 12/1 이상이거나,
    # 현재 확인할 꽃(flowers[0])이 피는 날짜가, 마지막 꽃이 지는 날짜와 이어지지 않는 경우
    # 반복문을 종료
    if prev_end >= 1201 or flowers[0][0] > prev_end:
        break

    # 이전 꽃에 이어서 심을 수 있는 꽃이 여러 개 있는 경우
    # 그 중 가장 늦게 지는 꽃의 지는 날짜를 저장
    tmp_max_end = -1
    for _ in range(len(flowers)):
        if flowers[0][0] <= prev_end:
            if tmp_max_end < flowers[0][1]:
                tmp_max_end = flowers[0][1]

            flowers.remove(flowers[0])  # 확인한 꽃은 리스트에서 제거

        else:
            break
    
    prev_end = tmp_max_end  # 가장 마지막에 지는 꽃의 날짜를 갱신
    cnt += 1    # 심은 꽃 개수 증가

# 꽃을 다 심었는데, 지는 날짜가 12/1 보다 빠르면 0 출력
print(0 if prev_end < 1201 else cnt)

# prev = list()
# tmp = list()
# is_start = False

# for i in range(N):
#     if is_start == False and flowers[i][0] <= 301 < flowers[i][1]:    # 종료일은 포함 X
#         tmp.append(i)
#         prev = flowers[i]
#         is_start = True

#     elif prev[0] < flowers[i][0] <= flowers[i][1]:
#         tmp.append(i)
#         prev = flowers[i]

# print(tmp)