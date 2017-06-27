#!/usr/bin/env python
import os
from setuptools import setup
from setuptools import find_packages
from pip.req import parse_requirements


def get_package_data(package):
  walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
          for dirpath, dirnames, filenames in os.walk(package)
          if not os.path.exists(os.path.join(dirpath, '__init__.py'))]
  filepaths = []
  for base, filenames in walk:
    filepaths.extend([os.path.join(base, filename)
                      for filename in filenames])
  return {package: filepaths}


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
install_reqs = parse_requirements('requirements.txt', session=False)
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as file:
  README = file.read()
requirements = [str(ir.req) for ir in install_reqs]
setup(
  name             = 'Pi-Stonith-For-Modem',
  version          = '1.0.0',
  description      = 'Modem stonith',
  author           = 'Isaac Kerley',
  author_email     = 'isaackerley.@gmail',
  url              = 'https://github.com/monkeyboy107/Pi-Stonith-For-Modem',
  zip_safe         = False,
  install_requires = requirements,
  data_files       = [
    ('/etc/systemd/system/', [
      'systemd/pistonithformodem.service',
    ])
  ],
  packages=find_packages()+['pistonithformodem'],
  package_data=get_package_data('pistonithformodem'),
  entry_points = {
    "console_scripts": [
      "pistonithformodem = pistonithformodem:shell",
    ]
  }
)