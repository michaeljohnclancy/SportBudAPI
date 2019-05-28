from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from .service import ActivityService
from .schema import ActivitySchema
from .model import Activity
from .interface import ActivityInterface
from . import BASE_ROUTE


def make_new_activity(id: int = 123, name: str = 'Test Activity', description: str = 'TestPassword', activity_time: float = 12345, location: str = 'Edinburgh') -> Activity:
    return Activity(
        id=id, name=name, description=description,
        activity_time=activity_time, location=location
    )

class TestActivityResource:
    @patch.object(ActivityService, 'get_all',
                  lambda: [
                      make_new_activity(),
                      make_new_activity(id=456)])

    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(f'/api/{BASE_ROUTE}',
                                 follow_redirects=True).get_json()
            expected = ActivitySchema(many=True).dump(
                [make_new_activity(),
                 make_new_activity(id=456)]
            ).data
            for r in results:
                assert r in expected
