from distutils.core import setup

setup(
    name='django-screenshots',
    version='0.2.0',
    author='Jim Barcelona',
    author_email='barce@me.com',
    packages=['django_screenshots', 'django_screenshots.tests'],
    install_requires=[
      'future', 'ipfshttpclient',
    ],
    scripts=[],
    url='http://pypi.python.org/pypi/django-screenshots/',
    license='LICENSE.txt',
    description='Screen shot a URL using a web server or p2p IPFS storage.',
    long_description=open('README.txt').read(),
)
