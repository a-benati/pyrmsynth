from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

include_gsl_dir = "/usr/include/"
lib_gsl_dir = "/usr/lib/"

VERSION = '1.3.1'

ext = Extension(
    "grid_tools",
    sources=["grid_tools.pyx"],
    include_dirs=[numpy.get_include(), include_gsl_dir],
    library_dirs=[lib_gsl_dir],
    libraries=["gsl", "gslcblas"]
)

setup(
    name="rm_tools",
    version=VERSION,
    description="rm_tools package from pyrmsynth",
    author="Michael Bell",
    author_email="mrbell@mpa-garching.mpg.de",
    packages=["rm_tools"],
    package_dir={"rm_tools": ""},
    ext_modules=cythonize([ext], language_level="3"),
    zip_safe=False
)
