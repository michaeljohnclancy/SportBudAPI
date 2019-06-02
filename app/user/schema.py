from marshmallow import fields, Schema


class UserSchema(Schema):
    """User schema"""

    # Read-only for UUID
    userUUID = fields.UUID(attribute='uuid', dump_only=True)
    username = fields.String(attribute='username')
    # Write-only for password
    password = fields.String(attribute='password', load_only=True)
    email = fields.String(attribute='email')
