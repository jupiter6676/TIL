while True:
    try:
        a, b = map(int, input().split())
        print(a + b)

    # EOFError, ValueError(엔터만 쳤을 때)시 반복문 종료
    except:
        break