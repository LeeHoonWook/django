class PasswordMatchError(Exception):
    def __init__(self):
        super().__init__('비밀번호가 일치하지 않습니다.')


class PasswordLengthError(Exception):
    def __init__(self):
        super().__init__('비밀번호가 4자리 이하입니다.')
