from setuptools import setup, find_packages

setup(
    name="seed-compiler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'jinja2>=3.1.2',
    ],
    entry_points={
        'console_scripts': [
            'seedc=seed_compiler.cli:main',
        ],
    },
)
