#!/usr/bin/env python3

import os

from setuptools import find_packages, setup

setup(
    name="Simple Timeslot",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={'':'src'},
    include_package_data=True,
    scripts=['src/manage.py'],
    data_files= [("lib/simple-timeslot-{}".format(root), [os.path.join(root, f) for f in files])
                 for root, dirs, files in os.walk('src/vocgui/templates/')] +
                [("lib/simple-timeslot-{}".format(root), [os.path.join(root, f) for f in files])
                 for root, dirs, files in os.walk('src/vocgui/static/')] +
                [('usr/lib/systemd/system/', ['simple-timeslot.service'])],
    install_requires=[
        "Django>=2.2.9",
        "",
        ""
    ],
    extras_require={
        "dev": [
            "packaging",
            "pylint",
            "pylint-django",
            "pylint_runner",
        ]
    },
    author="Tür an Tür Digitalfabrik gGmbH",
    author_email="info@integreat-app.de",
    description="Simple Timeslot booking",
    license="GPL-2.0-or-later",
    keywords="Simple TImeslot",
    url="http://github.com/digitalfabrik/simple-timeslot",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)

