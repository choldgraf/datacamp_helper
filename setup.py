from setuptools import setup, find_packages
from timeseries import __version__

setup(
    name='timeseries',
    version=__version__,
    author='Chris Holdgraf',
    author_email='choldgraf@berkeley.edu',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
)
