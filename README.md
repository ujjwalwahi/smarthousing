# Dockerfile - build
`docker-compose build`


# docker container - create or recreate 
`docker-compose up`

# start project
`docker-compose run web django-admin.py startproject smarthousing smarthousing/`

# Start django
`sudo docker-compose run web`

# ip address of docker container
`docker inspect 72c652097dc7`

# start project as non root user
`docker-compose run web su -m ujjwal -c "django-admin.py startproject smarthousing smarthousing/"`

# start django server
`docker-compose run web`

# create new django app
`docker-compose run web su -m ujjwal -c  "python smarthousing/manage.py startapp requestlogs  smarthousing/apps/requestlogs"`
