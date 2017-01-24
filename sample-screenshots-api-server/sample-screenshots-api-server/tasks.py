import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import hashlib
from subprocess import call

import logging
from django.db import connection
from django.conf import settings
import os
# import reversion
from django.db import models
from django.db import transaction
import simplejson as json
from .models import Screenshot
from time import sleep

logger = logging.getLogger(__name__)



def create_screenshot(url):
    print("does server exist?")
    try:
        response = urllib.request.urlopen(url)
    except:  #you can specify type of Exception also
        print("error")
        screenshot = Screenshot.objects.filter(url=url).last()
        screenshot.status = 'no server'
        screenshot.save()
        return

    print("calling create_screenshot")
    # TODO: call remotely, and pull screenshot off of windows
    browser = webdriver.Remote(
        command_executor='http://FQDN_OF_SELENIUM_HUB:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    

    browser.get(url)
    m = hashlib.md5()
    m.update(url.encode('utf-8'))
    browser.get_screenshot_as_file(str(m.hexdigest()) + '.png')
    # sleep(1)
    browser.close()
    try:
        print("++++ quitting browser ++++")
        browser.quit()
    except:
        print("cannot quit browser cleanly")
        
    browser = None
              
    print("image upload...")
    call(["s3cmd", "-P", "put", str(m.hexdigest()) + '.png', "s3://com.apis.screenshots/"])
    screenshot = Screenshot.objects.filter(url=url).last()
    screenshot.status = 'complete'
    screenshot.image_url = 'http://com.apis.screenshots.s3.amazonaws.com/' + str(m.hexdigest()) + '.png'
    screenshot.save()
    call(["rm", "-f", str(m.hexdigest()) + '.png'])
    print("exiting job")


