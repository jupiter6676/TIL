# n = input()

# n = int(n)
# i = int(n)

# nums = [False] * 10   # 0 ~ 9
# check = 0
# mult = 2
# res = 0

# while True:
#     # 0 ~ 9까지 다 들어갔으면 반복문 종료
#     if check == 10:
#         break

#     # 몫, 나머지 구하기
#     remainder = i % 10

#     # 0 ~ 9를 체크
#     if nums[remainder] == False:
#         nums[remainder] = True
#         check += 1

#     # 만약 수를 다 못 셌는데, i가 0이 될 경우,
#     # n을 2배, 3배...
#     if check != 10 and i == 0:
#         i = n * mult
#         res = int(i)    # i는 바뀌지만, res는 바뀌지 않음.
        
#         mult += 1   # 곱해주는 수 증가

#         continue    # 그리고 위로 다시 올라가기

#     # 자릿수 낮추면서 반복문 다시 돌기
#     i //= 10

# print(res)

T = int(input())

for test_case in range(1, T + 1):
    nums = [0] * 10
    check = 0
    mult = 1

    n = input()

    while True:
        # 0 ~ 9까지 다 들어갔으면 반복문 종료
        if check == 10:
            break
        else:
            i = str(int(n) * mult)  # n * 2, n * 3..

            for num in i:
                if nums[int(num)] == False:
                    nums[int(num)] = True
                    check += 1

        mult += 1

    print(f'#{test_case} {i}')