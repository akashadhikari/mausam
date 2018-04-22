from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='mausam',

    version='0.0.1',

    description='A simple application that collects the daily weather data from Meteorological Forecasting Division, Nepal.',

    license='MIT',

    # long_description=long_description,

    # long_description_content_type='text/markdown',

    url='https://github.com/akashadhikari/mausam',

    author='Akash',

    author_email='akashsky1313@gmail.com',

    keywords='nepal weather scraping',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['beautifulsoup4', 'pandas'],

    # extras_require={},

    # package_data={},

    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # entry_points={},

    # project_urls={
    #     'Bug Reports': 'https://github.com/akashadhikari/mausam/issues',
    #     'Source': 'https://github.com/akashadhikari/mausam/',
    # },
)
