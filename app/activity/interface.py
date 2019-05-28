from mypy_extensions import TypedDict
import time

class ActivityInterface(TypedDict):
    '''ActivityInterface: Defines what is required and expected
        in the creation of an Activity model.'''

    name: str
    description: str
    activity_time: float
    location: str