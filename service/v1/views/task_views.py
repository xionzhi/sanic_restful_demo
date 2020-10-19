from uuid import uuid4

from sanic.views import HTTPMethodView
from sanic.response import json as jsonify

from service.v1.common.utils import success_response
from service.v1.common.errors import (error_missing_request_params)


class TaskHandlerView(HTTPMethodView):

    @staticmethod
    async def get(request):
        """查询任务"""
        _task_id = request.args.get('task_id')

        if _task_id is None:
            return jsonify(error_missing_request_params())

        resp_data = dict(
            id=1,
            uuid=uuid4().hex,
            task_name='王五',
            task_info='task task task task'
        )

        return jsonify(success_response(resp_data))

    @staticmethod
    async def post(request):
        """新增任务"""
        pass

    @staticmethod
    async def patch(request):
        """修改任务"""
        pass

    @staticmethod
    async def put(request):
        """替换任务"""
        pass

    @staticmethod
    async def delete(request):
        """删除任务"""
        pass
