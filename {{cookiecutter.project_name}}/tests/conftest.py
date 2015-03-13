# -*- coding: utf-8 -*-
import pytest
from functools import partial
import django_webtest
from django.contrib.auth.models import User
from django.core import mail

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
def mails(request):
    mail.outbox = []
    request.addfinalizer(partial(setattr, mail, 'outbox', []))
    return mail.outbox


@pytest.fixture(scope='function')
def admin(request, app):
    user = User.objects.create_user(username='cnorris',
                                    email='chuck@norris.com',
                                    password='passwd')
    return user
