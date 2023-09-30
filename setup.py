from setuptools import setup, find_packages

setup(
    name="sshLoadFile",
    version="0.0.1",
    description='Package for loading files on server via ssh.',
    author="AstroKen",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "paramiko"
        ],
    include_package_data=True,
)
