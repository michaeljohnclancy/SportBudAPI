from pytest import fixture
from .model import Activity
from .interface import ActivityInterface
import time


@fixture
def interface() -> ActivityInterface:
    return ActivityInterface(
        name='Test Activity', description='An easy test activity!', activity_time=time.time(), location='test city!'
    )

def test_activityInterface_create(interface: ActivityInterface):
    assert interface


def test_activityInterface_works(interface: ActivityInterface):
    activity = Activity(**interface)
    assert activity