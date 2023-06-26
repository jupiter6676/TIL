import sys
input = sys.stdin.readline

stack = list()
for _ in range(int(input())):
    num = int(input())

    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))