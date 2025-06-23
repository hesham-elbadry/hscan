from setuptools import setup

setup(
    name='hscan',
    version='1.0',
    py_modules=['hscan'],
    entry_points={
        'console_scripts': [
            'hscan = hscan:main',
        ],
    },
)
