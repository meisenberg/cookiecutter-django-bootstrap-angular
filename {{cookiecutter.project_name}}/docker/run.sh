#!/bin/bash
IMAGE=python:2.7.9

if [ "$(whoami)" != "root" ]; then
    echo "Running docker..."
	docker run -it \
       -p 127.0.0.1:8000:8000 \
       -v $PWD:/var/www/app \
       -v $HOME/eggs:/var/www/app/eggs \
       $IMAGE \
       sh /var/www/app/docker/run.sh $@
    exit $?
fi;

cd /var/www/app
if ! grep /var/www/app bin/buildout > /dev/null; then
    echo "Building app..."
    python bootstrap.py
    python ./bin/buildout buildout:parts+=test
fi

if ! [ -f db.dat ]; then
    echo "Initialize db..."
    bin/django-manage syncdb --noinput
    bin/django-manage createsuperuser --noinput --username admin --email admin@example.com 2>/dev/null|| true
fi

! [ -d /var/www/app/static ] && bin/django-manage collectstatic --noinput

export PATH=$PATH:$PWD/bin

echo "$@"
exec $@

