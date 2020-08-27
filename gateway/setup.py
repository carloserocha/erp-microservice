from setuptools import find_packages, setup

setup(
    name='gateway',
    version='0.0.1',
    description='Serve Gateway',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'nameko==v3.0.0-rc6'
    ],
    zip_safe=True
)