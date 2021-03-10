from setuptools import setup

setup(
    name='hubmapbags',
    version='0.0.0',
    description='Generates BDBags for CFDE',
    url='https://github.com/hubmapconsortium/cfde-bdbag',
    author='Ivan Cao-Berg',
    author_email='icaoberg@psc.edu',
    packages=['hubmapbags'],
    install_requires=['pandas',
                      'numpy',
                      'tabulate'],
)
