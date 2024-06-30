import requests


class DwebbleHttpClient(object):
    def __init__(self):
        self.session = requests.Session()
    
    def get(self, url):
        res = self.session.get(url)
        return res.json()["data"]