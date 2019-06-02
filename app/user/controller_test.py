from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from .service import UserService
from .schema import UserSchema
from .model import User
from .interface import UserInterface
from . import BASE_ROUTE

from uuid import UUID, uuid4

from datetime import datetime



def make_new_user(uuid: UUID = uuid4(), username: str = 'TestUser',
                  password: str = 'TestPassword', email: str = 'TestEmail@gmail.com') -> User:
    return User(
        uuid=uuid, username=username, password=password, email=email
    )


test_uuid1 = uuid4()
test_uuid2 = uuid4()


class TestUserResource:
    @patch.object(UserService, 'get_all',
                  lambda: [
                      make_new_user(uuid=test_uuid1, username='TestUser1', password='TestPassword1', email='TestEmail1@gmail.com'),
                      make_new_user(uuid=test_uuid2, username='TestUser1', password='TestPassword1', email='TestEmail1@gmail.com')])
    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(f'/api/{BASE_ROUTE}',
                                 follow_redirects=True).get_json()
            expected = UserSchema(many=True).dump(
                [make_new_user(test_uuid1, username='TestUser1', password='TestPassword1', email='TestEmail1@gmail.com'),
                 make_new_user(test_uuid2, username='TestUser1', password='TestPassword1', email='TestEmail1@gmail.com')]
            ).data
            for r in results:
                assert r in expected
                
    @patch.object(UserService, 'create',
                  lambda create_request: User(**create_request))
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(username='Test User',
                           password='testpassword',
                           email='test_email@gmail.com')

            result = client.post(f'/api/{BASE_ROUTE}/', json=payload).get_json()

            expected = UserSchema().dump(User(
                username=payload['username'],
                password=payload['password'],
                email=payload['email'],
            )).data

            assert result == expected


def fake_update(user: User, changes: UserInterface) -> User:
    # To fake an update, just return a new object
    updated_user = User(uuid=user.uuid,
                        username=changes['username'],
                        password=changes['password'],
                        email=changes['email'])
    return updated_user


class TestUserUUIDResource:
    @patch.object(UserService, 'get_by_uuid',
                  lambda user_uuid: make_new_user(uuid=user_uuid))
    def test_get(self, client: FlaskClient):
        with client:

            result = client.get(f'/api/{BASE_ROUTE}/{test_uuid1}').get_json()
            expected = make_new_user(uuid=test_uuid1)

            assert result['userUUID'] == str(expected.uuid)

    @patch.object(UserService, 'delete_by_uuid',
                  lambda user_uuid: user_uuid)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:

            result = client.delete(f'/api/{BASE_ROUTE}/{test_uuid1}').get_json()
            expected = dict(status='Success', userUUID=str(test_uuid1))

            assert result == expected

    @patch.object(UserService, 'get_by_uuid',
                  lambda user_uuid: make_new_user(uuid=user_uuid))
    @patch.object(UserService, 'update', fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result = client.put(f'/api/{BASE_ROUTE}/{test_uuid1}',
                                json={'username': 'New Username',
                                      'password': 'passwordtest',
                                      'email': 'email@gmail.com'}).get_json()
            expected = UserSchema().dump(
                User(uuid=test_uuid1, username='New Username', password='passwordtest', email='email@gmail.com')).data

            assert result == expected



