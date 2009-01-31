import os
def pre_configure(options, buildout):
    """Custom pre-make hook for building libjpeg."""
    os.system("chmod +x %s/configure" % buildout['part']['compile-directory'])

