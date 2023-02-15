from setuptools import setup

setup(
    name="fileInfoExtraction",
    version="0.1.0",
    author="Tuanne Assenço",
    author_email="tuanne.assenco@gmail.com",
    description="A library for retrieving information about files",
    long_description="A longer description of the library and its features",
    url="https://github.com/devlower/fileInfoExtraction",
    packages=["fileInfoExtraction"],
    install_requires=["chardet", "python-magic"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
