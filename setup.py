# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 08:41:23
# @Last Modified time: 2018-01-22 09:55:37
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# For Markdown README
# https://stackoverflow.com/a/26737672/5951529
setup(
    packages=find_packages(),
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('', ['README.md'])],
    # long_description=long_description
)
