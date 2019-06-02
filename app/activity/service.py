from app import db
from typing import List
from .model import Activity
from .interface import ActivityInterface

from uuid import UUID, uuid4


class ActivityService:

    @staticmethod
    def get_all() -> List[Activity]:
        return Activity.query.all()

    @staticmethod
    def get_by_uuid(activity_uuid: UUID) -> Activity:
        return Activity.query.get(activity_uuid)

    @staticmethod
    def update(activity: Activity, activity_change_updates: ActivityInterface) -> Activity:
        activity.update(activity_change_updates)
        db.session.commit()
        return activity

    @staticmethod
    def delete_by_uuid(activity_uuid: UUID) -> List[UUID]:
        activity = Activity.query.filter(Activity.uuid == activity_uuid).first()
        if not activity:
            return []
        db.session.delete(activity)
        db.session.commit()
        return [activity_uuid]

    @staticmethod
    def create(new_attrs: ActivityInterface) -> Activity:
        new_activity = Activity(
            uuid=uuid4(),
            name=new_attrs['name'],
            description=new_attrs['description'],
            activity_time=new_attrs['activity_time'],
            location=new_attrs['location']
        )

        db.session.add(new_activity)
        db.session.commit()

        return new_activity