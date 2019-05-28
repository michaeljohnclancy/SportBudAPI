from flask_script import Command

from app import db
from app.user import User



def seed_things():
    classes = [User]
    for klass in classes:
        seed_thing(klass)


def seed_thing(cls):
    things = [
        {
            'username': 'TestUser1',
            'password': 'TestPassword1',
            'email': 'TestEmail1@gmail.com'
        },
        {
            'username': 'TestUser2',
            'password': 'TestPassword2',
            'email': 'TestEmail2@gmail.com'
        },
        {
            'username': 'TestUser3',
            'password': 'TestPassword3',
            'email': 'TestEmail3@gmail.com'
        },
    ]
    db.session.bulk_insert_mappings(cls, things)

class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        if input('ARE YOU SURE YOU WANT TO DROP ALL TABLES AND RECREATE? (Y/N)\n'
                 ).lower() == 'y':
            print('Dropping tables...')
            db.drop_all()
            db.create_all()
            seed_things()
            db.session.commit()
            print('DB successfully seeded.')