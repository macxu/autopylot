from framework.integration.user.UserService import UserService


class TestResource:

    def __init__(self):
        self._user_service = UserService()

    @property
    def user_service(self):
        return self._user_service
