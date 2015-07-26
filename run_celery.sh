#!/bin/sh
 
cd smarthousing
# run Celery worker for our project smarthousing with Celery configuration stored in Celeryconf
su -m ujjwal -c "celery -A smarthousing worker -l info"
#su -m myuser -c "celery worker -A myproject.celeryconf -Q default -n default@%h"