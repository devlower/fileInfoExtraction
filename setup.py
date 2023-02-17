from setuptools import setup

setup(
    author="Tuanne Assenço",
    author_email="tuanne.assenco@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    description="A library for retrieving information about files",
    install_requires=["chardet", "python-magic"],
    long_description="A longer description of the library and its features",
    name="fileInfoExtraction",
    packages=["fileInfoExtraction"],
    url="https://github.com/devlower/fileInfoExtraction",
    version="0.1.0",
)
