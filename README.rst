1. Source:
          https://github.com/omniti-labs/jlog
2. Modules/Libs:
         Jlog: we refer to it as the python extension for jlog lib(it also has java, perl, php version), which provide API to call service in libjlog.
         libjlog: provide the core service of logging
3. Build:
          First build jlog, the required 'setup.py' is under the python/ folder in jlog
          Build libjlog.so
4. Methods:
         ALL source code can be downloaded from the source above, the jlog in the source is actually that can be build into libjlog, and its extensions for Python, Perl, Java lies in different folders.
         a. In order to build a python package, Lets change the structure layout a little bit.
            Before:
                 jlog/
                       java/
                       python/
                       perl/
                       configure.in
                       <source file>
            After:
                  python/
                       setup.py
                       MANIFEST.in
                       jlog.c
                       cjlog.pxd
                       jlog.pyx
                       jlog/
             Notes: Folder java/,  perl/ and all other files that not required by python can be removed.
      b. Then edit MANIFEST.in to include or exclude files for jlog python package,
include *.pyx
include *.pxd
include README.rt
graft jlog  
global-exclude *.pyo
global-exclude *.pyc
prune jlog/perl
prune jlog/java
prune jlog/php

       c. Edit setup.py (Suggest setuptool.)
              Extend built_ext to write customized build steps,
              Then,  add cmdclass to make it available when run python setup.py install
              cmdclass = { 'build_ext': build_cjlog }

       d.  Publish the pip package:
               python setup.py sdist upload -r https://packages.corp.surveymonkey.com

       e.  Use the lib in pyramid project
                 python setup.py develop
            if jlog==1.0 lies in your requirements.txt, finally jlog will be installed correctly.

            As jlog still need to call libjlog.so.2 in run time, currently need to load it manually, use:
                    from ctypes import cdll cdll.LoadLibrary('/usr/local/lib/libjlog.so.2')
                          or
                    export LD_LIBRARY_PATH=/usr/local/lib
             Notes: Still not able to find a way to bind the shared lib to the package which enable to get rid of using the dynamic lib loading manually.

5 References:
       (1)  http://stackoverflow.com/questions/16993927/using-cython-to-link-python-to-a-shared-library
       (2)  http://stackoverflow.com/questions/7847305/how-to-set-ld-library-path-individually-for-django-web-sites-with-apache-and-mod?lq=1
       (3) http://stackoverflow.com/questions/856116/changing-ld-library-path-at-runtime-for-ctypes
       (4) http://docs.cython.org/src/reference/compilation.html
