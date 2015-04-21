#!/bin/bash
set -e

if ! grep $(which python) $BUILDOUT > /dev/null; then
    echo "Building app..."
    python bootstrap.py
    python $BUILDOUT $BUILDOUT_OPTIONS
fi

if ! [ -f db.dat ]; then
    echo "Initialize db..."
    bin/django-manage syncdb --noinput
    bin/django-manage createsuperuser --noinput --username admin --email admin@example.com 2>/dev/null|| true
fi

if ! [ -d $APP/static ]; then
   bin/gulp concat
   bin/django-manage collectstatic --noinput
fi

exec $@

