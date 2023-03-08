N, K = map(int, input().split())
nums = [0] * (N + 1)

cnt = 1
flag = False
for i in range(2, N + 1):
    if flag:
        break

    if nums[i] == 0:
        j = 1
        while True:
            if i * j > N:
                break

            if not nums[i * j]:
                if cnt == K + 1:
                    flag = True
                    break

                nums[i * j] = cnt
                cnt += 1
                
            j += 1

print(nums)
for i in range(N + 1):
    if nums[i] == K:
        print(i)
        break