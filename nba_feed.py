import json
import pdb
import requests
from base64 import b64encode
from hashlib import sha256
from platform import platform, python_version
from hmac import new
from time import time

api_base_url='https://api.mysportsfeed.com/v2.0/pull/nba'
api_key='1c7c50f6-971f-4afe-a8f7-a20b73'

class Client:
    def __init__(self, api_base_url, api_key):
        self.api_base_url = api_base_url
        self.api_key = api_key

    def set_headers(self, nonce=None):
        if not nonce:
            nonce = int(time())
        with open('mysportsfeed_credentials') as file:
            credentials = [x.strip().split(':') for x in file.readlines()]

        password = credentials[0][1]
        basicAuth = self.api_key + ":" + password
        encryptedAuth = b64encode(new(basicAuth.encode(), msg=str(nonce).encode(), digestmod=sha256).digest())
        pdb.set_trace()
        return {'Authorization': encryptedAuth}


client = Client(api_base_url, api_key)
client.set_headers()
