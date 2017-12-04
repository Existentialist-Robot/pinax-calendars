from setuptools import find_packages, setup

LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-calendars.svg
    :target: https://pypi.python.org/pypi/pinax-calendars/
===================
Pinax Notifications
===================
.. image:: https://img.shields.io/pypi/v/pinax-calendars.svg
    :target: https://pypi.python.org/pypi/pinax-calendars/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-calendars/
.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-calendars.svg
    :target: https://circleci.com/gh/pinax/pinax-calendars
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-calendars.svg
    :target: https://codecov.io/gh/pinax/pinax-calendars
.. image:: https://img.shields.io/github/contributors/pinax/pinax-calendars.svg
    :target: https://github.com/pinax/pinax-calendars/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-calendars.svg
    :target: https://github.com/pinax/pinax-calendars/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-calendars.svg
    :target: https://github.com/pinax/pinax-calendars/pulls?q=is%3Apr+is%3Aclosed
.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/

``pinax-calendars`` provides utilities for publishing events as a calendar.
 
Features
--------
* Good helpful stuff 

Supported Django and Python Versions
------------------------------------
* Django 1.8, 1.10, 1.11, and 2.0
* Python 2.7, 3.4, 3.5, and 3.6
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="Django utilities for publishing events as a calendar",
    name="pinax-calendars",
    long_description=LONG_DESCRIPTION,
    version="2.0.0",
    url="http://github.com/pinax/pinax-calendars/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pinax.calendars": [
            "templates/pinax/calendars/*"
        ]
    },
    install_requires=[
        "pytz"
    ],
    test_suite="runtests.runtests",
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
