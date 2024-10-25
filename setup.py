from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="craftitec-files",
    version="0.0.3",
    description="""Description pending.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Adeolu Oyewo",
    packages=find_packages(include=["files"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    license="MIT",
    url="https://github.com/AyobamitheTitan/files",
)
