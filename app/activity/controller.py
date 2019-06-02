from flask import request
from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import ActivitySchema
from .service import ActivityService
from .model import Activity
from .interface import ActivityInterface

api = Namespace('Activity', description='Activity Management Endpoint')


@api.route('/')
class ActivityResource(Resource):
    """Activities"""

    @responds(schema=ActivitySchema, many=True)
    def get(self) -> List[Activity]:
        """Get all activities"""

        return ActivityService.get_all()

    @accepts(schema=ActivitySchema, api=api)
    @responds(schema=ActivitySchema)
    def post(self) -> Activity:
        """Create a Single activity"""

        return ActivityService.create(request.parsed_obj)


@api.route('/<string:activityUUID>')
@api.param('activityUUID', 'Activity database UUID')
class ActivityIdResource(Resource):
    @responds(schema=ActivitySchema)
    def get(self, activityUUID: str) -> Activity:
        """Get Single activity"""

        return ActivityService.get_by_uuid(activityUUID)

    def delete(self, activityUUID: str) -> Response:
        """Delete Single activity"""
        from flask import jsonify

        uuid = ActivityService.delete_by_uuid(activityUUID)

        return jsonify(dict(status='Success', uuid=uuid))

    @accepts(schema=ActivitySchema, api=api)
    @responds(schema=ActivitySchema)
    def put(self, activityUUID: str) -> Activity:
        """Update Single activity"""

        changes: ActivityInterface = request.parsed_obj
        activity = ActivityService.get_by_uuid(activityUUID)
        return ActivityService.update(activity, changes)
