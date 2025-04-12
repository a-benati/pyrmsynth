from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

VERSION = '1.3.1'

include_gsl_dir = "/usr/include/"
lib_gsl_dir = "/usr/lib/"

extensions = [
    Extension(
        "grid_tools",
        sources=["grid_tools.pyx"],
        include_dirs=[numpy.get_include(), include_gsl_dir],
        library_dirs=[lib_gsl_dir],
        libraries=["gsl", "gslcblas"],
    )
]

setup(
    name="rm_tools",
    version=VERSION,
    author="Michael Bell",
    author_email="mrbell@mpa-garching.mpg.de",
    description="rm_tools package from pyrmsynth",
    packages=["rm_tools"],
    package_dir={"rm_tools": ""},
    ext_modules=cythonize(extensions, language_level="3"),
)
