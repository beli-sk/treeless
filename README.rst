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
                    [--indent-char CH] [--plain] [--cut] [--version]
                    [path]
    
    Treeless - Text mode directory tree viewer
    
    positional arguments:
      path                  Base path to start listing from
    
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
      --indent-char CH, -C CH
                            Indent character (default=.)
      --plain, -p           Plain output on stdout, no less
      --cut, -c             Cut off long lines to fit terminal width
      --version, -v         Show version and exit

Configuration
-------------

Treeless reads in configuration files in INI format. The same options as on
the command line are expected in the files. Files are read from following
locations, where latter override options from former files and command line
options override those from config files.

* ``/etc/treeless.conf``
* ``~/.config/treeless.conf``
* ``~/.treeless.conf``

Config file example (values shown here are not the defaults)::

    [treeless]
    # include files matching regular expression
    filematch = .*
    # include directories matching regexp
    dirmatch = .*
    # ignore files matching regexp
    fileignore = ^\.
    # ignore directories matching regexp
    dirignore = ^\.git$|^\.svn$
    # Note: a file or directory has to match the positive filter and not match
    #       the negative filter at the same time to be included in output
    # length of indent
    indent = 2
    # plain output on stdout, no less; allowed "ON" values are ``1, yes, true, on``
    # and "OFF" values ``0, no, false, off`` (case insensitive)
    plain = yes
    # cut off long lines to fit terminal width (accepts same values as *plain*)
    cut = false

The ``[treeless]`` section title is mandatory.

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

