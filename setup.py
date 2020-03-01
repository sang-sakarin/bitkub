from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='bitkub',
    version='0.0.2',
    description='A Python library for Bitkub API',
    long_description=readme(),
    url='https://github.com/sang-sakarin/bitkub',
    author='sang_sakarin',
    author_email='sang_sakarin@outlook.com',
    license='sang_sakarin',
    scripts=[],
    keywords='bitkub bitkub-python bitkub-python-sdk',
    packages=['bitkub'],
    install_requires=['requests'],
)
