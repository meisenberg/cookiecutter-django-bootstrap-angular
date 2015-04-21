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

Using docker-compose
====================

You'll need to install https://docs.docker.com/compose/

Just run::

    $ docker-compose run --service-ports web
