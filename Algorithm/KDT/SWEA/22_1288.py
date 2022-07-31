T = int(input())

for test_case in range(1, T + 1):
    nums = [0] * 10
    check = 0
    mult = 1

    n = input()

    while True:
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