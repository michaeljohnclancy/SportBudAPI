from app import db
from typing import List
from .model import User
from .interface import UserInterface

from uuid import UUID, uuid4


class UserService:

    @staticmethod
    def get_all() -> List[User]:
        return User.query.all()

    @staticmethod
    def get_by_uuid(activity_uuid: UUID) -> User:
        return User.query.get(activity_uuid)

    @staticmethod
    def update(user: User, user_change_updates: UserInterface) -> User:
        user.update(user_change_updates)
        db.session.commit()
        return user

    @staticmethod
    def delete_by_uuid(activityUUID: UUID) -> List[UUID]:
        user = User.query.filter(User.uuid == activityUUID).first()
        if not user:
            return []
        db.session.delete(user)
        db.session.commit()
        return [activityUUID]

    @staticmethod
    def create(new_attrs: UserInterface) -> User:
        new_user = User(
            uuid=uuid4(),
            username=new_attrs['username'],
            password=new_attrs['password'],
            email=new_attrs['email']
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user
