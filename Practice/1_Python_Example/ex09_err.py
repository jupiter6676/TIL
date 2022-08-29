# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
'''
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
'''
# 오류 1: fruit_count = {fruit: 1}
# 오류 2: else
# 1은 key-value 값 생성 방법이 잘못되었다.
# 2는 카운트 증가시키는 구문이 else문 안쪽에 있기 때문에
# 1번 오류를 고친다 하더라도, 과일 수는 0개로 나올 것이다.

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = dict()

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 0
    
    fruit_count[fruit] += 1

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

pprint(fruit_count)