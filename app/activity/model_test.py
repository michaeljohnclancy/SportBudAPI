from pytest import fixture
from .model import Activity

import time

@fixture
def activity() -> Activity:
    return Activity(
        name='Test Activity', description='An easy test activity!', activity_time=time.time(), location='test city!'
    )

def test_Widget_create(activity: Activity):
    assert activity