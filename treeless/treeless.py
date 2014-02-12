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

import os
import re
import sys
import struct
import subprocess

__version__ = '0.1.1'

def _get_terminal_size_linux():
    # taken from https://gist.github.com/jtriley/1108174
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
                    fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])

def str2bool(s):
    if s.lower() in ('1', 'yes', 'true', 'on'):
        return True
    elif s.lower() in ('0', 'no', 'false', 'off'):
        return False
    else:
        raise ValueError('Invalid boolean value "%s"' % s)

def echo(s, fd=sys.stdout):
    fd.write(str(s))

def echoln(s, indent=0, indentstr='.', maxwidth=None, fd=sys.stdout):
    if indent:
        outs = (indentstr * indent) + str(s)
    else:
        outs = '' + str(s)
    if maxwidth and len(outs) > maxwidth:
        outs = outs[:maxwidth-2] + '..'
    echo(outs+"\n", fd=fd)

def cre_match(cre, s, default=False):
    if not cre:
        return default
    else:
        return bool(cre.search(s))

def output_tree(config, fd=sys.stdout):
    prev_root = None
    indent = 0
    cre_match_filenames = None if not config.filematch else re.compile(config.filematch)
    cre_match_dirnames = None if not config.dirmatch else re.compile(config.dirmatch)
    cre_ignore_filenames = None if not config.fileignore else re.compile(config.fileignore)
    cre_ignore_dirnames = None if not config.dirignore else re.compile(config.dirignore)
    if config.cut:
        width, height = _get_terminal_size_linux()
    else:
        width = None
    indentstr = config.indent_char + ' ' * (config.indent - 1)
    os.chdir(config.path)
    for root, dirs, files in os.walk('.'):
        if root != prev_root:
            prev_root = root
            indent = root.count('/')
            if indent != 0:
                echoln(os.path.basename(root)+'/', indentstr=indentstr,
                        indent=indent-1, maxwidth=width, fd=fd)
            dirs.sort()
        for n in dirs:
            if not cre_match(cre_match_dirnames, n, True) or \
                    cre_match(cre_ignore_dirnames, n, False):
                dirs.remove(n)
        files.sort()
        for n in files:
            if cre_match(cre_match_filenames, n, True) and \
                    not cre_match(cre_ignore_filenames, n, False):
                echoln(n, indent=indent, indentstr=indentstr,
                        maxwidth=width, fd=fd)

def less_control(config):
    r = 64
    datapath = os.path.dirname(__file__)
    while r in (64, 65):
        less = subprocess.Popen(
                ['/usr/bin/less', '-k%s/lesskey.bin' % datapath,
                    '-Ptreeless (^R refresh)', '-S', '+g'],
                stdin=subprocess.PIPE, bufsize=1
                )
        try:
            output_tree(config, fd=less.stdin)
        except IOError:
            pass
        less.stdin.flush()
        less.stdin.close()
        r = less.wait()

