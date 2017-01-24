from distutils.core import setup

setup(
    name='django-screenshots',
    version='0.1.1',
    author='Jim Barcelona',
    author_email='barce@me.com',
    packages=['django-screenshots', 'django-screenshots.tests'],
    scripts=[],
    url='http://pypi.python.org/pypi/django-screenshots/',
    license='LICENSE.txt',
    description='Screen shot a URL.',
    long_description=open('README.txt').read(),
)
