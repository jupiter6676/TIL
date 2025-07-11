import itertools

def solution(cards):
    max_w = 0
    max_h = 0
    
    # 각 명함을 순회
    for card in cards:
        # 명함 중 더 긴 쪽을 가로, 더 짧은 쪽을 세로로 설정
        w = max(card[0], card[1])
        h = min(card[0], card[1])
        
        # 가장 긴 가로, 세로 길이 구하기
        max_w = max(max_w, w)
        max_h = max(max_h, h)
        
    answer = max_w * max_h
    
    return answer
