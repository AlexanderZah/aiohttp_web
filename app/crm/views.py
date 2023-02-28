import json
import uuid
from aiohttp.web_response import json_response

from app.web.app import View
from .models import User


class AddUserView(View):

    async def post(self):
        data = await self.request.json()
        user = User(email=data["email"], _id=uuid.uuid4())
        self.request.app.crm_accessor.add_user(user)
        return json_response({'status': 'ok'})


class ListUsersView(View):

    async def get(self):
        users = await self.request.app.crm_accessor.list_users()
        if users:
            raw_users = [{'email': user.email, '_id': str(user._id)}for user in users]
            return json_response(data={
                'users': raw_users
                })
        return json_response(data={
            'users': 'empty'
        })

