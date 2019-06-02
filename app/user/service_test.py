from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.test.fixtures import app, db  # noqa
from .model import User
from .service import UserService  # noqa
from .interface import UserInterface

from uuid import uuid4


def test_get_all(db: SQLAlchemy):
    test_user1: User = User(uuid=uuid4(), username="user1", password='pass1', email='email1@gmail.com')
    test_user2: User = User(uuid=uuid4(), username="user2", password='pass2', email='email2@gmail.com')
    db.session.add(test_user1)
    db.session.add(test_user2)
    db.session.commit()

    results: List[User] = UserService.get_all()

    assert len(results) == 2
    assert test_user1 in results and test_user2 in results


def test_update(db: SQLAlchemy):
    test_user: User = User(uuid=uuid4(), username="user1", password='pass1', email='email1@gmail.com')

    db.session.add(test_user)
    db.session.commit()
    updates: UserInterface = dict(email='newemail@gmail.com')

    UserService.update(test_user, updates)

    result: User = User.query.get(test_user.uuid)
    assert result.email == 'newemail@gmail.com'


def test_delete_by_uuid(db: SQLAlchemy):
    test_user1: User = User(uuid=uuid4(), username="user1", password='pass1', email='email1@gmail.com')
    test_user2: User = User(uuid=uuid4(), username="user2", password='pass2', email='email2@gmail.com')
    db.session.add(test_user1)
    db.session.add(test_user2)
    db.session.commit()

    UserService.delete_by_uuid(test_user1.uuid)
    db.session.commit()

    results: List[User] = User.query.all()

    assert len(results) == 1
    assert test_user1 not in results and test_user2 in results


def test_create(db: SQLAlchemy):

    test_user_interface: UserInterface = UserInterface(username="user1", password='pass1', email='email1@gmail.com')
    UserService.create(test_user_interface)

    results: List[User] = User.query.all()

    assert len(results) == 1

    for k in test_user_interface.keys():
        if k == 'password':
            assert results[0].verify_password(test_user_interface[k])
        else:
            assert getattr(results[0], k) == test_user_interface[k]
