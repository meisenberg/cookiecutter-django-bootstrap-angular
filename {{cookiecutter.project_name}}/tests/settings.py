# -*- coding: utf-8 -*-
from {{cookiecutter.project_name}}.settings import *

DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': 'test.db'}
