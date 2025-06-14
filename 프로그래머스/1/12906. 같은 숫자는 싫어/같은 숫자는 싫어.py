def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        num = arr[i]
        
        if answer[-1] != num:
            answer.append(num)
    
    return answer