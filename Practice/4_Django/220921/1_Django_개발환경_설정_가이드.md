# Django 개발 환경 설정 가이드



## 1. 프로젝트를 진행할 폴더 선택

- 아래와 같은 경로의 폴더를 VSCode로 열어, 해당 터미널에서 진행해보려고 한다.

  ![image-20220921135941676](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921135941676.png)



## 2. 서버 폴더 만들기

- `test-server`라는 이름의 폴더를 현재 폴더에 추가해 준다. (이름은 자유)

  ```bash
  $ mkdir [폴더이름]
  ```

  ![image-20220921135922617](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921135922617.png)

- 그리고 `test-server` 폴더로 이동한다.

  ```bash
  $ cd [폴더이름]
  ```

  ![image-20220921140457336](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921140457336.png)

  - `cd test-server` 와 `cd ./test-server`, `cd test-server/` 모두 가능하다.



## 3. 가상 환경 만들기

- 프로젝트마다 각각의 가상 환경을 만드는 것이 일반적이다.
  - 가상 환경을 만들어 해당 프로젝트에 필요한 패키지 관리를 수월하게 할 수 있다.
  - 패키지 버전을 통일하여, 호환성 문제를 차단한다.

- 파이썬 3.4 부터는 venv라는 패키지를 이용한다.



- `server-venv`라는 이름의 가상 환경을 만들어 준다. (이름은 자유)

  ```bash
  $ python -m venv [가상환경이름]
  ```

  ![image-20220921142333544](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921142333544.png)

- 그러면 `test-server` 폴더 속에 `server-venv`라는 폴더가 생성된다.
- 가상 환경이 만들어졌지만, 아직 실행된 것은 아니다.



## 4. 가상 환경 실행하기

- source 명령어를 통해서 실행할 수 있다.

- Window와 Mac의 명령어는 차이가 있는데, 아래는 윈도우에서의 모습이다.

- 가상 환경이 실행되면, 위에 `(server-venv)`라고 가상 환경 이름이 뜨게 된다.

- 가상 환경 내에서 작업할 때 저것이 항상 잘 있는지 확인해야 한다.

  ![image-20220921142709103](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921142709103.png)

  - Window

    ```bash
    $ source [가상환경이름]/Scripts/activate
    ```

  - Mac

    ```bash
    $ source [가상환경이름]/bin/activate
    ```



- 가상 환경 종료

  ```bash
  $ deactivate
  ```



## 5. Django 설치하기

- Django는 가상 환경에서 설치해야 한다.

- 완전히 최신 버전은 불안정할 수 있으므로, 3.2.13 버전을 설치한다.

  ```bash
  $ pip install django==3.2.13
  ```

  ![image-20220921143828976](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921143828976.png)

- 아래와 같이 나오면 설치 성공

  ![image-20220921143916431](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921143916431.png)

- 노란 글씨로 WARNING 되어 있는 건 무시해도 된다고 들었던 것 같다.



- 설치된 pip들은 다음과 같은 명령어로 확인할 수 있다.

  ```bash
  $ pip list
  ```

  ![image-20220921144233973](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921144233973.png)



- 가상 환경에 설치된 패키지는 목록을 저장해 두었다가, 나중에 다시 설치할 수도 있다. (통상적으로 `requirements.txt` 라는 이름의 파일에 저장한다.)

  ```bash
  $ pip freeze > requirements.txt
  ```

  ![image-20220921145024097](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921145024097.png)

- `requirements.txt` 파일의 내용대로 패키지를 설치

  ```bash
  $ pip install -r requirements.txt
  ```



## 6. Django 실행하기

- Django를 처음 실행한다면, 초기 설정을 위해 다음과 같은 명령어를 입력해 준다. (프로젝트 이름은 자유)

- 아래 명령어를 입력하면 프로젝트 이름으로 폴더가 생성되는데, 시작 경로는 그 폴더가 어디에 생성되어야 할 지를 결정한다.

  ```bash
  $ django-admin startproject [프로젝트이름] [시작경로]
  ```

  ![image-20220921145926453](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921145926453.png)

- 그러면 `test-server`에 `firstPjt`라는 폴더가 하나 생기고, 그 아래 `manage.py` 폴더가 생성된 것을 확인할 수 있다.

- 서버를 작동하려면 다음과 같은 명령어를 입력해 준다.

  ```bash
  $ python manage.py runserver
  ```



- 서버가 실행되면, `http://127.0.0.1:8000`이나 `http://localhost:8000`을 검색하여 들어갈 수 있고, 아래와 같은 화면을 볼 수 있다.

  ![image-20220921150457246](Assets/1_Django_개발환경_설정_가이드.assets/image-20220921150457246.png)

- 서버를 종료하기 위해서는, 터미널에 가서 `Ctrl + C`를 누른다.