#!/bin/bash
set -e

if ! [ -z $DB_PORT ]; then
    BUILDOUT_OPTIONS="$BUILDOUT_OPTIONS eggs:eggs+=mysqlclient"
    BUILDOUT_OPTIONS="$BUILDOUT_OPTIONS test:eggs+=mysqlclient"
fi

if ! grep $(which python) $BUILDOUT > /dev/null; then
    echo "Building app... $BUILDOUT_OPTIONS"
    python bootstrap.py
    python $BUILDOUT $BUILDOUT_OPTIONS
fi

env

if ! [ -z $DB_PORT ]; then
    echo "Initialize db..."
    bin/django-manage migrate --noinput
    bin/django-manage createsuperuser --noinput --username admin --email admin@example.com 2>/dev/null|| true
else
    if ! [ -f db.dat ]; then
        echo "Initialize db..."
        bin/django-manage migrate --noinput
        bin/django-manage createsuperuser --noinput --username admin --email admin@example.com 2>/dev/null|| true
    fi
fi

if ! [ -d static ]; then
   bin/gulp concat
   bin/django-manage collectstatic --noinput
fi

which virtualenv || pip install virtualenv

exec $@

