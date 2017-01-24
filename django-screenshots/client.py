#!/usr/bin/env python


import json
# import urllib.request

from requests.auth import HTTPBasicAuth

class Client:
    def __init__(self, url):
        self.url = url

    def get_image(self):
        return self.url
