N, K = map(int, input().split())
seq = list(map(int, input().split()))  # 전자제품 사용 순서

plugs = [0] * (K + 1)

use = 0
res = 0

for i in range(K):
    # 멀티탭에 자리가 있는 경우, 그냥 꽂기
    if use < N:
        if not plugs[seq[i]]:
            plugs[seq[i]] = 1
            use += 1

    # 멀티탭에 자리가 없는 경우
    else:
        if not plugs[seq[i]]:
            tmp_list = list()
            
            # 앞으로 꽂을 전자제품
            for j in range(i, K):
                # 현재 꽂혀있는 제품들 모두가 앞으로 더 꽂을 예정이라면, 꽂혀있는 제품 중 가장 마지막에 꽂을 제품을 뽑는다.
                # 앞으로 꽂을 전자제품 중, 이미 멀티탭에 꽂혀있는 게 있으면 tmp_list에 그 전자제품 기록
                if plugs[seq[j]] and not seq[j] in tmp_list:
                    tmp_list.append(seq[j])

                # 앞으로 꽂을 전자제품이 N개가 되면 반복 종료
                if len(tmp_list) == N:
                    break
            
            for j in range(K):
                # 1. 만약 현재 꽂혀있는 제품이, 더는 꽂지 않을 제품이라면
                if plugs[seq[j]] and not seq[j] in tmp_list:
                    plugs[seq[j]] = 0   # 그 제품을 뽑기
                    break
            
            # 2. 아니라면, 다시 꽂을 제품 중, 가장 늦게 꽂는 제품을 뽑는다.
            else:
                plugs[tmp_list[-1]] = 0

            # print('---------')
            # print(plugs)

            res += 1    # 제품을 하나 뽑았으므로, 수를 하나 증가시켜 준다.
            plugs[seq[i]] = 1   # 제품을 하나 꽂는다.

    # print(plugs)

print(res)

'''
4 20
1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
답: 4

3 5
1 3 1 2 1
답: 0

2 8
1 2 3 4 3 4 2 2
답: 3

2 15
3 2 1 2 1 2 1 2 1 3 3 3 3 3 3
답: 2

3 5
1 1 1 1 2
답: 0

3 10
7 2 3 9 2 3 7 8 2 7
답: 3

3 14
1 4 3 2 5 4 3 2 5 3 4 2 3 4
답: 4
'''