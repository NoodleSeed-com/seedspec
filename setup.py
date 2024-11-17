from setuptools import setup, find_packages

setup(
    name="seed-spec",
    version=__import__('seed_spec').__version__,
    packages=find_packages(),
    install_requires=[
        "anthropic>=0.3.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "seedspec=seed_spec.cli:main",
        ],
    },
    python_requires=">=3.8",
    author="Seed Spec Team",
    author_email="team@seedspec.dev",
    description="CLI tool for generating applications from Seed Specification Language",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fahd-noodleseed/seed-spec",
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
