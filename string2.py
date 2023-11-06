Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> drive = 'c:\'
SyntaxError: incomplete input
>>> drive = 'c:\\"
SyntaxError: incomplete input
>>> drive = 'c:\\'
>>> folder = 'scripts\\python\\'
>>> file = 'myscript.py'
>>> path = drive + folder + file
>>> print(path)
c:\scripts\python\myscript.py
>>> something='1000'
>>> type(int(something))
<class 'int'>
