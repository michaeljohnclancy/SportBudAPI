from pytest import fixture
from .model import User
from .interface import UserInterface

from uuid import uuid4


@fixture
def interface() -> UserInterface:
    return UserInterface(
        uuid=uuid4(), username="testuser", password='testpassword', email='testemail@gmail.com'
    )


def test_user_interface_create(interface: UserInterface):
    assert interface


def test_user_interface_works(interface: UserInterface):
    user = User(**interface)
    print(user)
    assert user
