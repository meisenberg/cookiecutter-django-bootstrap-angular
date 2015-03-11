# -*- coding: utf-8 -*-
import os
import pytest
import django
import django_webtest
from django.test import utils
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
from django.contrib.auth.models import User

"""
Contains py.test fixtures
"""

django.setup()
wtm = django_webtest.WebTestMixin()


@pytest.fixture(scope='function')
def app(request, db):
    request.addfinalizer(wtm._unpatch_settings)
    wtm._patch_settings()
    wtm.renew_app()
    return wtm.app


@pytest.fixture(scope='function')
def admin(request, app):
    user = User.objects.create_user(username='cnoris',
                                    email='chuck@noris.com',
                                    password='passwd')
    return user
