from setuptools import setup

setup(
    name='django-html5',
    version='1.0.0',
    url='https://github.com/dyve/django-html5',
    author='Dylan Verheul',
    author_email='dylan@dyve.net',
    license='Apache License 2.0',
    packages=['html5', 'html5.forms'],
    include_package_data=True,
    description='HTML5 support for Django projects',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
