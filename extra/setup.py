import io
from os.path import dirname, join

from setuptools import find_packages
from setuptools import setup

def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf-8")
    ).read()


setup(
    name="pycsw_frontend",
    version="0.1.0",
    description="A demo Django project that uses django-pycsw",
    long_description=open("README.rst").read(),
    author="Ricardo Garcia Silva",
    author_email="ricardo.garcia.silva@gmail.com",
    license="Apache",
    url="https://github.com/ricardogsilva/django-pycsw",
    package_dir = {"": "pycsw_frontend"},
    packages=find_packages("pycsw_frontend"),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        ],
    install_requires=[
        "django",
        "djangopycsw",
    ],
    zip_safe=False,
)
