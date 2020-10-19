from uuid import uuid4

from sanic.views import HTTPMethodView
from sanic.response import json as jsonify

from service.v1.common.utils import success_response
from service.v1.common.errors import (error_missing_request_params)


class UserHandlerView(HTTPMethodView):

    @staticmethod
    async def get(request):
        """查询用户"""
        _user_id = request.args.get('user_id')

        if _user_id is None:
            return jsonify(error_missing_request_params())

        resp_data = dict(
            id=1,
            uuid=uuid4().hex,
            user_name='王五',
            user_email='ww@test.sanic.com'
        )

        return jsonify(success_response(resp_data))

    @staticmethod
    async def post(request):
        """新增用户"""
        pass

    @staticmethod
    async def patch(request):
        """修改用户"""
        pass

    @staticmethod
    async def put(request):
        """替换用户"""
        pass

    @staticmethod
    async def delete(request):
        """删除用户"""
        pass
