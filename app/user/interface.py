from mypy_extensions import TypedDict

from uuid import UUID


class UserInterface(TypedDict, total=False):

    uuid: UUID
    username: str
    password: str
    email: str