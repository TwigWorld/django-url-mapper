from setuptools import setup, find_packages

setup(
    name='django-url-mapper',
    version='1.0.2',
    author='Colin Barnwell',
    scripts=[],
    description='Use fixed keys in your Django template to refer to dynamic URLs',
    long_description=open('README.md').read(),
    install_requires=[
        "Django==1.11.29",
    ],
    packages=find_packages(),
    include_package_data=True
)
