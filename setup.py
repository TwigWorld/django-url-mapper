from setuptools import find_packages
from setuptools import setup

setup(
    name="django-url-mapper",
    version="2.1.0",
    author="Colin Barnwell",
    scripts=[],
    description="Use fixed keys in your Django template to refer to dynamic URLs",
    long_description=open("README.md").read(),
    install_requires=[
        "Django<3",
    ],
    extras_require={
        "testing": [
            "pytest",
            "pytest-django",
            "black",
            "isort",
            "pre-commit",
            "check_pdb_hook",
        ]
    },
    packages=find_packages(),
    include_package_data=True,
)
