# -*- coding: utf-8 -*-
import pytest
import threading
import aiowsgi
from os import path
from functools import partial
import webdriverwrapper
import django_webtest
from django.contrib.auth.models import User
from django.core import mail
from webtest.http import get_free_port

"""
Contains py.test fixtures
"""


class Browser(webdriverwrapper.PhantomJS):

    def get(self, path):
        return super(Browser, self).get(self.url + path)

    def login(self, username, password='password'):
        self.get('/accounts/login/')
        form = self.wait_for_element(timeout=2, id_='login')
        form.fill_out_and_submit({
            'username': username,
            'password': password,
        })
        self.mustcontain(username)

    def mustcontain(self, *texts):
        for text in texts:
            if text not in self.page_source:
                print(self.page_source)
            assert text in self.page_source


wtm = django_webtest.WebTestMixin()


@pytest.fixture(scope='function')
def app(request, db):
    request.addfinalizer(wtm._unpatch_settings)
    wtm._patch_settings()
    wtm.renew_app()
    return wtm.app


class Server(threading.Thread):

    def __init__(self, app):
        super(Server, self).__init__()
        self.app = app
        _, self.port = get_free_port()
        self.url = 'http://127.0.0.1:%s' % self.port
        self.loop = aiowsgi.asyncio.new_event_loop()

    def run(self):
        aiowsgi.asyncio.set_event_loop(self.loop)
        server = aiowsgi.create_server(
            self.app, loop=self.loop, port=self.port)
        server.run()

    def stop(self):
        self.loop.stop()


@pytest.fixture(scope='function')
def browser(request, app):
    server = Server(app.app)
    server.start()
    # travis
    paths = (
        path.join(
            path.dirname(path.dirname(__file__)),
            'node_modules/karma-phantomjs-launcher/'
            'node_modules/phantomjs/bin/phantomjs'
        ),
        '/usr/local/phantomjs/bin/phantomjs',
        '/usr/bin/phantomjs',
    )
    for p in paths:
        if path.isfile(p):
            break
    if not path.isfile(p):
        raise OSError('Not able to find phantomjs binary')
    browser = Browser(executable_path=p)
    browser.url = server.url
    request.addfinalizer(browser.quit)
    request.addfinalizer(server.stop)
    return browser


@pytest.fixture(scope='function')
def mails(request):
    mail.outbox = []
    request.addfinalizer(partial(setattr, mail, 'outbox', []))
    return mail.outbox


@pytest.fixture(scope='function')
def admin(db, request):
    user = User.objects.create_user(username='cnorris',
                                    email='chuck@norris.com',
                                    password='passwd')
    return user
