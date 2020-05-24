Python 3.8.2 (default, Apr 27 2020, 15:53:34) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> book = "The hitchhiker's Guide to the Galaxy"
>>> booklist = list(book)
>>> book
"The hitchhiker's Guide to the Galaxy"
>>> booklist
['T', 'h', 'e', ' ', 'h', 'i', 't', 'c', 'h', 'h', 'i', 'k', 'e', 'r', "'", 's', ' ', 'G', 'u', 'i', 'd', 'e', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 'G', 'a', 'l', 'a', 'x', 'y']
>>> booklist[:3]
['T', 'h', 'e']
>>> ''.join(booklist[0:3])
'The'
>>> ''.join(booklist[-6])
'G'
>>> ''.join(booklist[-6:])
'Galaxy'
>>> backwards = booklist[::-1]
>>> ''.join(backwards)
"yxalaG eht ot ediuG s'rekihhctih ehT"
>>> every_other = booklist[::2]
>>> ''.join(every_other)
"Tehthie' ud oteGlx"
>>> booklist
['T', 'h', 'e', ' ', 'h', 'i', 't', 'c', 'h', 'h', 'i', 'k', 'e', 'r', "'", 's', ' ', 'G', 'u', 'i', 'd', 'e', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 'G', 'a', 'l', 'a', 'x', 'y']
>>> booklist[4:13]
['h', 'i', 't', 'c', 'h', 'h', 'i', 'k', 'e']
>>> hitchhiker = booklist[4:14]
>>> ''.join(hitchhiker)
'hitchhiker'
>>> ''.join(booklist=[-21:-32])
SyntaxError: invalid syntax
>>> ''.join(booklist[15:4:-1])
"s'rekihhcti"
>>> ''.join(booklist[15:3:-1])
"s'rekihhctih"
>>> ''.join.(booklist)
SyntaxError: invalid syntax
>>> ''.join(booklist)
"The hitchhiker's Guide to the Galaxy"
>>> ''.join(booklist[17:22])
'Guide'
>>> ''.join(booklist[22:16:-1])
' ediuG'
>>> 