N = int(input())
num_cnt = dict()

for i in range(N):
    num = int(input())
    num_cnt[num] = num_cnt.get(num, 0) + 1

# 위 딕셔너리의 아이템을 value 값을 기준으로 내림차순 정렬한 후,
# key 값으로 오름차순 정렬
sorted_lst = sorted(num_cnt.items(), key=lambda x: (-x[1], x[0]))
print(sorted_lst[0][0])

'''
# 시간 초과

# 위 딕셔너리의 아이템을 value 값을 기준으로 내림차순 정렬
sorted_lst = sorted(num_cnt.items(), key=lambda x: x[1], reverse=True)

max_num = sorted_lst[0][0]  # 제일 첫 번째 원소의 key가 정답
max_cnt = sorted_lst[0][1]
for i in range(1, len(sorted_lst)):
    # 최댓값이 단 하나라면 바로 종료
    if sorted_lst[i][1] < max_cnt:
        break

    # 최대로 카운트 된 게 여러 개
    # 근데 수가 더 작으면 그걸로 갱신
    elif sorted_lst[i][1] == max_cnt and sorted_lst[i][0] < max_num:
        max_num = sorted_lst[i][0]
        break

print(max_num)
'''