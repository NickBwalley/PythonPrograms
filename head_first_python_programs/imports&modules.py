Python 3.8.2 (default, Mar 13 2020, 10:14:16) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> datetime.date.today()
datetime.date(2020, 4, 24)
>>> datetime.date.today().day
24
>>> datetime.date.today().year
2020
>>> datetime.date.today().month
4
>>> datetime.date.isoformat(datetime.date.today())
'2020-04-24'
>>> import time
>>> time.strftime("%H:%M")
'22:41'
>>> time.strftime("%A %p")
'Friday PM'
>>> import html
>>> html.escape("<a>go to this page to see nick and the bronzebomber</a>")
'&lt;a&gt;go to this page to see nick and the bronzebomber&lt;/a&gt;'
>>> html.unescape("<a>go to this page to see nick and the bronzebomber</a>")
'<a>go to this page to see nick and the bronzebomber</a>'
>>> html.unescape("I &hearts; coding with passion")
'I ♥ coding with passion'
>>> 