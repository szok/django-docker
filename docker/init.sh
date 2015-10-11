#!/bin/bash
cd $BLOG_DIR
sleep 10  # give db some time to run
python manage.py migrate
python manage.py loaddata blog/blog/fixtures/initial_data.json
