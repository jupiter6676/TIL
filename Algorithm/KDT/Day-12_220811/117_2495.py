for _ in range(3):
    num = input()
    # 0 ~ 9까지 연속된 수의 길이를 저장할 변수
    len_list = [1] * 10
    cnt = 1
    max_ = 1

    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            cnt += 1
        else:
            cnt = 1
            max_ = 1
        
        if cnt > max_:
            len_list[int(num[i])] = cnt

    print(max(len_list))