from setuptools import find_packages
from setuptools import setup

setup(
    name='nameless',
    version='1.644.11',
    license='BSD-2-Clause',
    description='An example package. Generated with cookiecutter-pylibrary.',
    author='mpr',
    author_email='contact@ionelmc.ro',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,

)