from app import db
from sqlalchemy_utils import UUIDType

# Many-to-many relationship association table between and activity and a user.
participation = db.Table('participation',
                         db.Column('activity_uuid',
                                   UUIDType,
                                   db.ForeignKey('activities.uuid')),
                         db.Column('user_uuid',
                                   UUIDType,
                                   db.ForeignKey('users.uuid'))
                         )
