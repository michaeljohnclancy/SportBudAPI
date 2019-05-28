from pytest import fixture
from .model import User

@fixture
def user() -> User:
    return User(
        username='testuser', password='passwordtest', email='testemail@gmail.com'
    )


def test_Widget_create(user: User):
    assert user