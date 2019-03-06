#!/usr/bin/env python3

from setuptools import (
    setup,
    find_packages,
)

setup(
    name="{{cookiecutter.project_slug}}",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask"
    ],
    package_data={
        "{{cookiecutter.project_slug}}": [
            "templates/*/*",
            "assets/static/*/*"
        ]
    },
)
