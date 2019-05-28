from marshmallow import fields, Schema


class ActivitySchema(Schema):
    '''Activity schema'''

    activityName = fields.String(attribute='name')
    activityDescription = fields.String(attribute='description')
    activityTime = fields.Float(attribute='activity_time')
    activityLocation = fields.String(attribute='location')
