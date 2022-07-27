# x가 생성자를 가지는지 검사하는 함수
# 기존의 생성자를 구하는 함수를 개선한 것
# 2231번 문제 참고
def has_constructor(x):
    # 분해합은 생성자와 각 자릿수를 모두 더한 숫자
    # 만약 x가 3자리 수라면,
    # 각 자릿수의 합은 가장 커봐야 9 + 9 + 9 = 27
    # 즉, 생성자는 x - 27보다 항상 크거나 같다.
    # 단, 이때 (x - 27 > 0) 이어야 함.
    # 만약 아니라면 그냥 1부터 검사
    min_start = 1

    if x - 9 * len(str(x)) > 0:
        min_start = x - 9 * len(str(x))
    

    for i in range(min_start, x):
        digitsum = i + sum(list(map(int, str(i))))

        if digitsum == x:
            return True

    return False

for i in range(1, 10001):
    # 생성자를 가지지 않는 숫자
    # 즉, self-number만 출력
    if not has_constructor(i):
        print(i)