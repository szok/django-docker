#!/bin/bash
cd $BLOG_DIR
python manage.py migrate
python manage.py loaddata blog/blog/fixtures/initial_data.json
