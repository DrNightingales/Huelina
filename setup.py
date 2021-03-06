# -*- coding: utf-8 -*-

from huelina.huelina import __version__, script_path
import setuptools

with open ("README.md","r") as fh:
    long_descr = fh.read()

setuptools.setup(
    name='Huelina',
    version=str(__version__),
    packages=setuptools.find_packages(),
    url='https://github.com/DrNightingales/Huelina',
    license='GNU GPL v3.0',
    author='DrNightingales',
    author_email='petersoloviev123@gmail.com',
    description='A program for solving tests with multiple choice',
    install_requires="colorama>=0.3.9",
    python_requires='>=3.6',
    long_description=long_descr,
    long_description_content_type="text/markdown"
)
