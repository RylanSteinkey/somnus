from setuptools import setup

setup(
    name = 'somnus',
    version = '0.0.1',
    packages = ['somnus'],
    entry_points = {
        'console_scripts': [
            'somnus = somnus.__main__:main'
        ]
    })
