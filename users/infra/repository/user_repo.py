from database import SessionLocal
from users.domain.repository.user_repo import IUserRepository
from users.domain.user import User as UserV0
from users.infra.db_models.user import User
from fastapi import HTTPException
from utils.db_utils import row_to_dict

class UserRepository(IUserRepository):
    def save(self, user:UserV0):
        new_user = User(
            id = user.id,
            email = user.email,
            name = user.name,
            password = user.password,
            memo = user.memo,
            created_at = user.created_at,
            updated_at = user.updated_at,
        )

        with SessionLocal() as db:
            try:
                db.add(new_user)
                db.commit()
            finally:
                db.close()

    def find_by_email(self, email:str) -> UserV0:
        with SessionLocal() as db:
            user = db.query(User).filter(User.email == email).first()

        if not user:
            raise HTTPException(status_code=422)

        return UserV0(**row_to_dict(user))

    def find_by_id(self, user_id: str) -> UserV0:
        with SessionLocal() as db:
            user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(status_code=422)

        return UserV0(**row_to_dict(user))

    def update(self, user_vo: UserV0) -> None:
        with SessionLocal() as db:
            user = db.query(User).filter(User.id == user_vo.id).first()

            if not user:
                raise HTTPException(status_code=422)

            user.name = user_vo.name
            user.password = user_vo.password
            user.memo = user_vo.memo
            user.updated_at = user_vo.updated_at

            db.commit()
