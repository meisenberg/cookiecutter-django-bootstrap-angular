# -*- coding: utf-8 -*-
import pytest
import django_webtest
from django.contrib.auth.models import User

"""
Contains py.test fixtures
"""

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
