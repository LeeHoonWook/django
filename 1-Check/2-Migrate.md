# 1. migrate 오류 시

```sh
# syncdb는 settings.py의 Installed apps에서 추가된 앱에 대한 테이블을 처음 db에 만들어주는 command
(venv) User $ python manage.py migrate --run-syncdb

# db 초기화
(venv) User $ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
(venv) User $ find . -path "*/migrations/*.pyc"  -delete
(venv) User $ rm -rf db.sqlite3

(venv) User $ pip install --upgrade --force-reinstall Django
```

# 2. migrate & superuser

```sh
# 처음에 만들어야하는 장고프레임워크가 필요로 하는 데이터베이스를 생성
(venv) User $ python manage.py migrate

# 내가 만든 model을 생성한 후 실행
(venv) User $ python manage.py makemigrations (app명)
(venv) User $ python manage.py migrate (app명)

# 앱의 첫 슈퍼유저 생성
(venv) User $ python manage.py createsuperuser
```