from setuptools import setup, find_packages, find_namespace_packages
from setuptools.command.install import install
import subprocess
import os

class InstallPyCommand(install):
    def run(self):
        print('Running custom install programm')
        subprocess.call(['./bin/install.sh'])
        install.run(self)

setup(
    name='FACEID',
    version='1.0.0',
    url='https://www.hs-furtwangen.de/',
    license='',
    author='Studiengang Mobile Systeme',
    author_email='artur.dick@hs-furtwangen.de',
    description='Semesterprojekt',
    python_requires='~=3.6',
    packages=find_namespace_packages(include=['src.*']),
    include_package_data = True,
    entry_points = {
        'console_scripts': ['FACEID=src.controller.Controller:main']
    },
    scripts=['bin/install.sh'],
    cmdclass={
        'install': InstallPyCommand
    }
)
