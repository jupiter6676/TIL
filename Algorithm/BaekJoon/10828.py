import sys
input = sys.stdin.readline

N = int(input())
stack = list()

for _ in range(N):
    line = input().split()

    command = line[0]
    if len(line) == 2:
        num = line[1]

    if command == 'push':
        stack.append(num)
    elif command == 'pop':
        print(stack.pop() if stack else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1 if not stack else 0)
    else:   # top
        print(stack[-1] if stack else -1)