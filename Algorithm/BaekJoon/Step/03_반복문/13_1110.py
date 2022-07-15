num = input()   # str

# 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만듦
if len(num) == 1:
    num = '0' + num

# 변수 초기화
cnt = 0
digit_10 = int(num[0])  # 10의 자리 수
digit_1 = int(num[1])   # 1의 자리 수

while True:
    # 새로운 수
    new_num = digit_1 * 10 + (digit_1 + digit_10) % 10

    # 새로운 수의 1, 10의 자리 수
    digit_10 = new_num // 10  # 10의 자리 수
    digit_1 = new_num % 10    # 1의 자리 수

    cnt += 1

    # 새로운 수가 원래의 수와 같아지면 종료
    if new_num == int(num):
        break

print(cnt)