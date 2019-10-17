# apis
contains screenshot api endpoints

# Steps to set up:

# 1) Setup a selenium node / hub cluster
# 2) Run the code in this folder as a django app
# 3) configure FQDN_OF_SELENIUM_HUB in tasks.py
# 4) install s3cmd
# 5) To run the django app:
cd $DJANGO_APP_DIR; uwsgi --ini apis_uwsgi.ini
rq-dashboard
cd $DJANGO_APP_DIR; python manage.py rqworker screenshots

# /scripts
contains a sample scripts

seleniume-screenshot.py - serverless screenshot script that uses selenium
