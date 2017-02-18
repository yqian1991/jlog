from distutils.core import Command
from setuptools import setup, find_packages, Extension
from distutils.command.build_ext import build_ext as _build_ext
from distutils.command.install import install
import os, sys

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
LIB_PATH = sys.prefix
#SITE_PACKAGE_PATH = os.sep.join(['/', sys.prefix, 'lib', 'python' + sys.version[:3], 'site-packages'])

ext_modules=[
  Extension(
    "jlog",
    ["jlog.c"],
    libraries = ["jlog"],
    include_dirs = [
      "/usr/local/include",
      "/usr/include",
      LIB_PATH+'/include',
      LIB_PATH+"/local/include"],
    library_dirs = [
      "/usr/local/lib",
      "/usr/lib",
      LIB_PATH+'/local/lib',
      LIB_PATH+'/lib']
  )
]

class build_cjlog(_build_ext):
    description = "Build C Libjlog which linked by PyJlog Extension"
    user_options = []
    def _build_cjlog(self):
        BUILD_DIR = 'jlog/'
        CURRENT_DIR=os.getcwd()
        os.chdir(BUILD_DIR)
        #os.system("autoconf > /dev/null 2>&1")
        os.environ['LIB_PATH'] = LIB_PATH
        os.system("./configure --prefix=$LIB_PATH > /dev/null 2>&1")
        os.system("make clean > /dev/null 2>&1")
        os.system("make > /dev/null 2>&1")
        os.system("make install > /dev/null 2>&1")
        os.chdir(CURRENT_DIR)
    def initialize_options(self):
        _build_ext.initialize_options(self)
    def finalize_options(self):
        _build_ext.finalize_options(self)
    def run(self):
        self._build_cjlog()
        _build_ext.run(self)

setup(
     name = "jlog",
     author = "Yu Qian",
     author_email = "jinggeqianyu1991@gmail.com",
     version = "1.0.1",
     license = 'MIT',
     description = "JLog Python Library",
     packages = find_packages(),
     package_data = {'libjlog': ['libjlog.so.2']},
     include_package_data = True,
     zip_safe = False,
     url = "https://labs.omniti.com/labs/jlog",
     cmdclass = {
         'build_ext': build_cjlog
     },
     ext_modules = ext_modules
)
