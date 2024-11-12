from setuptools import find_packages, setup

def load_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name='bm23id24_xas',
    packages=find_packages(include=['bm23id24_xas']),
    version='0.0.7',
    description='Library for XAS data analysis',
    author='Molokova, Lomachenko, Lopez Romero',
    install_requires = load_requirements("requirements.txt"),
)