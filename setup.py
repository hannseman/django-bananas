#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages

here = path.dirname(path.abspath(__file__))

# Get the long description from the relevant file
long_description = None

try:
    with open(path.join(here, "README.rst"), encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    pass


setup(
    name="django-bananas",
    description="Django Bananas - Django extensions the monkey way",
    long_description=long_description,
    url="https://github.com/5monkeys/django-bananas",
    version=__import__("bananas").__version__,
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=["tests", "_*", "example"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    tests_require=["detox", "coverage"],
    test_suite="runtests.main",
)

