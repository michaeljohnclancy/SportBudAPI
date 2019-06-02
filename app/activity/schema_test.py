from pytest import fixture

from .model import Activity
from .schema import ActivitySchema
from .interface import ActivityInterface

import datetime



@fixture
def schema() -> ActivitySchema:
    return ActivitySchema()


def test_activitySchema_create(schema: ActivitySchema):
    assert schema


def test_activitySchema_works(schema: ActivitySchema):
    params: ActivityInterface = schema.load({
        'activityName': 'test activity',
        'activityDescription': 'Test Description!',
        'activityTime': '2019-02-01 22:01:00',
        'activityLocation': 'Edinburgh'
    })

    activity = Activity(**params.data)

    assert activity.name == 'test activity'
    assert activity.description == 'Test Description!'
    assert activity.activity_time == datetime.datetime(2019, 2, 1, 22, 1)
    assert activity.location == 'Edinburgh'