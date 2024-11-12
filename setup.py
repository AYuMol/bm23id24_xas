from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='bm23id24_xas',
    packages=find_packages(include=['bm23id24_xas']),
    version='0.0.9',
    description='Library for XAS data analysis',
    long_description=long_description,
    author='Molokova, Lomachenko, Lopez Romero',
    install_requires = required,
)