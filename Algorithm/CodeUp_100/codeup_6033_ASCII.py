letter = input()

# ord(): 문자 → 아스키코드
# chr(): 아스키코드 → 문자
next = chr(ord(letter) + 1)

print(next)