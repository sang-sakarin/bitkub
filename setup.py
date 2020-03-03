import pypandoc

from setuptools import setup


long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='bitkub',
    version='0.1.0',
    description='A Python library for Bitkub API',
    long_description=long_description,
    url='https://github.com/sang-sakarin/bitkub',
    author='sang_sakarin',
    author_email='sang_sakarin@outlook.com',
    license='sang_sakarin',
    scripts=[],
    keywords='bitkub bitkub-python bitkub-python-sdk',
    packages=['bitkub'],
    install_requires=['requests'],
)
