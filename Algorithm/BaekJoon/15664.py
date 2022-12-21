def recursion(start):
    if len(seq) == M:
        print(*seq)
        return

    remember = 0
    for i in range(start, N):
        if not visited[i] and remember != nums[i]:
            visited[i] = True
            remember = nums[i]
            seq.append(nums[i])
            recursion(i + 1)

            visited[i] = False
            seq.pop()


'''main'''
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [False] * N   # nums[i] ↔ visited[i]
seq = list()

recursion(0)