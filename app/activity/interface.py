from mypy_extensions import TypedDict
from datetime import datetime
import time

from uuid import UUID


class ActivityInterface(TypedDict):
    """ActivityInterface: Defines what is required and expected
        in the creation of an Activity model."""

    uuid: UUID
    name: str
    description: str
    activity_time: datetime
    location: str
