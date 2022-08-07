T = int(input())

for test_case in range(1, T + 1):
    string = input()

    # {문자 : base64 값}
    base64 = dict()

    # base64 초기화
    # 대문자
    for i in range(26):
        base64[chr(i + 65)] = i
    # 소문자
    for i in range(26):
        base64[chr(i + 97)] = i + 26
    # 숫자
    for i in range(10):
        base64[chr(i + 48)] = i + 52
    # 기타
    base64['+'] = 62
    base64['/'] = 63


    # 입력 받은 문자열의 base64 값을 이진수로 변환
    base64_to_bit = ''
    for ch in string:
        # 문자와 대응하는 base64의 10진수 값을 
        # 6자리(.zfill) 이진수로. 이때 맨 앞 '0b' 제거 ([2:])
        base64_to_bit += bin(base64[ch])[2:].zfill(6)


    decode = ''
    substring = ''
    for i in range(len(base64_to_bit)):
        substring += base64_to_bit[i]

        # 이진수 문자열을 8자리마다 끊어서
        if (i + 1) % 8 == 0:
            # 이진수를 10진수로 변환한 아스키코드 값을 해당 문자로 바꿈
            ascii = int(substring, base=2)
            decode += chr(ascii)

            substring = ''

    print(f'#{test_case} {decode}')