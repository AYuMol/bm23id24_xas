from setuptools import find_packages, setup
setup(
    name='bm23id24_xas',
    packages=find_packages(include=['bm23id24_xas']),
    version='0.0.1',
    description='Library for XAS data analysis',
    author='Molokova, Lomachenko, Lopez Romero',
    install_requires = ['xraylarch', 'pymcr', 'pyfitit','h5py'],
)