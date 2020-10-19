#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "PyCrypto",
]

setup_requirements = [
    "setuptools",
]

test_requirements = [ ]

setup(
    author="Philippe Teuwen",
    author_email='phil@teuwen.org',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2 :: Only',
    ],
    description="PyCrypto.Cypher extensions",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='CryptoPlus',
    name='CryptoPlus',
    package_dir={'': 'src'},
    packages=find_packages("src"),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/doegox/python-cryptoplus',
    version='1.0.0',
    zip_safe=False,
)
