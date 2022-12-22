# 연산자 우선 순위를 무시하고 앞에서부터 진행
# 나눗셈은 정수 나눗셈으로 몫만 취함
# 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꿈
def func():
    global max_
    global min_

    if len(tmp_list) == N - 1:  # N - 1 → 연산자 개수
        # print(*tmp_list)
        dp = list()
        for num in nums:
            dp.append(num)

        for i in range(N - 1):
            if tmp_list[i] == '+':
                dp[i + 1] = dp[i] + dp[i + 1]
            elif tmp_list[i] == '-':
                dp[i + 1] = dp[i] - dp[i + 1]
            elif tmp_list[i] == '*':
                dp[i + 1] = dp[i] * dp[i + 1]
            else:
                if dp[i] < 0:
                    dp[i + 1] = -(abs(dp[i]) // dp[i + 1])
                else:
                    dp[i + 1] = dp[i] // dp[i + 1]
        
        max_ = max(max_, dp[-1])    # dp의 마지막 원소는 사칙연산 결과
        min_ = min(min_, dp[-1])

        return

    # opers로 만들 수 있는 조합으로 tmp_list 구성
    for i in range(4):
        # 추가할 연산자가 1개 이상
        if opers[i] > 0:
            if i == 0:
                tmp_list.append('+')
            elif i == 1:
                tmp_list.append('-')
            elif i == 2:
                tmp_list.append('*')
            else:
                tmp_list.append('/')

            opers[i] -= 1
            func()

            opers[i] += 1
            tmp_list.pop()


'''main'''
N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split())) # +, -, ×, ÷

tmp_list = list()   # opers로 만들 수 있는 조합
max_ = -1000000000  # 결과는 -10억보다 항상 큼
min_ = 1000000000   # 결과는 10억보다 항상 작음

func()
print(max_)
print(min_)