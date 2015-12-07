from distutils.core import Command
from setuptools import setup, find_packages, Extension
from distutils.command.build_ext import build_ext as _build_ext
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

ext_modules=[
  Extension(
    "jlog",
    ["jlog.c"],
    libraries = ["jlog"],
    include_dirs = [
      "/usr/local/include",
      "/usr/include"],
    library_dirs = [
      "/usr/local/lib",
      "/usr/lib"]
  )
]

class build_cjlog(_build_ext):
    description = "Build C Libjlog which linked by PyJlog Extension"
    user_options = []
    def _build_cjlog(self):
        BUILD_DIR = 'jlog/'
        CURRENT_DIR=os.getcwd()
        os.chdir(BUILD_DIR)
        os.system("autoconf > /dev/null 2>&1")
        os.system("./configure > /dev/null 2>&1")
        os.system("make clean > /dev/null 2>&1")
        os.system("make > /dev/null 2>&1")
        os.system("sudo make install > /dev/null 2>&1")
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
     author_email = "yuq@surveymonkey.com",
     version = "1.0",
     license = 'MIT',
     description = "JLog Python Library",
     packages = find_packages(),
     include_package_data=True,
     zip_safe = False,
     url = "https://labs.omniti.com/labs/jlog",
     cmdclass = {
         'build_ext': build_cjlog
     },
     ext_modules = ext_modules
)
