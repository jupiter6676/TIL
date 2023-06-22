# 1. 데이터 구조 (Data Structure)

- 함수 (Function)

  - Decomposition, Abstraction

  - 사용자 정의 함수, 내장 함수, 외부 함수



- 타입.**메서드()**

  ```python
  input().split()		# 문자열.split()
  [1, 2, 3].append()	# 리스트.append()
  ```



- `.sort()` 메서드

  ```python
  a = [10, 1, 100]
  a.sort()
  print(a)
  ```

  - sort() 메소드는 리스트를 정렬된 상태로 변경 (원본을 변경)
  - 반환되는 것은 None



- `sorted()` 함수

  ```python
  b = [10, 1, 100]
  b2 = sorted(b)
  print(b1, b2)
  ```

  - sorted() 함수는 원본을 변경하지 X
  - 반환되는 것은 정렬된 리스트



# 2. 메서드 (Methods)

## (1) 문자열

| 문법          | 설명                                                         |
| ------------- | ------------------------------------------------------------ |
| `s.find(x)`   | x의 첫 번째 위치를 반환, 없으면 -1을 반환                    |
| `s.index(x)`  | x의 첫 번째 위치를 반환, 없으면 오류 발생                    |
| `s.isalpha()` | 알파벳 문자 여부 <br />단순 알파벳 X, 유니코드 상의 Letter (한국어 포함) |
| `s.isupper()` | 대문자 여부                                                  |
| `s.islower()` | 소문자 여부                                                  |
| `s.istitle()` | 타이틀 형식 여부                                             |

---



1. **문자열 탐색**

   - `.find(x)` : x의 **첫 번째 위치**를 반환, **없으면 -1을 반환**

     ```python
     print('apple'.find('p'))	# 1
     print('apple'.find('k'))	# -1
     ```

   

   - `.index(x)` : x의 **첫 번째 위치**를 반환, **없으면 오류 발생**

     ```python
     print('apple'.find('p'))	# 1
     print('apple'.find('k'))	# ValueError: substring not found
     ```



2. **문자열 검증**❣️❣️❣️❣️❣️❣️❣️

   - `.isalpha()`: 모두 알파벳이면 True

   - `.isupper()` : 모두 대문자이면 True

   - `.islower()` : 모두 소문자이면 True

   - `.istitle()` : 맨 앞글자가 대문자이면 True

   - 문자열이 숫자형인가?
     - `.isdecimal()` ⊆ .isdigit() ⊆ .isnumeric()



---

| 문법                                 | 설명                                       |
| ------------------------------------ | ------------------------------------------ |
| `s.replace(old, new[, count])`       | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 |
| `s.strip([chars])`                   | 공백이나 특정 문자를 제거                  |
| `s.split([sep=None[, maxsplit=-1]])` | 공백이나 특정 문자를 기준으로 분리         |
| `s.capitalize()`                     | 가장 첫 번째 글자를 대문자로 변경          |
| `s.title()`                          | `'`나 공백 이후를 대문자로 변경            |
| `s.upper()`                          | 모두 대문자로 변경                         |
| `s.lower()`                          | 모두 소문자로 변경                         |
| `s.swapcase()`                       | 대 ↔ 소문자 서로 변경                      |

---



3. **문자열 변경**

   >문자열은 스스로 바뀌는 경우 X
   >
   >바뀐 결과를 반환한다.

   - ❣️`.replace(old, new[, count])`

     - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

     - count를 지정하면, 해당 개수 만큼만 시행

       ```python
       print('coone'.replace('o', 'a'))	# caane
       print('wooowo'.replace('o', '!', 2))	# w!!owo
       ```

   

   - ️`.strip([chars])`

     - 특정한 문자들을 지정하면

     - 양쪽을 제거하거나 (strip), 왼쪽을 제거 (lstrip), 오른쪽을 제거 (rstrip)

     - 문자열을 지정하지 않으면 **공백을 제거** → Space, \n

       ```python
       print('    A\n').strip()	# 'A'
       print('    A\n').lstrip()	# 'A\n'
       print('    A\n').rstrip()	# '    A'
       print('A????\n').strip('?')	# 'A'
       ```

   

   - ❣️`.split([sep=None[, maxsplit=-1]])`

     - 문자열을 특정한 단위로 나눠, **리스트로 반환**

     - sep = None이거나 지정되지 않으면

       - 연속된 공백문자를 단일한 공백문자로 간주하고, 공백을 기준으로 문자열을 나누어 준다.
       - 선행/후행 공백은 빈 문자열에 포함시키지 않는다.

     - 분리할 단어의 개수 maxsplit = -1인 경우에는 제한이 없음.

       ```python
       print('a,b,c'.split('_'))	# ['a,b,c']
       print('a b c'.split())	# ['a', 'b', 'c']
       ```

   

   - ❣️`'separator'.join([iterable])`

     - 반복 가능한 컨테이어 요소들을

     - separator(구분자)로 합쳐 문자열 반환

     - Iterable에 문자열이 아닌 값이 있으면, TypeError 발생

       ```python
       print(''.join(['3', '5']))	# 35
       print(','.join(['홍길동', '김철수']))	# 홍길동,김철수
       ```

   

   - 기타 변경
     - `.capitalize()`
     - `.title()`
     - `.upper()`
     - `.lower()`
     - `.swapcase()`



## (2) 리스트

| 문법                     | 설명                                                         |
| ------------------------ | ------------------------------------------------------------ |
| `L.append(x)`            | 리스트 마지막에 항목 x 추가                                  |
| `L.insert(i, x)`         | 리스트 인덱스 i에 항목 x 삽입                                |
| `L.remove(x)`            | 리스트 가장 첫 번째에 있는 항목 x 제거<br />존재하지 않을 경우, ValueError |
| `L.pop()`                | 리스트 마지막 항목을 반환 후 제거                            |
| `L.pop(i)`               | 리스트 인덱스 i에 있는 항목을 반환 후 제거                   |
| `L.extend(m)`            | 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=과 같은 기능)   |
| `L.index(x, start, end)` | 리스트 가장 첫 번째에 있는 항목 x의 인덱스 반환              |
| `L.reverse()`            | 리스트 순서를 뒤집음                                         |
| `L.sort()`               | 리스트 정렬 (매개변수 이용 가능 → reverse)                   |
| `L.count(x)`             | 리스트 중 항목 x의 개수를 반환                               |

---



1. **값 추가 및 삭제**

   > 리스트 원본 자체가 변경됨.

   - ❣️`.append(x)` : 리스트의 마지막에 값 x를 추가

     ```python
     lst = ['a', 'b', 'c']
     lst.append('d')
     print(lst)	# ['a', 'b', 'c', 'd']
     ```

     

   - `.extend(iterable)` : 리스트에 iterable의 항목을 추가

     ```python
     a = ['apple']
     a.extend(['banana', 'mango'])
     print(a)	# ['apple', 'banana', 'mango']
     ```

   

   - `.insert(i, x)` : 정해진 위치 i에 값을 추가

     ```python
     a = ['apple']
     a.insert(0, 'banana')
     print(a)	# ['banana', 'apple']
     # 만약 i가 리스트의 길이보다 큰 경우, 맨 뒤에 추가한다.
     ```

   

   - `.remove(x)` : 리스트에서 값 x를 삭제
   - `.pop(i)`
     - 정해진 위치 i에 있는 값 삭제, 그 항목을 반환
     - i가 지정되지 않으면, 마지막 항목을 삭제하고 반환
   - `.clear()` : 모든 항목을 삭제



2. **탐색 및 정렬**

   - `.index(x)`
     - x값을 찾아 해당 index 값을 반환
     - 없는 경우 ValueError

   - `.count(x)` : 원하는 값의 개수를 반환

     ```python
     nums = [1, 2, 3, 1, 1]
     nums.count(1)	# 3
     ```

   - `.sort()`

     - 원본 리스트를 정렬, None 반환
     - sorted() 함수는 정렬된 리스트를 반환

   - `.reverse()`

     - 순서를 반대로 뒤집음 (정렬 X)
     - None을 반환



## (3) 세트

| 문법              | 설명                                                         |
| ----------------- | ------------------------------------------------------------ |
| `s.copy()`        | 세트의 얕은 복사본 반환                                      |
| `s.add(x)`        | 항목 x가 세트 s에 없다면 추가                                |
| `s.pop()`         | 세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거<br />세트가 비어있을 경우, KeyError |
| `s.remove(s)`     | 항목 x를 세트 s에서 삭제<br />항목이 존재하지 않을 경우, KeyError |
| `s.discard(x)`    | 항목 x가 세트 s에 있는 경우, 항목 x를 세트 s에서 삭제        |
| `s.update(t)`     | 세트 t에 있는 모든 항목 중, 세트 s에 없는 항목을 추가        |
| `s.clear()`       | 모든 항목을 제거                                             |
| `s.isdisjoint(t)` | 세트 s가 세트 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우 True 반환 |
| `s.issubset(t)`   | 세트 s가 세트 t의 하위 세트인 경우, True 반환                |
| `s.issuperset(t)` | 세트 s가 세트 t의 하=상위 세트인 경우, True 반환             |

---



## (4) 딕셔너리

| 문법                 | 설명                                                         |
| -------------------- | ------------------------------------------------------------ |
| `d.clear()`          | 모든 항목 제거                                               |
| `d.keys()`           | 딕셔너리 d의 모든 키를 담은 뷰를 반환                        |
| `d.values()`         | 딕셔너리 d의 모든 값을 담은 뷰를 반환                        |
| `d.items()`          | 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환                |
| `d.get(k)`           | 키 k의 값을 반환<br />키 k가 없을 경우 None을 반환           |
| `d.get(k, v)`        | 키 k의 값을 반환<br />키 k가 없을 경우 v를 반환              |
| `d.pop(k)`           | 키 k의 값을 반환하고, 키 k인 항목을 삭제<br />키 k가 없을 경우 KeyError |
| `d.pop(k, v)`        | 키 k의 값을 반환하고, 키 k인 항목을 삭제<br />키 k가 없을 경우 v를 반환 |
| `d. update([other])` | 딕셔너리 d의 값을 매핑하여 업데이트                          |

---



1. **조회**

   - `.keys()` : Key들을 일종의 리스트 형태로 보여준다.

   - `.values()` : Value들을 일종의 리스트 형태로 보여준다.

   - `.itmes()` : 일종의 리스트 안의 튜플 형태로 보여준다.

     ```python
     dic = {'apple': '사과', 'banana': '바나나'}
     
     print(dic.keys())	# dic_keys(['apple', 'banana'])
     print(dic.values())	# dic_values(['사과', '바나나'])
     print(dic.items())	# dic_items([('apple', '사과'), ('banana', '바나나')])
     
     # 활용
     for k in dic:
         print(k, dic[k])	# apple 사과 ...
     
     for v in dic.values():
         print(v)	# 사과 ...
         
     for k, v in dic.items():
         print(k, v)	# apple 사과 ...
     ```

   

   - `.get(key[, default])`

     - key를 통해 value를 가져옴.

     - KeyError가 발생하지 않음.

     - default 값을 설정할 수 있음. (기본은 None)

       ```python
       dic = {'apple': '사과'}
       
       print(dic['pineapple'])	# Error
       print(dic.get('pineapple'))	# None
       print(dic.get('apple'))		# 사과
       print(dic.get('pineapple', 0))	# 0
       ```



2. **추가 및 삭제**

   - `.pop(key[, default])`

     - key가 딕셔너리에 있으면 제거하고, 해당 값 반환

     - 그렇지 않으면 default를 반환

     - default 값이 없으면 KeyError

       ```python
       dic = {}
       
       # key-value 추가
       dic['a'] = 'airplane'
       
       # key를 통해 항목 삭제
       pop_data = dic.pop('a')
       ```

   

   - `.update([other])`

     - 값을 제공하는 key, value로 덮어쓴다.

       ```python
       dic = {'apple': '사'}
       dic.update(apple='사과')
       ```



# 3. 기타

- [파이썬 코딩 도장](https://dojang.io/course/view.php?id=7)