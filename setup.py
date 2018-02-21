from setuptools import setup, find_packages

setup(
    name='oneliners',
    version='1.0',
    description="A collection of random one-liner jokes scraped from the Internet.",
    long_description=open("README.rst").read(),
    author='Konstantin Tretyakov',
    author_email='kt@ut.ee',
    license='MIT',
    classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 7 - Inactive',
    ],
    zip_safe=False,
    url='https://github.com/konstantint/oneliners',
    packages=find_packages(),
    include_package_data=True
)
