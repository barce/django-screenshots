==================
django-screenshots
==================

DM me on github, or @barce on twitter, if
you want to see a working demo.

installation
===========================================
    pip install django-screenshots
    pip install requests

set values for using environment variables: 
===========================================
    export SCREENSHOT_USER=''
    export SCREENSHOT_PASSWORD=''
    export SCREENSHOT_SERVER_URL=''
    export SCREENSHOT_FORCE_ENV='1'


set values for using django settings: 
===========================================
    SCREENSHOT_USER=''
    SCREENSHOT_PASSWORD=''
    SCREENSHOT_SERVER_URL=''


Capture a screen shot and get the URL:
======================================
    from django_screenshots import Builder
    b = Builder('http://www.google.com/')
    b.capture()
    print(b.image_url)

Get info about a screen shot:
=============================
    from django_screenshots import Builder
    b = Builder('http://www.google.com/')
    print(b.info())

Search for a URL:
=================
    from django_dscreenshots import Builder
    b = Builder('http://www.google.com/')
    print(b.search())

IPFS local use and p2p storage:
===============================

1) https://github.com/mozilla/geckodriver/releases
2) download the latest for your OS, e.g. geckodriver-v0.26.0-macos.tar.gz
3) tar zxvf geckodriver-v0.26.0-macos.tar.gz
4) mv geckodriver /usr/local/bin/.
5) pip3 install selenium
6) brew install ipfs # mac os, or
6a) sudo apt-get install ipfs # linux
7) pip3 install ipfshttpclient
8) ipfs daemon
9) Use this code to try it out:
    from django_screenshots import ScreenShotIpfs
    import ipfshttpclient
    b = ScreenShotIpfs('https://www.reddit.com/')
    b.image_directory = './tests'
    b.capture()
    b.upload() 
    b.get(b.ipfs_hash, './tests/output.png')

For developers:
===============
    How to upload to pypi:
      python setup.py sdist register upload
      # python setup.py sdist
      # twine upload dist/*

