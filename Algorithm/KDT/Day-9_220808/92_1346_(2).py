N = int(input())

num = 0
cnt = 0

# N번째 숫자를 찾을 때까지
while cnt != N:
    # 숫자를 1씩 계속 증가
    num += 1

    # tmp로 숫자를 10씩 나눠가며, 666이 있는지 검사
    tmp = num
    while tmp != 0:
        # 1000으로 나눈 나머지가 666이면 cnt +1
        if tmp % 1000 == 666:
            cnt += 1
            break
        else:
            tmp //= 10

print(num)