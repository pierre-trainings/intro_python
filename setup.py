from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["Click==7.0"]

setup(
    name="intro_python",
    version="0.0.1",
    author="Pierre LC",
    author_email="pierrelchen@gmail.com",
    description="Python intro",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/pierre-trainings/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)
