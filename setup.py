#!/usr/bin/env python
#
# Treeless - Text mode directory tree viewer
#
# Copyright 2013 Michal Belica <devel@beli.sk>
#
# This file is part of Treeless.
# 
# Treeless is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Treeless is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Treeless.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

from treeless import __version__

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(name='treeless',
        version=__version__,
        author='Michal Belica',
        author_email='devel@beli.sk',
        url='https://github.com/beli-sk/treeless',
        description='Text mode directory tree viewer',
        long_description=long_description,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Natural Language :: English',
            # TODO 'Operating System :: OS Independent',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 2.7',
            # TODO 'Programming Language :: Python :: 3',
            'Topic :: Utilities',
            ],
        packages=['treeless'],
        package_data={'treeless': ['lesskey.*']},
        scripts=['scripts/treeless'],
        )

