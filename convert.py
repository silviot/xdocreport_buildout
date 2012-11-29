#!/usr/bin/env python
import os
import subprocess
import sys


LIBDIR = os.path.join(os.path.dirname(__file__), 'parts', 'xdocreport_tools', 'lib')
jars = []
for filename in os.listdir(LIBDIR):
    jars.append(os.path.abspath(os.path.join(LIBDIR, filename)))
base_args = ['java', '-classpath', ':'.join(jars), 'fr.opensagres.xdocreport.document.tools.Main' ]
subprocess.call(base_args + sys.argv[1:])
