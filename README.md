# My-Precious-Note

public/private 옵션과 '좋아요' 기능을 제공하는 메모 앱.



## I. 프로젝트 기능

- 로그인/회원가입
- 메모 읽기/수정/삭제
- 메모 생성시 지정한 옵션에 따라 다른 사람에게 공개/비공개 가능

	| Memo Option | Read | Write |
	| :----: | :----: | :-----: |
	| public | owner, guest | owner |
	| private | owner | owner |


- 개인 페이지 제공
- 메모 조회 및 필터링



## II. 개발 및 배포

### (1) 개발 환경

- Language : Python(3.6.7), Html, CSS, Javascript

- Framework : Django(2.2.3), Bootstrap(4.3.1)

- requirements.txt : package lit

	```
	# package install
	pip install -r requirements.txt
	```



### (2) 배포 환경

- 배포 플랫폼 : Heroku



## III. 설계

### (1) DB 설계

- #### Note Table

  | Field | Type | Description |
  | :----: | :----: | :----- |
  | id | Number, PK | 메모 식별키 |
  | title | Text | 메모 제목 |
  | content | Text | 메모 내용 |
  | isPublic | Boolean(default=False) |  public/private 설정 |
  | created_at | DateTime | 메모 생성 날짜 및 시간 |
  | updated_at | DateTime | 업데이트 날짜 및 시간 |
  | user | Number,FK | User Table과 1:N 관계 |
  | like_users | Number,FK | User Table과 M:N 관계 |


- #### User Table

  
  - Django에서 제공하는 User 모델과 1:1로 매핑하여 사용한다.
  <br/>
  
  | Field | Type | Description |
  | :----: | :----: | :----- |
  | id | Number, PK | 사용자 식별키 |
  | user | Number, FK | Django User Model 과 1:1 관계 <br />(https://docs.djangoproject.com/en/2.2/ref/contrib/auth/) |
  | nickname | Text | 닉네임 |



### (2) URL 설계

- #### notes app

	| Method | URL | Rule |
	| :----: | :---- | :----- |
	| GET | /notes/ | `public`  메모 목록 조회 |
	| GET | /notes/1/like | 좋아요 기능 |
	| POST | /notes/ | `private`  메모 목록 조회 |
	| GET | /notes/create | 새 메모 작성 폼 |
	| POST | /notes/creare | 새 메모 생성 |
	| GET | /notes/1/update | 메모 수정 폼 |
	| POST | /notes/1/update | 메모 수정 |
	| POST | /notes/1/delete | 메모 삭제 |


- #### accounts app

	| Method | URL              | Rule                       |
	| :----: | :--------------- | :------------------------- |
	|  GET   | /accounts/login  | 로그인 폼                  |
	|  POST  | /accounts/login  | 로그인                     |
	|  POST  | /accounts/logout | 로그아웃                   |
	|  GET   | /accounts/signup | 회원 가입 폼               |
	|  POST  | /accounts/signup | 회원 가입                  |
    |  GET   | /accounts/update | 회원 정보 변경 폼               |
	|  POST  | /accounts/update | 회원 정보 변경                  |
	|  GET   | /accounts/1      | 개인 페이지                |
