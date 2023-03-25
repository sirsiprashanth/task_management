from modules.resource_managment import router as resource_managment_router
from modules.subscription_managment import router as subscription_managment_router
from modules.task_managment import router as task_managment_router
from modules.user_managment import router as user_managment_router
from modules.authentication import router as authentication_router


class ConfigureRoutes():
    def __init__(app):
        app.include_router(authentication_router.router,
                           tags=["Authentication"])
        app.include_router(resource_managment_router.router,
                           tags=["Resource Managment"])
        app.include_router(subscription_managment_router.router,
                           tags=["Subscription Managment"])
        app.include_router(task_managment_router.router,
                           tags=["Task Managment"])
        app.include_router(user_managment_router.router,
                           tags=["User Managment"])
