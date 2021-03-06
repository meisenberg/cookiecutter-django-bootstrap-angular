================================================
{{cookiecutter.project_name}}
================================================

Bootstrapping
=============

For development purpose::

    $ python2.7 bootstrap.py
    $ bin/buildout buildout:parts+=test
    $ bin/gulp concat

For deployment purpose::

    $ python2.7 bootstrap.py
    $ bin/buildout
    $ bin/gulp concat

Serving your application
========================

You can launch a dev server using::

    $ bin/django-serve

Or with gulp if you working on css/javascript resources::

    $ bin/gulp watch server

Using docker-compose for development
====================================

You'll need to install https://docs.docker.com/compose/

Using mysql::

    $ docker-compose up mysql
    $ docker-compose run --service-ports web

With sqlite::

    $ docker-compose run --service-ports --no-deps web

You can also launch a specific command::

    $ docker-compose run --service-ports web gulp watch server

Running tests::

    $ docker-compose run --service-ports web tox

Building a docker image
=======================

Just run::

   $ docker build -t {{cookiecutter.project_name}} .
