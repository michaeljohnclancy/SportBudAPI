from marshmallow import fields, Schema, pre_load, post_dump
from datetime import datetime


class ActivitySchema(Schema):
    """Activity schema"""

    # Read-only for uuid
    activityUUID = fields.UUID(attribute='uuid', dump_only=True)
    activityName = fields.String(attribute='name')
    activityDescription = fields.String(attribute='description')
    activityTime = fields.DateTime(attribute='activity_time')
    activityLocation = fields.String(attribute='location')


