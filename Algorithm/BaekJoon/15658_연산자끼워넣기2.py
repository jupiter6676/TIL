import sys
input = sys.stdin.readline

def dfs(start):
    global max_, min_

    if len(seq) == N - 1:
        sum = nums[0]
        for i in range(1, N):
            if seq[i - 1] == 0:
                sum += nums[i]
            elif seq[i - 1] == 1:
                sum -= nums[i]
            elif seq[i - 1] == 2:
                sum *= nums[i]
            else:
                # sum //= nums[i]
                if sum * nums[i] < 0:
                    sum = abs(sum) // abs(nums[i]) * -1
                else:
                    sum //= nums[i]

        max_ = max(max_, sum)
        min_ = min(min_, sum)
        return

    for i in range(start, 4):
        if opers[i]:
            opers[i] -= 1
            seq.append(i)

            dfs(start)
            opers[i] += 1
            seq.pop()
        
            
'''main'''
N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split())) # +-*/

max_ = int(-1e10)
min_ = int(1e10)

seq = list()
dfs(0)
print(max_)
print(min_)