def solution(new_id):
    answer = ''
    
    # 1. 대문자 → 소문자
    new_id = new_id.lower()
    
    # 2. 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
    for ch in new_id:
        if 97 <= ord(ch) <= 122:
            answer += ch
        
        elif 48 <= ord(ch) <= 57:
            answer += ch
            
        elif ch in '-_.':
            answer += ch
            
    # 3. .가 2번 이상 연속 → 하나의 마침표(.)
    tmp_lst = ''
    is_prev = False
    
    for i in range(len(answer)):    
        if answer[i] == '.':
            if not is_prev:
                tmp_lst += answer[i]
            is_prev = True
            
        else:
            tmp_lst += answer[i]
            is_prev = False
    
    answer = tmp_lst
            
    # 4. 마침표(.)가 처음이나 끝에 위치하면 제거
    answer = answer.strip('.')
    
    # 5. id가 빈 문자열이면, new_id에 "a"를 대입
    if not answer:
        answer = 'a'
    
    # 6. id의 길이가 16자 이상이면, 15자까지만 저장 (끝에 .있으면 제거)
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
    
    # 7. id의 길이가 2자 이하라면, 마지막 문자를 id 길이가 3이 될 때까지 반복해서 붙이기
    if len(answer) <= 2:
        for i in range(3 - len(answer)):
            answer += answer[-1]
    
    return answer