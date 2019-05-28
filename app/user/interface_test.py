from pytest import fixture
from .model import User
from .interface import UserInterface


@fixture
def interface() -> UserInterface:
    return UserInterface(
        username="testuser", password='testpassword', email='testemail@gmail.com'
    )

def test_UserInterface_create(interface: UserInterface):
    assert interface


def test_UserInterface_works(interface: UserInterface):
    user = User(**interface)
    assert user