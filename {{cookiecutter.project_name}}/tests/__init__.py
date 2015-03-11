# -*- coding: utf-8 -*-
import os

os.environ['DJANGO_SETTINGS_MODULE'] = '{{cookiecutter.project_name}}.settings'

import django  # NOQA
django.setup()
