from huelina.huelina import version

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='Huelina',
    version=str(version),
    packages=['huelina'],
    url='https://github.com/DrNightingales/Huelina',
    license='GNU GPL v3.0',
    author='DrNightingales',
    author_email='petersoloviev123@gmail.com',
    description='A program for solving tests with multiple choice',
    install_requires="colorama",
    python_requires='>=3.6'
)
