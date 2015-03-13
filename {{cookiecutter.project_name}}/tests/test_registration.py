# -*- coding: utf-8 -*-


def test_register(app, mails):
    resp = app.get('/')
    resp = resp.click('Register')
    form = resp.forms['register']
    form['username'] = 'user'
    form['email'] = 'user@example.com'
    form['password1'] = 'passwd'
    form['password2'] = 'passwd'
    resp = form.submit()

    # check email
    assert len(mails) == 1
    mail = str(mails[0].message())

    # extract confirmation link
    url = [l for l in mail.split() if l.startswith('http')][0]

    # confirm
    resp = app.get(url.split('example.com', 1)[1]).follow()
    resp.mustcontain('Your account is now activated.')

    # login
    resp = resp.click('Log in')
    form = resp.forms['login']
    form['username'] = 'user'
    form['password'] = 'passwd'
    resp = form.submit().follow()
    resp.mustcontain('Log out')
