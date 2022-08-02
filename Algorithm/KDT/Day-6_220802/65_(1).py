# [Programmers] 숫자 문자열과 영단어

def solution(s):
    answer = ''

    nums = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    word = ''   # 영단어

    for ch in s:
        if ch in '0123456789':
            answer += ch
            continue
        else:
            word += ch

            # 영단어가 딕셔너리에 있으면
            if nums.get(word):
                answer += nums[word]
                word = ''   # 영단어 초기화

    return int(answer)

s = 'zerozero'
print(solution(s))