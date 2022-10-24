# 1. 상담

## (1) 기술 스택 전환 & 학습 부족

- 다음 주부터 있는 프로젝트를 위해 지금까지 달려온 것도 있다.
- 100% 공부만 하는 것이 다가 아니다. (조모임 X)
- 기능 개발을 협업으로 하는 첫 번째 시간
- 프로젝트 기간을 길게 잡은 이유: 마지막 프로젝트 정도에는 기술 스택을 전환하거나, 다른 부분을 각자 키워나갈 수 있도록 하기 위해서
- 자바/스프링을 배우는 것도, Django로 프로젝트를 해보고 배우는 것과 아닌 것이 다르다.
- 상담 팁
  - 목표를 정한 상태에서 이야기하면 가장 Best
  - 목표를 정하기 위한 정보 수집
    - 본인이 어느 정도 찾고, 어떠한 내용을 이야기 해야 도움 주시기가 더 좋다.



# 2. Many to many relationship

## (1) 개요

- 병원 예약 시스템 구축을 위한 DB 모델링을 진행한다면?
  - 만약 1:N(환자1, 의사N)으로 모델링하면, 환자는 여러 명의 의사에게 동시에 예약할 수 없다.
  - 1:N 관계에서는, 동일한 환자여도 다른 의사에게 예약하기 위해서는, 객체를 하나 더 만들어 예약을 진행해야 한다.
    - 새로운 환자 객체를 생성할 수밖에 없다.
  - 외래 키 컬럼에 '1, 2'의 형태로 참조하는 것은 Integer 타입이 아니기 때문에 불가능하다.
  - 따라서, **예약 테이블**을 따로 만들어야 한다. → **중개 모델**
    - 이 모델은 의사와 환자에 대해 각각 1:N 관계를 가진다.
- 이는 좋아요도 마찬가지
  - 좋아요 테이블을 따로 만들어서, 글의 id와 좋아요한 사람의 id를 함께 저장한다.



## (2) 중개 모델

1. 환자 모델의 외래 키를 삭제하고, 별도의 예약 모델을 새로 작성

   ```python
   # hospitals/models.py
   
   class Patient(models.Model):
       name = models.TextField()
       def __str__(self):
   		return f'{self.pk}번 환자 {self.name}'
   
   # 중개모델 작성
   class Reservation(models.Model):
       doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
       patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
       def __str__(self):
       	return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
   ```



2. 의사와 환자 생성 후 예약 만들기 → **`create()`**

   ```python
   d1 = Doctor.objects.create(name='alice')
   p1 = Patient.objects.create(name='carol')
   
   Reservation.objects.create(doctor=d1, patient=p1)
   ```



3. 예약 정보 조회

   ```python
   # 의사 → 예약 정보 찾기
   d1.reservation_set.all()
   # <QuerySet [<Reservation: 1번 의사의 1번 환자>]>
   
   # 환자 → 예약 정보 찾기
   patient1.reservation_set.all()
   # <QuerySet [<Reservation: 1번 의사의 1번 환자>]>
   ```



4. 1번 의사에게 새로운 환자 예약 생성

   ```python
   p2 = Patient.objects.create(name='dane’)
   Reservation.objects.create(doctor=d1, patient=p2)
   ```



## (3) ManyToManyField ①

1. ManyToManyField를 사용하면 자동으로 중개 테이블이 생성된다. (hospitals_patient_doctors)

   ```python
   # hospitals/models.py
   
   class Patient(models.Model):
       doctors = models.ManyToManyField(Doctor)
       # ...
       
   # Reservation Class 주석 처리
   ```



2. 의사 1명과 환자 2명 생성

   ```python
   d1 = Doctor.objects.create(name=
   'alice')
   
   p1 = Patient.objects.create(name='carol')
   p2 = Patient.objects.create(name=
   'dane')
   ```



3. 예약 생성 (환자가 의사에게 예약) → **`add()`**

   ```python
   # 환자1이 의사1에게 예약
   p1.doctors.add(d1)
   
   # 환자1 - 자신이 예약한 의사 목록 확인
   p1.doctors.all()
   # <QuerySet [<Doctor: 1번 의사 alice>]>
   
   # 의사2 - 자신의 예약된 환자 목록 확인
   d1.patient_set.all()
   # <QuerySet [<Patient: 1번 환자 carol>]>
   ```



4. 예약 생성 (의사가 환자를 예약)

   ```python
   # 의사1이 환자2를 예약
   d1.patient_set.add(p2)
   
   # 의사1 - 자신의 예약된 환자 목록 확인
   d1.patient_set.all()
   
   # 환자2 - 자신이 예약한 의사 목록 확인
   p2.doctors.all()
   ```



5. 예약 취소(삭제) → **`remove()`** (기존은 해당하는 예약을 찾아서 지워야 했다.)

   ```python
   # 의사1이 환자1 진료 예약 취소
   d1.patient_set.remove(p1)
   
   # 환자2가 의사1 진료 예약 취소
   p2.doctors.remove(d1)
   ```





- 중개 모델을 직접 작성하는 것과, ManyToManyField를 사용하는 것의 차이점은?
  - 둘 모두 구조는 id, doctor_id, patient_id로 같다. (테이블 이름은 다를 수 있다.)
  - ManyToManyField는 p1.doctors.all()을 하면, 그 결과로 환자1이 만난 모든 의사들을 바로 확인할 수 있다.
  - 중개 모델(Reservation)을 직접 작성하면, p1.reservation_set.all()로 예약 정보들을 확인할 수 있지만, 환자1이 만난 모든 의사들을 바로 확인하기는 힘들다.
- 그러면 중개 모델을 직접 작성해야 할 때는 언제일까?
  - 환자 id와 의사 id 이외에, 예약 시간과 상담 내용 등과 같은 다른 정보도 함께 저장하고 싶을 때



- 중개 모델을 하나 만들고, ManyToManyField의 through 옵션을 사용하면, p1.doctors.all()로 환자1이 만난 모든 의사들을 찾을 수 있다.

  ```python
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor, through='Reservation')
  ```

- ManyToManyField에서 역참조를 바로 하고 싶으면, related_name을 함께 넣는다. (= 역참조 이름을 정한다고 생각하면 OK)

  ```python
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor, related_name='patient')
  ```

  - doctors.patient_set.all() 대신에,

  - doctors.patient.all()로 조회할 수 있다.

  - 필수로 사용해야 하는 상황이 있는데, 역참조 모델 이름이 같을 경우

    ```python
    class Article(models.Model):
        user = models.ForeignKey(...)
        like_users = models.ManyToManyField(..., related_name='like_articles')
    ```



## (4) ManyToManyField ②

1. `related_name` 인자

   ```python
   class Patient(models.Model):
   # ManyToManyField - related_name 작성
   	doctors = models.ManyToManyField(Doctor, related_name='patients')
   	# ...
   ```

   - target model이 source model을 참조할 때 사용할 manager name (역참조 시 사용할 manager 이름)
   - ForeignKey()의 related_name과 동일
   - 위와 같이 설정하면, 의사가 환자를 역참조할 시, `d1.patient_set.all()` 대신, `d1.patients.all()`과 같은 형식으로 사용할 수 있다.



2. `through` 인자

   ```python
   class Patient(models.Model):
       doctors = models.ManyToManyField(Doctor, through='Reservation')
       name = models.TextField()
       
       def __str__(self):
       	return f'{self.pk}번 환자 {self.name}'
   
   class Reservation(models.Model):
       doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
       patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
       symptom = models.TextField()
       reserved_at = models.DateTimeField(auto_now_add=True)
       
       def __str__(self):
       	return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
   ```

   - 중개 모델을 직접 작성하는 경우,
   - 모델에 through 옵션을 사용하여, 그 모델에서 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있다.
   - 가장 일반적인 용도는, 중개테이블에 id 외의 추가 데이터를 정의하여 다대다 관계와 연결할 때 사용한다,
     - 위의 경우에는 symptom과 reserved_at



3. `symmertrical` 인자

   ```python
   # 예시
   class Person(models.Model):
       friends = models.ManyToManyField('self')
       # friends = models.ManyToManyField('self', symmetrical=False)
   ```

   - 기본 값: True
   - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용한다.
   - True일 경우
     - _set 매니저를 추가 하지 않는다.
     - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면, target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 한다. (대칭)
     - 즉, 내가 당신의 친구라면 당신도 내 친구가 되는 것
   - 대칭을 원하지 않는 경우 False로 설정
     - Follow 기능 구현에서 다시 확인할 예정



## (5) 정리

- M:N 관계로 맺어진 두 테이블에는 변화가 없다.
- Django의 ManyToManyFieldsms 중개 테이블을 자동으로 생성한다.
- Django의 ManyToManyField는 M:N 관계를 가진 모델 어디에 위치해도 상관 없다.
  - 대신, 필드 작성 위치에 따라 참조와 역참조 방향을 주의해야 한다.



# 3. 좋아요 기능 구현

- DB에 좋아요를 어떻게 기록할 것인지?
  - Article(M) - User(N)
  - Article은 0명 이상의 User에게 좋아요를 받는다.
  - User는 0개 이상의 Article에 좋아요를 누를 수 있다.
- 로직
  - URL: /articles/\<int:pk>/like/
  - 상세보기 페이지에서 좋아요 링크를 누르면,
  - 좋아요를 DB에 추가하고, 다시 상세보기 페이지로 redirect