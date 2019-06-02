from pytest import fixture
from .model import Activity

from flask_sqlalchemy import SQLAlchemy
from app.test.fixtures import app, db  # noqa

import datetime

import uuid


test_uuid = uuid.uuid4()


@fixture
def activity() -> Activity:
    return Activity(
        name='Test Activity', description='An easy test activity!', activity_time=datetime.datetime.now(), location='test city!'
    )

def test_activity_create(activity: Activity):
    assert activity

def test_activity_retrieve(activity: Activity, db: SQLAlchemy):  # noqa
    db.session.add(activity)
    db.session.commit()
    s = Activity.query.first()
    assert s.__dict__ == activity.__dict__
