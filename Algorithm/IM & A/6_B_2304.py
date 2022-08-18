N = int(input())
pillar = [0] * 1001 # idx: 기둥 위치, val: 기둥 높이

first = 999999  # 첫 기둥이 있는 위치
last = 0        # 마지막 기둥이 있는 위치
max_height = 0  # 기둥의 최고 높이

for _ in range(N):
    L, H = map(int, input().split())
    pillar[L] = H

    if L > last:
        last = L
    if L < first:
        first = L
    
    if H > max_height:
        max_height = H


stack = list()

# 스택에 처음 시작하는 곳의 높이를 담는다.
stack.append(pillar[first])

is_asc = True
# 시작한 곳의 한 칸 뒤부터 마지막까지 반복
for i in range(first + 1, last + 1):
    if is_asc:
        # 현재까지 저장한 가장 최근의 높이 stack[-1]
        # 보다 현재의 높이가 더 크면, 스택에 새로운 높이를 쌓기
        if stack[-1] < pillar[i]:
            stack.append(pillar[i])

        # 그렇지 않으면 가장 최근의 높이만 계속 쌓기
        else:
            stack.append(stack[-1])

        # 최고 높이에 닿았으면 이 반복을 종료
        if pillar[i] == max_height:
            is_asc = False
            break

# i != last를 추가한 이유는
# 내리막이 없으면 이 반복문을 돌 필요가 없기 때문이다.
# 내리막이 존재하면 이 반복문을 도는 것.

# 맨 마지막에서부터 오르막이면 스택에 추가 (앞 부분 로직과 동일)
# 최고 높이가 2개여도 else문 때문에, 스택에 올바르게 쌓인다.
if not is_asc and i != last:
    # 맨 끝 (가장 낮은 곳)의 높이 추가
    stack.append(pillar[last])

    # 맨 끝 한 칸 앞에서부터 시작,
    # 중단된 부분(최고점)의 한 칸 뒤까지 반복
    for j in range(last - 1, i, -1):
        if stack[-1] < pillar[j]:
            stack.append(pillar[j])

        else:
            stack.append(stack[-1])

# 면적을 구한다.
print(sum(stack))


'''
4
1 6
3 6
5 6
7 7
답: 43 (난 50)

3
0 3
1 2
2 3
답: 9 (난 12)
'''