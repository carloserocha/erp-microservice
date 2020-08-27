from setuptools import find_packages, setup

setup(
    name='product',
    version='0.0.1',
    description='Store and Serve ProductData',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'nameko==v3.0.0-rc6',
        'nameko-sqlalchemy==1.5.0',
        'alembic==1.0.10',
        'marshmallow==2.19.2',
        'psycopg2-binary==2.8.2',
    ],
    zip_safe=True
)