# -*- coding: utf-8 -*-


def test_home_page(app):
    resp = app.get('/')
    resp.mustcontain('<div class="container">')
