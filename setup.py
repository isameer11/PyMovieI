from setuptools import setup

setup(
    name='PyMovieI',
    version='0.1.0',
    author='Sameer Khan',
    author_email='sameermadina786@gmail.com',
    packages=['PyMovieI'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='PyMovieI is Python Library to fetch movie information and Movie Poster using Webscraping',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        ["bs4"
,"google"
,"requests"
,"lxml"]
    ],
    classifiers=[
    "License :: OSI Approved::MIT License"
    "Programing Language ::Python::3.x"
    ]
)