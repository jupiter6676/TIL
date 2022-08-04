M = int(input())
cups = [0, 1, 0, 0] # 0번 인덱스 사용 X

for _ in range(M):
    x, y = map(int, input().split())
    
    # 둘 중 하나에 공이 있으면,
    # 공을 없는 컵에 옮기기 (= Swap)
    if cups[x] == 1 or cups[y] == 1:
        cups[x], cups[y] = cups[y], cups[x]
        
for i in range(len(cups)):
    if cups[i] == 1:
        print(i)
        break