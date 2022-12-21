def recursion():
    if len(seq) == M:
        print(*seq)
        return

    remember = 0
    for i in range(N):
        if remember != nums[i]:
            remember = nums[i]
            seq.append(nums[i])
            recursion()

            seq.pop()


'''main'''
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

seq = list()

recursion()