from distutils.core import setup

version = '0.0.1'

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name = 'yamljson2xml',
    version = version,
    description = 'Converts json or yaml files to xml.',
    long_description = long_description,
    author = 'Matt Dewar',
    author_email = 'mattpdewar@gmail.com',
    license = 'LICENCE.txt',
    url = 'https://github.com/kobbled/yamljson2xml',
    package_dir={'yamljson2xml': 'src'},
    packages=['yamljson2xml'],
    platforms='Cross-platform',
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 3'
    ],
)
