#!/usr/bin/env python

from future.standard_library import install_aliases
install_aliases()

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import json

import requests
from requests.auth import HTTPBasicAuth

import os

use_environment_variables = None

try:
    from django.conf import settings
except ImportError:
    use_environment_variables = True

class Builder:
    user = None
    password = None
    api_server_url = None

    if use_environment_variables == True:
        try:
            user = os.environ['SCREENSHOT_USER']
            password = os.environ.get('SCREENSHOT_PASSWORD') # use get to return None, because password might be blank
            api_server_url = os.environ['SCREENSHOT_SERVER_URL']
        except:
            print("configure environment variables for screenshots")
    else: 
        try:
            user = settings.SCREENSHOT_USER
            password = settings.SCREENSHOT_PASSWORD # use get to return None, because password might be blank
            api_server_url = settings.SCREENSHOT_SERVER_URL
        except:
            print("configure django settings variables")
        

    def __init__(self, url):
        self.url = url
        self.id = None
        self.image_url = None

    def capture(self):
        search_results = json.loads(self.search())
        count = len(search_results['results'])
        if count > 0:
            self.id = search_results['results'][count - 1]['id']
            text = self.info()
            if json.loads(text)['status'] != 'complete':
                self.screenshot()
        else:
            text = self.screenshot()
            self.id = json.loads(text)['id']
        return text

    def screenshot(self):
        r = requests.post("{}/screenshots/".format(self.api_server_url), json={"url": self.url}, auth=HTTPBasicAuth(self.user,self.password))        
        text = r.text
        self.id = json.loads(r.text)['id']
        return r.text

    def info(self):
        r = requests.get("{}/screenshots/{}".format(self.api_server_url,self.id), auth=HTTPBasicAuth(self.user,self.password))
        self.image_url = json.loads(r.text)['image_url']
        return r.text

    def search(self):
        encoded_url = quote_plus(self.url)
        print("searching for {}".format(encoded_url))
        r = requests.get("{}/screenshot_search/{}/".format(self.api_server_url,encoded_url), auth=HTTPBasicAuth(self.user,self.password))
        return r.text

