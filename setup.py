import setuptools
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

install_dependencies = [
    "joblib==0.16.0",
]

setuptools.setup(
    name="fmlwright-api",
    version="0.1.0",
    author="Sebastiaan",
    author_email="Sebastiaan",
    description="Generator api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_dependencies,
    packages=find_packages(),
)
