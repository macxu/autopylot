from framework.integration.user.UserServiceClient import UserServiceClient


class UserService:
    def __init__(self):
        self._service_client = UserServiceClient()

    def get_users(self):
        return self._service_client.get()

    def get_user(self, user_id):
        return self._service_client.get(user_id)

    def get_users_by_name(self, user_name):
        return self._service_client.get(1)
