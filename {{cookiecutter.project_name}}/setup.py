from setuptools import find_packages
from setuptools import setup
import sys
import os

version = '{{cookiecutter.version}}'

install_requires = [
    'Sphinx',
    'Django>=1.7',
    'DjangoDevKit',
    'django-registration-redux',
    'django-autoslug',
    'django-bootstrap3',
]

test_requires = [
    'webdriverwrapper',
    'django-webtest',
    'coverage',
    'flake8',
    'pytest-django',
    'pytest-cov',
    'pytest',
    'aiowsgi',
]


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

if 'dev' in sys.argv:
    for filename in ('.installed.cfg', '.coverage'):
        if os.path.isfile(filename):
            os.remove(filename)


setup(
    name='{{cookiecutter.project_name}}',
    version=version,
    description="{{cookiecutter.description}}",
    long_description=read('README.rst'),
    classifiers=[],
    keywords='',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    url='',
    license='',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'test': test_requires,
    },
    zip_safe=False,
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    """,
)
