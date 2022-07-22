# 문자열 word의 길이를 출력하는 코드를 
# 1) while문 2) for문(문자열 그대로) 3) for문(index)으로 각각 작성하시오.
# len() 함수 사용 금지

word = 'happy!'

# 1) ?
cnt = 0

try:
    while word[cnt]:
        cnt += 1
except IndexError:
    print(cnt)

# 2)
cnt = 0

for j in word:
    cnt += 1
print(cnt)

# 3)
cnt = 0

while word[cnt:]:
    cnt += 1
print(cnt)