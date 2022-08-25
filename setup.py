from setuptools import setup, find_packages

setup(
    name='django-url-mapper',
    version='2.0.0',
    author='Colin Barnwell',
    scripts=[],
    description='Use fixed keys in your Django template to refer to dynamic URLs',
    long_description=open('README.md').read(),
    python_requires='>=3.7.0'
    install_requires=[
        "Django>=1.11.29, <2.0",
    ],
    packages=find_packages(),
    include_package_data=True
)
