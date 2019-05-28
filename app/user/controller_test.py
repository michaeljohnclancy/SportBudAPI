from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from .service import UserService
from .schema import UserSchema
from .model import User
from .interface import UserInterface
from . import BASE_ROUTE


def make_new_user(id: int = 123, username: str = 'TestUser',
                  password: str = 'TestPassword', email: str = 'TestEmail@gmail.com') -> User:
    return User(
        id=id, username=username, password=password, email=email
    )


class TestUserResource:
    @patch.object(UserService, 'get_all',
                  lambda: [
                      make_new_user(123, username='TestUser1', password='TestPassword1', email='TestEmail1@gmail.com'),
                      make_new_user(456, username='TestUser1', password='TestPassword1', email='TestEmail1@gmail.com')])
    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(f'/api/{BASE_ROUTE}',
                                 follow_redirects=True).get_json()
            expected = UserSchema(many=True).dump(
                [make_new_user(123, username='TestUser1', password='TestPassword1', email='TestEmail1@gmail.com'),
                 make_new_user(456, username='TestUser1', password='TestPassword1', email='TestEmail1@gmail.com')]
            ).data
            for r in results:
                assert r in expected
