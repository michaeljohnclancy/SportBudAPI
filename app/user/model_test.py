from pytest import fixture
from .model import User
from flask_sqlalchemy import SQLAlchemy
# noinspection PyUnresolvedReferences
from app.test.fixtures import app, db
from uuid import uuid4

@fixture
def user() -> User:
    return User(
        uuid=uuid4(), username='testuser', password='passwordtest', email='testemail@gmail.com'
    )


def test_user_create(user: User):
    assert user

def test_activity_retrieve(user: User, db: SQLAlchemy):  # noqa
    db.session.add(user)
    db.session.commit()
    s = User.query.first()
    assert s.__dict__ == user.__dict__
