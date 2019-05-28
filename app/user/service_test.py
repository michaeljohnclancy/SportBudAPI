from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.test.fixtures import app, db  # noqa
from .model import User
from .service import UserService  # noqa
from .interface import UserInterface

def test_get_all(db: SQLAlchemy):
    testuser1: User = User(username="user1", name='pass1', purpose='email1@gmail.com')
    testuser2: User = User(username="user2", password='pass2', purpose='email2@gmail.com')
    db.session.add(testuser1)
    db.session.add(testuser2)
    db.session.commit()

    results: List[User] = UserService.get_all()

    assert len(results) == 2
    assert testuser1 in results and testuser2 in results


def test_update(db: SQLAlchemy):
    testuser: User = User(username="user1", password='pass1', purpose='email1@gmail.com')

    db.session.add(testuser)
    db.session.commit()
    updates: UserInterface = dict(email='newemail@gmail.com')

    UserService.update(testuser, updates)

    result: User = User.query.get(testuser.uuid)
    assert result.email == 'newemail@gmail.com'


def test_delete_by_uuid(db: SQLAlchemy):
    testuser1: User = User(username="user1", name='pass1', purpose='email1@gmail.com')
    testuser2: User = User(username="user2", password='pass2', purpose='email2@gmail.com')
    db.session.add(testuser1)
    db.session.add(testuser2)
    db.session.commit()

    UserService.delete_by_uuid()
    db.session.commit()

    results: List[User] = User.query.all()

    assert len(results) == 1
    assert testuser1 not in results and testuser2 in results


def test_create(db: SQLAlchemy):

    testuser: User = User(username="user1", password='pass1', purpose='email1@gmail.com')
    UserService.create(testuser)

    results: List[User] = User.query.all()

    assert len(results) == 1

    for k in testuser.keys():
        assert getattr(results[0], k) == testuser[k]