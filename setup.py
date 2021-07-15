#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from jitsu_python_example.telemetry import JitsuApi

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Vladimir Klimontovich",
    author_email='hello@jitsu.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Analytics for your python lib based on Jitsu example",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='jitsu_python_example',
    name='jitsu_python_example',
    packages=find_packages(include=['jitsu_python_example', 'jitsu_python_example.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jitsucom/jitsu-python-example',
    version='0.0.1',
    zip_safe=False,
)

# JitsuApi sends install event on every pip install
JitsuApi().send_event({
    'event_type': 'install'
})

