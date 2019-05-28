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
    '''Users'''

    @responds(schema=UserSchema, many=True)
    def get(self) -> List[User]:
        '''Get all users'''

        return UserService.get_all()

    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def post(self) -> User:
        '''Create a Single user'''

        return UserService.create(request.parsed_obj)


@api.route('/<int:userId>')
@api.param('userId', 'user database ID')
class UserIdResource(Resource):
    @responds(schema=UserSchema)
    def get(self, user_id: int) -> User:
        '''Get Single user'''

        return UserService.get_by_id(user_id)

    def delete(self, user_id: int) -> Response:
        '''Delete Single user'''
        from flask import jsonify

        id = UserService.delete_by_id(user_id)
        return jsonify(dict(status='Success', id=id))

    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def put(self, user_id: int) -> User:
        '''Update Single user'''

        changes: UserInterface = request.parsed_obj
        user = UserService.get_by_id(user_id)
        return UserService.update(user, changes)
