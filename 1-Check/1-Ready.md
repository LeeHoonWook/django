# 1. 환경 설정

> 해당 개발 환경은 window의 wsl2를 기반으로 작성되었습니다.   

```sh
# pip 안될 시
User $ sudo apt-get install python3-pip

# 가상환경 생성 및 실행
User $ sudo pip3 install virtualenv virtualenvwrapper
User $ virtualenv --python=python3 가상환경명
User $ source 환경명/bin/activate
(venv) User $ 필요한 모듈 설치

# 패키지 관리
(venv) User $ pip freeze > requirements.txt

# 내려받기 
(venv) User $ pip install -r requirements.txt
```

# 2. Django 시작 

```sh
# 장고 설치
(venv) User $ pip install django

# django-environ 설치
(venv) User $ pip install django-environ

# 장고 시작
(venv) User $ django-admin startproject 프로젝트명
(venv) User $ cd 프로젝트명

# app 생성
(venv) User $ python manage.py startapp 폴더명

# 장고 실행
(venv) User $ python manage.py runserver
```