Python 3.8.2 (default, Apr 27 2020, 15:53:34) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> first = [1,2,3,4,5]
>>> first
[1, 2, 3, 4, 5]
>>> second = first
>>> second
[1, 2, 3, 4, 5]
>>> second.append(6)
>>> second
[1, 2, 3, 4, 5, 6]
>>> first
[1, 2, 3, 4, 5, 6]
>>> third = second.copy()
>>> third
[1, 2, 3, 4, 5, 6]
>>> third.append(7)
>>> third
[1, 2, 3, 4, 5, 6, 7]
>>> second
[1, 2, 3, 4, 5, 6]
>>> saying = "Don't panic!"
>>> letters = list(saying)
>>> letters
['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
>>> letters[0]
'D'
>>> letters[3]
"'"
>>> letters[-1]
'!'
>>> letters
['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
>>> letters[0:10:3]
['D', "'", 'p', 'i']
>>> letters[:3]
['D', 'o', 'n']
>>> letters[3:]
["'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
>>> letters[:10]
['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i']
>>> letters[::2]
['D', 'n', 't', 'p', 'n', 'c']
>>> print('My name is Nick')
My name is Nick
>>> print("My name is Nick")
My name is Nick
>>> 