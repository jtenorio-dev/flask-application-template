from setuptools import find_packages, setup
import os
import io

def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name="flask-application",
    version=read("app", "VERSION"),
    description="Flask Template",
    url="https://github.com/jtenorio-dev/template",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Jomari Tenorio",
    packages=find_packages(exclude=["tests"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["app = app.__main__:main"]
    },
    extras_require={
        "test": read_requirements("requirements-test.txt")
        + read_requirements("requirements-dev.txt")
    },
)