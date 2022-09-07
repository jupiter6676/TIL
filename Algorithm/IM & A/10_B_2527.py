for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 첫 번째 사각형의 왼쪽 아래 꼭짓점 좌표가
    # 두 번째 사각형의 왼쪽 아래 꼭짓점 좌표보다
    # 항상 왼쪽에 위치하도록
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        p1, p2 = p2, p1
        q1, q2 = q2, q1

    # 1. 공통부분 없음 1
    if p1 < x2 or q1 < y2 or y1 > q2:
        print('d')

    # 2. 공통부분 없음 2 - 1 1 3 3 3 4 7 9
    elif p1 == x2 and (q1 < y2 or y1 > q2):
        print('d')

    # 3. 공통부분 없음 3
    elif (q1 == y2 or y1 == q2) and p1 < x2:
        print('d')

    # 4. 점 - 2 2 3 3 1 1 2 2
    elif p1 == x2 and (q1 == y2 or y1 == q2):
        print('c')

    # 5. 선분
    elif p1 == x2 or q1 == y2 or y1 == q2:
        print('b')

    # 6. 직사각형
    else:
        print('a')