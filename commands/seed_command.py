from flask_script import Command

from app import db
from app.activity import Activity

import datetime
from uuid import uuid4


def seed_things():
    classes = [Activity]
    for klass in classes:
        seed_thing(klass)


def seed_thing(cls):
    things = [
        {
            "uuid": uuid4(),
            "name": "Test",
            "description": "TestDesc",
            "activity_time": datetime.datetime(2019, 5, 1),
            "location": "Edinburgh"
        },
        {
            "uuid": uuid4(),
            "name": "Test",
            "description": "TestDesc",
            "activity_time": datetime.datetime(2019, 5, 1),
            "location": "Edinburgh"
        },
        {
            "uuid": uuid4(),
            "name": "Test",
            "description": "TestDesc",
            "activity_time": datetime.datetime(2019, 5, 1),
            "location": "Edinburgh"
        }]
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