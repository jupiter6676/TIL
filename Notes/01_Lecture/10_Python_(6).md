# 1. 딕셔너리 해설

1. 파이썬 실습 문제 18번. 알파벳 등장 개수 구하기

   ```python
   word = 'banana'
   result = dict()
   
   # 첫 번째 방법
   for char in word:
       # 기존에 키가 없으면, 1로 초기화
       if char not in result:
           result[char] = 1
       # 키가 있으면, 기존 값에 더함
       else:
           result[char] += 1
           
   # 두 번째 방법
   for char in word:
       # result[char]	# 없으면 KeyError
       # result.get(char, 0)	# 없으면 None, {char: 0}의 아이템 하나 생성
       result[char] = result.get(char, 0) + 1
   ```



# 2. 에러/예외 처리 (Error/Exception Handling)

- 디버깅을 할 때, 어떤 부분을 중점으로 봐야 할까?
  - Branches: 모든 조건이 원하는대로 동작하는지
  - For loops: 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
  - While loops: For loops와 동일, 종료조건이 제대로 동작하는지
  - Function: 함수 호출 시, 함수 파라미터, 함수 결과
- 디버깅 방법
  - print 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각
    - 코드를 bisection으로 나눠서 실행
  - 개발 환경 (text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
  - Python tutor 활용 (단순 파이썬 코드인 경우)
  - 뇌 컴파일, 눈 디버깅
- 코드를 작성하다가
  - 로직 에러가 발생하는 경우: 명시적 에러 메시지 없이 예상과 다른 결과가 나온 경우
    - 정상적으로 동작했던 코드 이후 작성된 코드를 생각해보기
    - 전체 코드를 살펴보기
    - 휴식을 가져보기
    - 누군가에게 설명해보기



# 3. 에러와 예외

1. 에러 (Error)
   - 에러가 발생하면, 프로그램이 실행되지 않음
2. 예외 (Exception)
   - 실행 중 감지되는 에러
   - 예외 타입의 종류
     - Exception: 예외들 중 가장 상위에 있는 것
     - NameError: 네임스페이스 상에 변수 이름이 존재하지 X❣️❣️❣️❣️
     - TypeError: 타입 불일치
     - ValueError: 타입은 올바르나, 값이 적절하지 않거나 없는 경우
     - IndexError, KeyError, ModuleNotFoundError, ImportError, IndentationError



# 4. 예외 처리

1. try - except

   - `try` 문

     - 오류가 발생할 가능성이 있는 코드를 실행

   - `except` 문

     - 예외가 발생하면, except 문이 실행
     - 아래는 발생할 수 있는 에러 2개에 대해, 각각 예외처리를 해 준 예시 → 단, 하위 에러들을 먼저 적어주어야 한다.
     - 에러가 발생하면, 에러 메시지 대신 아래의 문구를 출력해준다.

     ```python
     num = input()
     
     try:
         print(100/int(num))
         
     except ZeroDivisionError as e:
         print(e)	# division by zero
         print('0으로 나눌 수 없습니다.')
     except ValueError:
         print('숫자 형식을 입력해주세요.')
         
     # 가장 상위의 에러를 맨 밑에
     # 위 2개 에러를 제외한 나머지 오류에 대하여 '오류'라는 문구를 출력한다.
     except Exception:
         print('오류')
     ```

   - `else`

     - try 문에서 예외가 발생하지 않으면 실행

   - `finally`

     - 예외 발생 여부와 관계없이 항상 실행



2. 예외 처리 예시

   - 파일을 열고 읽는 코드를 작성하는 경우

   - 파일 열기 시도
     - 파일이 없는 경우 → '해당 파일이 없습니다.' 출력 (except)
     - 파일이 있는 경우 → 파일 내용을 출력 (else)

   - 파일 읽기 작업 종료 → '파일 읽기를 종료합니다.' 출력 (finally)

   ```python
   try:
       f = open('test.txt')
   except FileNotFoundError:
       print('해당 파일이 없습니다.')
   else:
       print('파일을 읽기 시작합니다.')
       print(f.read())
       print('파일을 모두 읽었습니다.')
       f.close
   finally:
       print('파일 읽기를 종료합니다.')
   ```



# 5. 예외 발생시키기

- `raise`를 통해, 강제로 예외를 발생시킴.
- 파이썬 내부적으로 사용됨.