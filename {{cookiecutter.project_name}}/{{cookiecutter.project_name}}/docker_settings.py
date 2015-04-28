# -*- coding: utf-8 -*-
import os

if 'DB_PORT' in os.environ:
    DB_HOST, DB_PORT = os.environ['DB_PORT'].split('://', 1)[1].split(':')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '{{cookiecutter.project_name}}',
            'USER': '{{cookiecutter.project_name}}',
            'PASSWORD': 'passwd',
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }
