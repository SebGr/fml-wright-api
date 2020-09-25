from distutils.core import setup

install_requires = [
    "fastapi==0.61.1",
    "uvicorn==0.11.8",
    "python-multipart"
]

setup(
    name="fml-wright-api",
    author="Sebastiaan Grasdijk",
    packages=["app"],
    install_requires=install_requires
)
