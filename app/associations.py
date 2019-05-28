from app import db
from passlib.context import CryptContext

# Many-to-many relationship association table between and activity and a user.
participation = db.Table('participation',
    db.Column('activity_id', db.Integer, db.ForeignKey('activities.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)