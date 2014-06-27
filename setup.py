from distutils.core import setup

from setup_helpers import package_files


setup(
    name='django-url-mapper',
    version='0.1.1',
    author='Colin Barnwell',
    scripts=[],
    description='Use fixed keys in your Django template to refer to dynamic URLs',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.6",
    ],
    **package_files(app_dir='urlmapper')
)