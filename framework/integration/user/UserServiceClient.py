import requests


class UserServiceClient:

    def __init__(self):
        self.url = 'https://jsonplaceholder.typicode.com/users'

    def get(self, user_id=None):
        url = self.url
        if user_id:
            url = url + '/' + str(user_id)
        return requests.get(url)