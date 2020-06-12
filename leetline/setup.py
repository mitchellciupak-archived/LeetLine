from setuptools import setup
setup(
    name = 'leetline',
    version = '0.1.0',
    packages = ['leetline'],
    entry_points = {
        'console_scripts': [
            'leetline = leetline.__main__:main'
        ]
    })