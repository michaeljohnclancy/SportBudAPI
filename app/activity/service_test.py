from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.test.fixtures import app, db  # noqa
from .model import Activity
from .service import ActivityService  # noqa
from .interface import ActivityInterface

from datetime import datetime
import uuid


def test_get_all(db: SQLAlchemy):
    test_activity1: Activity = Activity(uuid=uuid.uuid4(), name='Test Activity 1', description='An easy test activity!', activity_time=datetime.now(), location='test city!')
    test_activity2: Activity = Activity(uuid=uuid.uuid4(), name='Test Activity 2', description='An easy test activity!', activity_time=datetime.now(), location='test city!')

    print(test_activity1)
    print(test_activity2)
    db.session.add(test_activity1)
    db.session.add(test_activity2)
    db.session.commit()

    results: List[Activity] = ActivityService.get_all()

    assert len(results) == 2
    assert test_activity1 in results and test_activity2 in results


def test_update(db: SQLAlchemy):
    test_activity: Activity = Activity(uuid=uuid.uuid4(), name='Test Activity 1', description='An easy test activity!', activity_time=datetime.now(), location='test city!')

    db.session.add(test_activity)
    db.session.commit()
    updates: ActivityInterface = dict(description='This is an updated description!')

    ActivityService.update(test_activity, updates)

    result: Activity = Activity.query.get(test_activity.uuid)
    assert result.description == 'This is an updated description!'


def test_delete_by_uuid(db: SQLAlchemy):
    test_activity1: Activity = Activity(uuid=uuid.uuid4(), name='Test Activity 1', description='An easy test activity!',
                                        activity_time=datetime.now(), location='test city!')
    test_activity2: Activity = Activity(uuid=uuid.uuid4(), name='Test Activity 2', description='An easy test activity!',
                                        activity_time=datetime.now(), location='test city!')
    db.session.add(test_activity1)
    db.session.add(test_activity2)
    db.session.commit()

    ActivityService.delete_by_uuid(str(test_activity1.uuid))
    db.session.commit()

    results: List[Activity] = Activity.query.all()

    assert len(results) == 1
    assert test_activity1 not in results and test_activity2 in results


def test_create(db: SQLAlchemy):

    test_activity_interface: ActivityInterface = dict(name='Test Activity 1', description='An easy test activity!', activity_time=datetime(2019, 2, 1, 22, 1), location='test city!')
    ActivityService.create(test_activity_interface)

    results: List[Activity] = Activity.query.all()

    assert len(results) == 1

    for k in test_activity_interface.keys():
        assert getattr(results[0], k) == test_activity_interface[k]