import sys
input = sys.stdin.readline

def solution(clothes): 
    # 1. 종류별 의상의 개수 매핑하여 저장
    c_dict = dict()
    
    for rows in clothes:
        type = rows[1]
        c_dict[type] = c_dict.get(type, 0) + 1
    
    # 2. 종류별 의상의 개수를 곱하여 경우의 수 계산
    answer = 1
    for k, v in c_dict.items():
        # +1 하여 곱하는 이유는, 그 종류의 의상을 입지 않은 경우를 포함하기 위함.
        answer *= (v + 1)
    
    # 3. 적어도 한 종류의 의상을 입어야 하므로, 모든 의상을 입지 않은 1가지 경우를 제거
    return answer - 1