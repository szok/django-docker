#!/bin/bash
set -e

apt-get update

apt-get install -y --force-yes \
    libpq-dev \
    python3.4 \
    python3.4-dev \
    python3-pip
