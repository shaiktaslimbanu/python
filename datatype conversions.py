Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #int
>>> int(8)
8
>>> int(8.0)
8
>>> int(3j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(3+j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+j)
NameError: name 'j' is not defined
>>> int("hello")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
>>> int(True)
1
>>> int(False)
0
>>> #float
>>> float(7)
7.0
>>> float(6.5)
6.5
>>> float(7j+10)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(7j+10)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float("hi")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #str
>>> str(11)
'11'
str(3.5)
'3.5'
string("world")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    string("world")
NameError: name 'string' is not defined. Did you forget to import 'string'?
str("hello")
'hello'
str(3j+30)
'(30+3j)'
str(True)
'True'
str(False)
'False'
#complex
complex(11)
(11+0j)
complex(2.8)
(2.8+0j)
complex("hi")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex("hi")
ValueError: complex() arg is a malformed string
complex(3j+100)
(100+3j)
complex(True)
(1+0j)
complex(flase)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(flase)
NameError: name 'flase' is not defined
complex(False)
0j
#boolean
bool(7)
True
bool(8.0)
True
bool("hlo")
True
bool(7j)
True
bool(True)
True
bool(False)
False
