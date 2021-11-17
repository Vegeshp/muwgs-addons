from setuptools import setup, find_packages


setup(
    name='muwgs',
    version='1.0.0',
    keywords=['Microsoft Ultimate Word Games', 'script', 'python'],
    description='muwg script',
    long_description='Python Script for automatic playing Microsoft Ultimate Word Games',
    license='MIT License',

    url='https://github.com/bhshp/muwgs.git',
    author='bhshp',
    author_email='shp_123@foxmail.com',

    include_package_data=True,
    platforms='Windows 10 or above',
    packages=find_packages(),
    requires=[]
)
