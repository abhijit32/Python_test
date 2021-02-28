import requests
from cachetools import cached,TTLCache

app_id = 'f54f1ad905b348e5bc2598af1d616707'
endpoint = 'https://openexchangerates.org/api'

class OpenExchangeClient:

    def __init__(self):
        self.app_id = app_id
        self.endpoint = endpoint
         
    @cached(cache=TTLCache(maxsize=2,ttl=900))
    def latest(self):
        return requests.get(f"{self.endpoint}/latest.json?app_id={self.app_id}").json()
