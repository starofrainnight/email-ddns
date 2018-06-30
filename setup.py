#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as readme_file, \
        open('HISTORY.rst', encoding='utf-8') as history_file:
    long_description = (readme_file.read() + "\n\n" + history_file.read())

install_requires = [
    'click>=6.0',
    'ipgetter',
    'attrdict',
]

setup_requires = [
    'pytest-runner',
]

tests_requires = [
    'pytest',
]

setup(
    name='email-ddns',
    version='0.0.2',
    description=("A DDNS server/client that only rely on free services (email, "
                 "outer ip getter)"),
    long_description=long_description,
    author="Hong-She Liang",
    author_email='starofrainnight@gmail.com',
    url='https://github.com/starofrainnight/email-ddns',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'email-ddns=emailddns.__main__:main'
        ]
    },
    include_package_data=True,
    install_requires=install_requires,
    license="GNU Affero General Public License v3",
    zip_safe=False,
    keywords='emailddns,email-ddns',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=tests_requires,
    setup_requires=setup_requires,
)
