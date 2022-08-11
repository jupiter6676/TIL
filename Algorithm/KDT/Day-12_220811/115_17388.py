S, K, H = map(int, input().split())

if S + K + H >= 100:
    print('OK')
else:
    min_ = min(S, K, H)

    if min_ == S:
        print('Soongsil')
    elif min_ == K:
        print('Korea')
    else:
        print('Hanyang')