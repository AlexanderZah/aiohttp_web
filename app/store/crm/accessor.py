from typing import Optional
import typing

from app.crm.models import User

if typing.TYPE_CHECKING:
    from app.web.app import Application


class CrmAccessor:
    def __init__(self):
        self.app: Optional[Application] = None

    async def connect(self, app: 'Application'):
        self.app = app
        self.app.database['users'] = []
        print('connected to db')

    async def disconnect(self, app: 'Application'):
        self.app = None
        print('disconnected db')

    def add_user(self, user: User):
        self.app.database['users'].append(user)

    async def list_users(self):
        return self.app.database.get('users')

    async def get_user(self, user_id):
        users = await self.app.database.get('users')
        for user in users:
            if user._id == user_id:
                return user
        return None
