import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

res = 0
for i in range(1, W - 1):
    # i번째 블록을 기준으로, 가장 높은 왼쪽과 오른쪽 벽
    left_max = max(blocks[:i])
    right_max = max(blocks[i + 1:])

    if blocks[i] < left_max and blocks[i] < right_max:
        res += min(left_max, right_max) - blocks[i]

print(res)

# last = blocks[0]    # 왼쪽 벽
# stack = list()
# for i in range(1, W):
#     # 왼쪽 벽보다 낮은 벽
#     if last > blocks[i]:
#         if i != W - 1:
#             stack.append(blocks[i])
#         else:
#             res += blocks[i] * len(stack) - sum(stack)

#     # 왼쪽 벽보다 높거나 같은 벽
#     else:
#         res += last * len(stack) - sum(stack)
#         stack = list()
#         last = blocks[i]

# print(res)

'''
4 8
0 1 0 1 4 1 2 1
답: 2
'''