# app/widget/__init__.py

from .model import Activity
from .schema import ActivitySchema
BASE_ROUTE = 'activity'


def register_routes(api, app, root='api'):
    from .controller import api as activity_api

    api.add_namespace(activity_api, path=f'/{root}/{BASE_ROUTE}')