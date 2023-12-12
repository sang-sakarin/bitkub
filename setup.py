import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bitkub-v2',
    version='3.1.3',
    description='A Python library for Bitkub API v3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/appcorner/bitkub',
    author='appcorner',
    author_email='appcorner@yahoo.com',
    license='MIT',
    scripts=[],
    keywords=['bitkub', 'bitkub-python', 'bitkub-python-sdk'],
    packages=['bitkub'],
    install_requires=['requests'],
)
