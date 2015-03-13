# -*- coding: utf-8 -*-
from {{cookiecutter.project_name}}.settings import *  # NOQA

DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': 'test.db'}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
