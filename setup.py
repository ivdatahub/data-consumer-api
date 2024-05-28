from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        requirements = [line for line in lines if line and not line.startswith("#")]
    return requirements


setup(
    name='"ETL-awesome-api"',
    version="4.4.0",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
)
