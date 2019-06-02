from flask import request
from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import UserSchema
from .service import UserService
from .model import User
from .interface import UserInterface

api = Namespace('User', description='Account Management Endpoint')


@api.route('/')
class UserResource(Resource):
    """Users"""

    @responds(schema=UserSchema, many=True)
    def get(self) -> List[User]:
        """Get all users"""

        return UserService.get_all()

    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def post(self) -> User:
        """Create a Single user"""

        return UserService.create(request.parsed_obj)


@api.route('/<string:userUUID>')
@api.param('userUUID', 'User database UUID')
class UserUUIDResource(Resource):
    @responds(schema=UserSchema)
    def get(self, userUUID: str) -> User:
        """Get Single user"""

        return UserService.get_by_uuid(userUUID)

    def delete(self, userUUID: str) -> Response:
        """Delete Single user"""
        from flask import jsonify

        id = UserService.delete_by_uuid(userUUID)
        return jsonify(dict(status='Success', userUUID=userUUID))

    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def put(self, userUUID: str) -> User:
        """Update Single user"""

        changes: UserInterface = request.parsed_obj
        user = UserService.get_by_uuid(userUUID)
        return UserService.update(user, changes)
