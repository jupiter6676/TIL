import sys
input = sys.stdin.readline

# 1. s² 색종이를 붙일 수 있는지 검사
def can_attach(y, x, s):
    for i in range(s):
        for j in range(s):
            if not graph[y + i][x + j]:
                return False    # 범위 내 0 있으면 X
            
    return True

# 2. s² 색종이 붙이기
def attach(y, x, s):
    for i in range(s):
        for j in range(s):
            graph[y + i][x + j] = 0

    papers[s] -= 1

# 4. s² 색종이 떼기
def remove(y, x, s):
    for i in range(s):
        for j in range(s):
            graph[y + i][x + j] = 1

    papers[s] += 1

# 5. 모든 1을 덮었는지 확인
def is_all_filled():
    for i in range(10):
        for j in range(10):
            if graph[i][j]:
                return False
    
    return True

def dfs(cnt):   # 사용한 색종이 개수
    global res

    if cnt >= res:
        return
    
    # 5. 모든 1을 덮었는지 확인
    if is_all_filled():
        res = min(res, cnt)
        return

    for y in range(10):
        for x in range(10):
            if not graph[y][x]:
                continue

            # 색종이 크기마다 재귀 (크기가 큰 순서로)
            for s in range(5, 0, -1):
                # 사용 가능 색종이가 남지 않은 경우
                if not papers[s]:
                    continue
                
                # 범위 체크
                if not (y + s - 1 < 10 and x + s - 1 < 10):
                    continue
                
                # 1. s² 색종이를 붙일 수 있는지 검사
                if not can_attach(y, x, s):
                    continue

                attach(y, x, s) # 2. s² 색종이 붙이기 (graph를 0으로)
                dfs(cnt + 1)    # 3. 색종이 하나 더 붙이기
                remove(y, x, s) # 4. s² 색종이 떼기 (graph를 1로)

            return  # 중복 행 검사를 피함 (어짜피 다음 재귀에서 검사할테니)


'''main'''                
graph = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5] # 각 크기의 색종이의 최대 개수
res = 26

dfs(0)
print(res if res != 26 else -1)