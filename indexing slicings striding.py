Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #indexing
>>> #postive
>>> a="taslim"
>>> a[0]+a[5]
'tm'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'taslim'
>>> #negative
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]
'milsa'
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]
IndexError: string index out of range
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]
'milsat'
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'taslim'
>>> "vijyawada is a royal city"
'vijyawada is a royal city'
>>> a="vijyawada is a royal city"
>>> a[-1]+a[-2]+a[-3]+a[-4]
'ytic'
>>> a[-4]+a[-3]+a[-2]+a[-1]
'city'
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
>>> a[-4]
'c'
>>> a[-8]
'y'
>>> a[-12]
'a'
>>> a[-9]+a[-8]
'oy'
>>> a[-14]+a[-13]
's '
>>> #slicing
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> "vijaywada"
'vijaywada'
a[:10]
'codegnan'
b="vijaywada"
a[:10]
'codegnan'
b[:10]
'vijaywada'
c="vizag is a city of destiny
SyntaxError: unterminated string literal (detected at line 1)
c="vizag is a city of destiny"
c[0:5]
'vizag'
c[7:8]
's'
c=[6:8]
SyntaxError: invalid syntax
c[6:8]
'is'
c[9:10]
'a'
c[11:14]
'cit'
c[11:15]
'city'
c[16:18]
'of'
c[17:25]
'f destin'
c=[18:26]
SyntaxError: invalid syntax
c=[18:26]
SyntaxError: invalid syntax
c=[18:26]
SyntaxError: invalid syntax
c[18:25]
' destin'
c[18:26]
' destiny'
#negative
a="a simple is better than complex"
a[-7:]
'complex'
a[-7:11]
''
a[-7:-1]
'comple'
a[-8:-1]
' comple'
a[-8:-0]
''
a[-7:-1]
'comple'
a[-12:-8]
'than'
a[-19:-13]
'better'
a[-20:12]
' '
a[-22:14]
'is be'
a[-22:12]
'is '
a[-22:28]
'is better than comp'
a[-28:22]
'imple is better tha'
a[-29-19]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a[-29-19]
IndexError: string index out of range
a[-29:19]
'simple is better '
a[29:23]
''
a[-29:-23]
'simple'
a[23-24]
'x'
a[-7:24]
''
a[-7:23]
''
#striding
#postive
a="data science"
a=[a:b:c]
SyntaxError: invalid syntax
a[a:b:c]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a[a:b:c]
TypeError: slice indices must be integers or None or have an __index__ method
[::]
SyntaxError: invalid syntax
a=[::]
SyntaxError: invalid syntax
a[::]
'data science'
a[::4]
'd e'
a[::1]
'data science'
a[::2]
'dt cec'
a[::4]
'd e'
b="machine learning"
a[::1]
'data science'
b=[::1]
SyntaxError: invalid syntax
b[::1]
'machine learning'
#bcie l anng
b[::2]
'mcielann'
b[::3]
'mheeng'
c="python
SyntaxError: unterminated string literal (detected at line 1)








'
c="python"
c[::6]
'p'
c[::]
'python'
c[::1]
'python'
c[::2]
'pto'
c[::3]
'ph'
d="cloud computing"
d[::]
'cloud computing'
[::1]
SyntaxError: invalid syntax
c[::]
'python'
d[::]
'cloud computing'
d[::1]
'cloud computing'
d[::2]
'codcmuig'
d[::3]
'cucpi'
#negative
e="tashu"
e[::]
'tashu'
e[::1]
'tashu'
e[::-1]
'uhsat'
e[::-2]
'ust'
e[::-5]
'u'
e[-5:-1]
'tash'
e[-6:-1]
'tash'
e[-6:-7]
''
f="python course"
f=[-1:-9:-2]
SyntaxError: invalid syntax
f[-1:-9:-2]
'ero '
f[-2:-12:-2]
'sucnh'
