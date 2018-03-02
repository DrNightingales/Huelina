# Huelina
A program for creating and solving tests with multiple choice

## Installation
No installation packeges are avaliable yet

## Dependencies 
No dependencies yet

In future PyQT5 library will be used for GUI

## Issues
On windows 8 or later you should run huelina through powershell, since escape sequences for colors are not supported in standart cmd

On linux you may change encoding for CSV files to utf8 rather than ansi


## CSV for test
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
 
