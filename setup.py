from setuptools import setup
from setuptools import find_packages

setup(
    name="cloob",
    version="1.0.0",
    author="Andreas Fuerst",
    author_email="fuerst@ml.jku.at",
    package_dir = {
        'cloob': 'src',
    },
    packages=['cloob.clip'],
    include_package_data=True
)