# jlog
## Source:
This package is a python API for jlog from omniti-labs https://github.com/omniti-labs/jlog
Although you can found python API code in the source repo, Many problems occurred when we want to build it into a package which can be installed as a dependency of a whole project or system.

## Modules/Libs:
* Jlog: we refer to it as the python extension for jlog lib(it also has java, perl, php version), which provide API to call service in libjlog.
* libjlog: provide the core service of logging

## References:
* http://stackoverflow.com/questions/16993927/using-cython-to-link-python-to-a-shared-library
* http://stackoverflow.com/questions/7847305/how-to-set-ld-library-path-individually-for-django-web-sites-with-apache-and-mod?lq=1
* http://stackoverflow.com/questions/856116/changing-ld-library-path-at-runtime-for-ctypes
* http://docs.cython.org/src/reference/compilation.html
