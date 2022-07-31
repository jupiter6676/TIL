T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))

    average = round(sum(lst)/len(lst))

    print(f'#{test_case} {average}')