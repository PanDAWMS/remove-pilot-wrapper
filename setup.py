#!/usr/bin/env python
#
# Setup prog for wrapper executable 
#
#
release_version='1.0.1'

import os
import sys

from distutils.core import setup
from distutils.command.install import install as install_org
from distutils.command.install_data import install_data as install_data_org

# ===========================================================
#           data files
# ===========================================================

docs_files = ['docs/%s' %file for file in os.listdir('docs') if os.path.isfile('docs/%s' %file)]

executable = ['wrapper-%s.sh' %release_version,]

rpm_data_files=[ ('/usr/libexec', executable),                                        
                 ('/usr/share/doc/wrapper', docs_files),                                        
               ]
home_data_files=[ ('doc/wrapper', docs_files),                                        
                 ('libexec', executable),                                        
               ]

# ===========================================================

def choose_data_files():
    rpminstall = True
    userinstall = False
     
    if 'bdist_rpm' in sys.argv:
        rpminstall = True

    elif 'install' in sys.argv:
        for a in sys.argv:
            if a.lower().startswith('--home'):
                rpminstall = False
                userinstall = True
                
    if rpminstall:
        return rpm_data_files
    elif userinstall:
        return home_data_files
    else:
        # Something probably went wrong, so punt
        return rpm_data_files
       
# setup for distutils
setup(
    name="wrapper",
    version=release_version,
    description='wrapper package',
    long_description='''This package contains wrapper''',
    license='GPL',
    author='Jose Caballero',
    author_email='jcaballero@bnl.gov',
    maintainer='Jose Caballero',
    maintainer_email='jcaballero@bnl.gov',

    data_files = choose_data_files()
)
