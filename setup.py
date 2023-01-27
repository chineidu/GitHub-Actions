from pathlib import Path

from setuptools import find_namespace_packages, setup

ROOT_DIR = Path(__file__).absolute().parent

# Required packages
def list_reqs(*, filename: str = "requirements.txt") -> None:
    with open(ROOT_DIR / filename, encoding="utf-8") as f:
        return f.read().splitlines()


setup(
    name="src",
    version="0.1.0",
    description="A simple package by Neidu.",
    author="Chinedu Ezeofor",
    author_email="neidue@email.com",
    packages=find_namespace_packages(),
    install_requires=list_reqs(),
    python_requires=">=3.8",
)
