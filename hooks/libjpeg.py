import os
import sys
def pre_configure(options, buildout):
    """Custom pre-make hook for building libjpeg."""
    if sys.platform.startswith('cygwin'):
        c = os.getcwd()
        os.chdir(options['compile-directory'])
        os.system("autoreconf -ifv")
    os.system("chmod +x %s/configure" % buildout['part']['compile-directory'])

