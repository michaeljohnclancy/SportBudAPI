from app import db
from typing import List
from .model import User
from .interface import UserInterface
from passlib.context import CryptContext

class UserService():

    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )

    @staticmethod
    def get_all() -> List[User]:
        return User.query.all()

    @staticmethod
    def get_by_id(id: str) -> User:
        return User.query.get(id)

    @staticmethod
    def update(user: User, user_change_updates: UserInterface) -> User:
        user.update(user_change_updates)
        db.session.commit()
        return user

    @staticmethod
    def delete_by_id(id: str) -> List[str]:
        user = User.query.filter(User.id == id).first()
        if not user:
            return []
        db.session.delete(user)
        db.session.commit()
        return [id]

    @staticmethod
    def create(new_attrs: UserInterface) -> User:
        new_user = User(
            username=new_attrs['username'],
            password=new_attrs['password'],
            email=new_attrs['email']
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user