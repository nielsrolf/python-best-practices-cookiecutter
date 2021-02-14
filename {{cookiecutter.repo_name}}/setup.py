import os
import sys
from setuptools import setup


setup(
    name="{{cookiecutter.repo_name}}",
    version=0.1,
    description="Description here",
    license="Apache 2.0",
    packages=setuptools.find_packages(),
    package_data={"": ["*.gin"],},
    scripts=[],
    install_requires=[],
    extras_require={"test": ["pytest", "pylint!=2.5.0"],},
    entry_points={"console_scripts": [],},
    classifiers=[],
    tests_require=["pytest"],
    setup_requires=["pytest-runner"],
    keywords="audio dsp signalprocessing machinelearning music",
)
