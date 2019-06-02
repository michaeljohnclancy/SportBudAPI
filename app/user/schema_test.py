from pytest import fixture

from .model import User
from .schema import UserSchema
from .interface import UserInterface


@fixture
def schema() -> UserSchema:
    return UserSchema()


def test_user_schema_create(schema: UserSchema):
    assert schema


def test_user_schema_works(schema: UserSchema):
    params: UserInterface = schema.load({
        'username': 'testuser',
        'password': 'testpassword',
        'email': 'testemail@gmail.com'
    }).data
    user = User(**params)

    assert user.username == 'testuser'
    assert user.verify_password('testpassword')
    assert user.email == 'testemail@gmail.com'
