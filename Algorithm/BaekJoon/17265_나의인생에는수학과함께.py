import sys
input = sys.stdin.readline

def dfs(y, x):
    global max_res, min_res

    if y == N - 1 and x == N - 1:
        # 스택에서 연산하기
        tmp = int(stack[0])
        for i in range(1, len(stack) - 1):
            if stack[i] == '+':
                tmp += int(stack[i + 1])
            if stack[i] == '-':
                tmp -= int(stack[i + 1])
            if stack[i] == '*':
                tmp *= int(stack[i + 1])

        max_res = max(max_res, tmp)
        min_res = min(min_res, tmp)

        return
    
    for d in range(2):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < N and -1 < nx < N):
            continue
        
        stack.append(graph[ny][nx])
        dfs(ny, nx)
        stack.pop()


'''main'''
N = int(input())
graph = [list(input().split()) for _ in range(N)]

dy = [1, 0]
dx = [0, 1]

max_res = -999999
min_res = 999999

stack = [graph[0][0]]
dfs(0, 0)

print(max_res, min_res)