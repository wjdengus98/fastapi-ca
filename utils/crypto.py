from passlib.context import CryptContext

class Crypto:
    """bcrypt를 사용해 비밀번호를 해싱하고 검증한다."""

    def __init__(self):
        # 새 해시는 bcrypt로 생성하고, 사용 중단된 해시 형식은 자동으로 식별한다.
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def encrypt(self,secret):
        """평문 비밀번호를 복원할 수 없는 해시값으로 변환한다."""
        return self.pwd_context.hash(secret)
    
    def verify(self,secret,hash):
        """입력된 평문 비밀번호가 저장된 해시값과 일치하는지 확인한다."""
        return self.pwd_context.verify(secret, hash)
    
