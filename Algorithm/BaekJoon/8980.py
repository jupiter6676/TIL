N, C = map(int, input().split())    # 마을 수 N, 트럭 용량 C
M = int(input())    # 박스 정보의 개수 M

# 보내는 마을 번호, 받는 마을 번호, 박스 개수
boxes = [list(map(int, input().split())) for _ in range(M)]

# 도착 마을 번호 기준으로 오름차순 정렬
boxes.sort(key=lambda x: (x[1], x[0]))

load = [0] * N  # 각 마을에서 트럭에 박스를 얼마나 적재했는지 기록
total = 0
for i in range(M):
    # 보내는 마을에서 받는 마을로 트럭이 짐을 싣고 가는 중
    # 그 중 가장 큰 수(= 현재 트럭이 싣고 가는 중인 박스 수)를 저장
    max_load = 0
    for j in range(boxes[i][0], boxes[i][1]):
        max_load = max(max_load, load[j])   # 트럭이 싣고 가는 중인 박스의 수

    # 트럭에 더 실을 수 있는 용량 계산
    # 박스를 더 실어도 용량이 남는 경우 boxes[i][2]가 남은 용량이 될 것이고,
    # 용량이 넘을 경우 C - max_load가 남은 용량이 될 것이다.
    left_space = min(boxes[i][2], C - max_load)
    
    total += left_space # 그 용량만큼 적재하므로 total에 더해준다.

    # 보내는 마을에서 받는 마을로 트럭이 짐을 싣고 가는 중
    # 남은 용량만큼 마을에서 실어서 이동하므로,
    # 그 경로에 left_space를 다 더해준다.
    for j in range(boxes[i][0], boxes[i][1]):
        load[j] += left_space

print(total)