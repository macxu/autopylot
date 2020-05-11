import requests


class QaRestClient:

    def get(self, url):
        return requests.get(url)

    def get_json(self, url):
        return self.get(url)