from setuptools import setup, find_packages

setup(
    name="edusco",
    version="0.1",
    packages=find_packages(),
    install_requires=["pyspellchecker"],
    package_data={
        "edusco": ["resources/*.json"],   
    },
)
