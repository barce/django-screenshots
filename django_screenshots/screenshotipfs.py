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

import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import hashlib
import ipfshttpclient

use_environment_variables = None

try:
    from django.conf import settings
except ImportError:
    use_environment_variables = True

class ScreenShotIpfs:
    def __init__(self, url):
        self.url = url
        self.id = None
        self.image_url = None
        self.image_directory = '/tmp'
        self.image_file = None
        self.image_full_file_path = None
        self.ipfs_local = '/ip4/127.0.0.1/tcp/5001'
        self.ipfs_hash = None

    # This little function make screen size to maximum for better screenshot result
    def save_screenshot(self, driver, path):
        original_size = driver.get_window_size()
        required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(required_width, required_height)
        try:
            driver.find_element_by_tag_name('body').screenshot(path)  # Avoids scrollbar
        except Exception as e:
            print(e)
        driver.set_window_size(original_size['width'], original_size['height'])


    def capture(self):
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities['acceptSslCerts'] = True  # This is for accepting self signed SSl certificates.
        opts = Options()
        driver = webdriver.Firefox(options=opts, executable_path="/usr/local/bin/geckodriver")
        driver.capabilities = capabilities
        driver.get(self.url)

        m = hashlib.md5()
        m.update(self.url.encode('utf-8'))
        self.image_file = str(m.hexdigest()) + '.png'
        self.image_full_file_path = self.image_directory + '/' + self.image_file
        # Saving the screenshot
        self.save_screenshot(driver, self.image_full_file_path) 
        driver.close()

    def upload(self):
        client = ipfshttpclient.connect(self.ipfs_local)
        res = client.add(self.image_full_file_path)
        self.ipfs_hash = res['Hash']
        client.close()
        return self.ipfs_hash

    def get(self,ipfs_hash,image_file):
        client = ipfshttpclient.connect(self.ipfs_local)
        some_string = client.cat(ipfs_hash)
        with open(image_file, "wb") as file:
            file.write(some_string)
        client.close()
