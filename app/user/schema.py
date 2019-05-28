from marshmallow import fields, Schema


class UserSchema(Schema):
    '''User schema'''

    id = fields.Integer(attribute='user_id')
    username = fields.String(attribute='username')
    password = fields.String(attribute='password')
    email = fields.String(attribute='email')