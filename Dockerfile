FROM python:3.5
# FROM python:3.5
MAINTAINER mateusz@mkurek.com

# set paths
ENV BLOG_DIR=/home/blog

# TODO: user dir

ADD . $BLOG_DIR
WORKDIR $BLOG_DIR
RUN pip install -r requirements/production.txt

VOLUME /root/db

EXPOSE 22 8001
CMD python manage.py runserver 0.0.0.0:8001
