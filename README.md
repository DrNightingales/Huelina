# Huelina
A program for creating and solving tests with multiple choice

## Installation
Install as python package from TestPyPI:
```python3 -m pip install --index-url https://test.pypi.org/simple/ example_pkg```

## Requirements & Dependencies 
python 3.6.x+ <br />
[Colorama](https://pypi.org/project/colorama/)


In future PyQT5 library will be used for GUI

## Issues
You may have troubles with encodings. Use ANSI files on windows and UTF-8 on unix/linux


## Syntax for files with questions&answers
*example:*
~~~
1 Question
:question image url/path (not supported yet)
incorrect ans1
incorrect ans2
*correct ans1
~~~
***The rules actually are:***
 1. If the first symbol is number, then it's a question (**NB**, if you want one of your answers to start from number add space)
 2. If the first symbol is a colon, then it's a link to an image for a qusetion (not supported yet)
 3. If the first symbol is an asterisk(*), then it's a correct answer
 4. Any other first character will mean an incorrect answer
 
