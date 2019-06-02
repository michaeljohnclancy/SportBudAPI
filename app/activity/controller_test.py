from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app
from .service import ActivityService
from .schema import ActivitySchema
from .model import Activity
from .interface import ActivityInterface
from . import BASE_ROUTE

from uuid import uuid4, UUID

from datetime import datetime


def make_new_activity(uuid: UUID = uuid4(), name: str = 'Test Activity', description: str = 'TestPassword',
                      activity_time: datetime = datetime(2019, 3, 2, 4, 6, 3), location: str = 'Edinburgh') -> Activity:
    return Activity(
        uuid=uuid, name=name, description=description,
        activity_time=activity_time, location=location
    )


test_uuid = uuid4()


class TestActivityResource:

    @patch.object(ActivityService, 'get_all',
                  lambda: [
                      make_new_activity(uuid=test_uuid)])
    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(f'/api/{BASE_ROUTE}',
                                 follow_redirects=True).get_json()
            expected = ActivitySchema(many=True).dump(
                [make_new_activity(uuid=test_uuid)]
            ).data
            for r in results:
                assert r in expected

    @patch.object(ActivityService, 'create',
                  lambda create_request: Activity(**create_request))
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(activityName='Test Activity',
                           activityDescription='Test description',
                           activityTime='2019-02-01 22:01:03',
                           activityLocation='Edinburgh')
            result = client.post(f'/api/{BASE_ROUTE}/', json=payload).get_json()
            expected = ActivitySchema().dump(Activity(
                name=payload['activityName'],
                description=payload['activityDescription'],
                activity_time=datetime.strptime(payload['activityTime'], "%Y-%m-%d %H:%M:%S"),
                location=payload['activityLocation']
            )).data
            assert result == expected


def fake_update(activity: Activity, changes: ActivityInterface) -> Activity:
    # To fake an update, just return a new object
    updated_activity = Activity(uuid=activity.uuid,
                                name=changes['name'],
                                description=changes['description'],
                                activity_time=changes['activity_time'],
                                location=changes['location'])
    return updated_activity


class TestActivityUUIDResource:
    @patch.object(ActivityService, 'get_by_uuid',
                  lambda activity_uuid: make_new_activity(uuid=activity_uuid))
    def test_get(self, client: FlaskClient):
        with client:
            result = client.get(f'/api/{BASE_ROUTE}/{test_uuid}').get_json()
            expected = make_new_activity(uuid=test_uuid)
            assert result['activityUUID'] == str(expected.uuid)

    @patch.object(ActivityService, 'delete_by_uuid',
                  lambda activity_uuid: activity_uuid)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:

            result = client.delete(f'/api/{BASE_ROUTE}/{str(test_uuid)}').get_json()
            expected = dict(status='Success', uuid=str(test_uuid))
            assert result == expected

    @patch.object(ActivityService, 'get_by_uuid',
                  lambda activity_uuid: make_new_activity(uuid=activity_uuid))
    @patch.object(ActivityService, 'update', fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            activity_uuid = uuid4()
            result = client.put(f'/api/{BASE_ROUTE}/{str(activity_uuid)}',
                                json={'activityName': 'New Activity Name',
                                      'activityDescription': 'New Description!',
                                      'activityTime': '2019-02-01 22:01:00',
                                      'activityLocation': 'Edinburgh'}).get_json()
            expected = ActivitySchema().dump(
                Activity(uuid=activity_uuid, name='New Activity Name', description='New Description!',
                         activity_time=datetime(2019, 2, 1, 22, 1), location='Edinburgh')).data
            assert result == expected
