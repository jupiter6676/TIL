# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
'''
numbers = input().split()
print(sum(numbers))
'''
# 문자열은 sum할 수 X

numbers = list(map(int, input().split()))
print(sum(numbers))