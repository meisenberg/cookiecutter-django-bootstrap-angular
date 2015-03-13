# -*- coding: utf-8 -*-


def test_home_page(app):
    resp = app.get('/')
    resp.mustcontain('<div class="container">')
    resp.mustcontain(no='Hello World !')


def test_browser_home_page(browser):
    browser.get('/')
    browser.mustcontain('<div class="container">')
    browser.wait_for_element(timeout=3, id_='claim')
    browser.mustcontain('Hello World !')
