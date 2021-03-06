#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os


def run(cmd):
    p = subprocess.Popen(cmd, shell=True)
    p.wait()
    if p.returncode:
        sys.exit(p.returncode)

if not os.path.isfile('.installed.cfg'):
    print('bootstraping project using %s...' % sys.executable)
    run('%s bootstrap.py' % sys.executable)
    print('running bin/buildout...')
    run('bin/buildout buildout:parts+=test')
    print('running bin/gulp concat...')
    run('bin/gulp concat')
    print('running bin/gulp less...')
    run('bin/gulp less')
