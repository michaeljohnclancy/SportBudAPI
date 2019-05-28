from pytest import fixture

from .model import Activity
from .schema import ActivitySchema
from .interface import ActivityInterface

import time


@fixture
def schema() -> ActivitySchema:
    return ActivitySchema()


def test_activitySchema_create(schema: ActivitySchema):
    assert schema


def test_activitySchema_works(schema: ActivitySchema):
    params: ActivityInterface = schema.load({
        'activityName': 'test activity',
        'activityDescription': 'Test Description!',
        'activityTime': 346267,
        'activityLocation': 'Edinburgh'
    }).data

    activity = Activity(**params)

    assert activity.name == 'test activity'
    assert activity.description == 'Test Description!'
    assert activity.activity_time == 346267
    assert activity.location == 'Edinburgh'