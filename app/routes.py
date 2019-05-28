def register_routes(api, app, root='api'):
    from app.user import register_routes as attach_user_endpoints

    attach_user_endpoints(api, app)
