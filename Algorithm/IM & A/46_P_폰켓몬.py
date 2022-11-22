def solution(nums):
    N = len(nums)  # 총 포켓몬 수
    M = len(set(nums))  # 중복 제거 포켓몬 수
    
    answer = M if M < N // 2 else N // 2
    
    return answer