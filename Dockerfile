FROM python:3.5
MAINTAINER mateusz@mkurek.com

# set UTF-8 locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# set paths
ENV BLOG_DIR=/home/blog

# TODO: user dir

ADD . $BLOG_DIR
WORKDIR $BLOG_DIR
RUN pip install -r requirements/production.txt

VOLUME /root/db

EXPOSE 22 8001
CMD python manage.py runserver 0.0.0.0:8001
