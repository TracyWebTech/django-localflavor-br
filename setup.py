import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name = 'django-localflavor-br',
    version = '1.0',
    description = 'Country-specific Django helpers for Brazil.',
    long_description = README,
    author = 'Django Software Foundation',
    author_email = 'foundation@djangoproject.com',
    license='BSD',
    url = 'https://github.com/django/django-localflavor-br',
    packages = ['django_localflavor_br'],
    include_package_data = True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'Django>=1.4',
    ]
)
