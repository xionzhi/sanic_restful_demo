from sanic import Blueprint

from service.v1.views.user_views import (UserHandlerView)
from service.v1.views.task_views import (TaskHandlerView)

# user
user_bp = Blueprint('user')
user_bp.add_route(UserHandlerView.as_view(), '/user')

# task
task_bp = Blueprint('task')
user_bp.add_route(TaskHandlerView.as_view(), '/task')


# group Blueprint
api_blueprint_v1 = Blueprint.group(user_bp, task_bp)
