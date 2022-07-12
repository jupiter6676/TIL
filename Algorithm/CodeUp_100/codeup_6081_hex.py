# 16진수의 문자를 10진수로
hex_ch = int(input(), 16)

# print("%x" %n): 16진수
# %X는 대문자 표기
for i in range(1, 16):
    print("%X*%X=%X" %(hex_ch, i, hex_ch * i))