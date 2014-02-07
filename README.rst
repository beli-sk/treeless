Treeless
========

Text mode directory tree viewer.

The name is made of *tree* as in directory tree and *less* the text viewer
which is used by *Treeless* to display its output.

Locations
---------

Treeless packages are available from Cheese shop (PyPI)
at https://pypi.python.org/pypi/treeless

The `project page <https://github.com/beli-sk/treeless>`_ is hosted on Github.

If you've never worked with *git* or contributed to a project on Github,
there is a `quick start guide <https://help.github.com/articles/fork-a-repo>`_.

If you find something wrong or know of a missing feature, please
`create an issue <https://github.com/beli-sk/treeless/issues>`_ on the project
page. If you find that inconvenient or have some security concerns, you could
also drop me a line at <devel@beli.sk>.

Install
~~~~~~~

::

    pip install treeless

Use
---

::

    usage: treeless [-h] [--filematch REGEXP] [--dirmatch REGEXP]
                    [--fileignore REGEXP] [--dirignore REGEXP] [--indent N]
                    [--plain] [--cut] [--version]
    
    Treeless - Text mode directory tree viewer
    
    optional arguments:
      -h, --help            show this help message and exit
      --filematch REGEXP, -f REGEXP
                            Files regexp
      --dirmatch REGEXP, -d REGEXP
                            Directories regexp
      --fileignore REGEXP, -F REGEXP
                            Regexp for ignored files
      --dirignore REGEXP, -D REGEXP
                            Regexp for ignored directories
      --indent N, -i N      Indent length (1-8, default=1)
      --plain, -p           Plain output on stdout, no less
      --cut, -c             Cut off long lines to fit terminal width
      --version, -v         Show version and exit

License
-------

Copyright 2013 Michal Belica <devel@beli.sk>

::

    Treeless is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    Treeless is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with Treeless.  If not, see < http://www.gnu.org/licenses/ >.

