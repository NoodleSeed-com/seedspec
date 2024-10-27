from setuptools import setup, find_packages

setup(
    name="seedml",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "anthropic>=0.3.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "seedml=seedml_generator:main",
        ],
    },
    python_requires=">=3.8",
    author="SeedML Team",
    author_email="team@seedml.dev",
    description="CLI tool for generating applications from SeedML specifications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seedml/seedml",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
