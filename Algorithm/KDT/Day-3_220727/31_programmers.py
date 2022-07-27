# https://school.programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(signs)):
        # absolutes[i]가 양수
        if signs[i] == 1:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer