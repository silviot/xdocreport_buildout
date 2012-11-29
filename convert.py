#!/usr/bin/env python
import os
import subprocess
import sys


LIBDIR = os.path.join(os.path.dirname(__file__), 'parts', 'xdocreport_tools', 'lib')
jars = []
for filename in os.listdir(LIBDIR):
    jars.append(os.path.abspath(os.path.join(LIBDIR, filename)))
subprocess.call(['java', '-classpath', ';'.join(jars)] + sys.argv[1:])
