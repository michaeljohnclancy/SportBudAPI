from pytest import fixture
from .model import Activity
from .interface import ActivityInterface
import time

from uuid import uuid4

@fixture
def interface() -> ActivityInterface:
    return ActivityInterface(
        uuid=uuid4(), name='Test Activity', description='An easy test activity!', activity_time=time.time(), location='test city!'
    )

def test_activityInterface_create(interface: ActivityInterface):
    assert interface


def test_activityInterface_works(interface: ActivityInterface):
    activity = Activity(**interface)
    print(activity)
    assert activity