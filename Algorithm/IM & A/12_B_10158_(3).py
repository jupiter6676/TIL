'''하나만 맞힌 코드...'''
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

NE = 1  # 오른쪽 위 45도 방향
SW = 0  # 왼쪽 아래 45도 방향

# 개미가 꼭짓점에서 부딪히는 경우
# 같은 선분 위에서 계속 이동하게 된다.
if w - p == h - q:
    m = w - p

    # 우선 개미를 오른쪽 위 꼭짓점에 이동시킨다.
    p += m
    q += m
    t -= m

    # 한 선분을 몇 번 왕복하는지 구하기 위해
    # 최대 선분의 길이를 구한다.
    n = w if w < h else h

    dir_ = NE if (t // n) % 2 else SW

    tmp = t % n
    if dir_ == NE:
        p = p - n + tmp
        q = q - n + tmp
    else:
        p -= tmp
        q -= tmp

# 모르겠다...
else:
    pass

        
print(p, q)

'''
6 4
5 3
6
답: 3 1
'''