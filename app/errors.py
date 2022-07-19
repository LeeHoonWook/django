class PasswordMatchError(Exception):
    def __init__(self):
        super().__init__('비밀번호가 일치하지 않습니다.')
