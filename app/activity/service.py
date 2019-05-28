from app import db
from typing import List
from .model import Activity
from .interface import ActivityInterface

class ActivityService():

    @staticmethod
    def get_all() -> List[Activity]:
        return Activity.query.all()

    @staticmethod
    def get_by_id(id: int) -> Activity:
        return Activity.query.get(id)

    @staticmethod
    def update(activity: Activity, activity_change_updates: ActivityInterface) -> Activity:
        activity.update(activity_change_updates)
        db.session.commit()
        return activity

    @staticmethod
    def delete_by_id(id: int) -> List[int]:
        activity = Activity.query.filter(Activity.id == id).first()
        if not activity:
            return []
        db.session.delete(activity)
        db.session.commit()
        return [id]

    @staticmethod
    def create(new_attrs: ActivityInterface) -> Activity:
        new_activity = Activity(
            name=new_attrs['name'],
            description=new_attrs['description'],
            activity_time=new_attrs['activity_time'],
            location=new_attrs['location']
        )

        db.session.add(new_activity)
        db.session.commit()

        return new_activity