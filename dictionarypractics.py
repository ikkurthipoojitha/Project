Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> diction={}
>>> mydict={1:'ofo',2:'poo',3:'pkil'}
>>> mydict
{1: 'ofo', 2: 'poo', 3: 'pkil'}
>>> mydict.items()
dict_items([(1, 'ofo'), (2, 'poo'), (3, 'pkil')])
>>> mydict.values()
dict_values(['ofo', 'poo', 'pkil'])
>>> mydict.keys()
dict_keys([1, 2, 3])
>>> mydict.get[2]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    mydict.get[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> mydict.get(2)
'poo'
>>> mydict[4]={2:'poojitha'}
>>> mydict
{1: 'ofo', 2: 'poo', 3: 'pkil', 4: {2: 'poojitha'}}
>>> mydict[2]={'poojitha'}
>>> mydict
{1: 'ofo', 2: {'poojitha'}, 3: 'pkil', 4: {2: 'poojitha'}}
>>> mydict[2]='kavya'
>>> mydict
{1: 'ofo', 2: 'kavya', 3: 'pkil', 4: {2: 'poojitha'}}
>>> a={1:'oku',2:'kojk',3:'poo',2:'poojitha'}
>>> a
{1: 'oku', 2: 'poojitha', 3: 'poo'}
>>> b={1:'a',2:'v',3:'o',4:'g',1:3,2:'n'}
>>> b
{1: 3, 2: 'n', 3: 'o', 4: 'g'}
>>> mixed={1:89,2:'lkkjfke','name':'pooo','lollipop':98}
>>> mixedd
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    mixedd
NameError: name 'mixedd' is not defined
>>> mixed
{1: 89, 2: 'lkkjfke', 'name': 'pooo', 'lollipop': 98}
>>> d=mixed
>>> d
{1: 89, 2: 'lkkjfke', 'name': 'pooo', 'lollipop': 98}
>>> mixed['name']
'pooo'
>>> mixed.get('name')
'pooo'
>>> mixed.get('salary')
>>> mixed.pop(1)
89
>>> mixed
{2: 'lkkjfke', 'name': 'pooo', 'lollipop': 98}
>>> mixed.popitem()
('lollipop', 98)
>>> mixed
{2: 'lkkjfke', 'name': 'pooo'}
>>> mixed.clear()
>>> mixed
{}
>>> del mixed
>>> mixed
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    mixed
NameError: name 'mixed' is not defined
>>> c={1:'po',2:'kjl'}
>>> k=e.copy(c)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    k=e.copy(c)
NameError: name 'e' is not defined
>>> e={'mail':3}
>>> k=e.copy(c)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    k=e.copy(c)
TypeError: copy() takes no arguments (1 given)
>>> k=e.copy()
>>> k
{'mail': 3}
>>> k.update(c)
>>> k
{'mail': 3, 1: 'po', 2: 'kjl'}
>>> c
{1: 'po', 2: 'kjl'}
>>> c[3]='lol'
>>> c
{1: 'po', 2: 'kjl', 3: 'lol'}
>>> k
{'mail': 3, 1: 'po', 2: 'kjl'}
>>> c.clear()
>>> c
{}
>>> k
{'mail': 3, 1: 'po', 2: 'kjl'}
>>> abc={'nik':'loop',2:0887,3:None}
SyntaxError: invalid token
>>> abc={'nik':'loop',2:0887}
SyntaxError: invalid token
>>> abc={'nik':'loop',2:887}
>>> abc.setdefault(3:None}
SyntaxError: invalid syntax
>>> abc.setdefault(3,None}
SyntaxError: invalid syntax
>>> abc.setdefault(3,None)
>>> abc
{'nik': 'loop', 2: 887, 3: None}
>>> square={x:x*x for x in range(3)}
>>> square
{0: 0, 1: 1, 2: 4}
>>> oddsquare={x:x*x for x in range(23) if x%2==1}
>>> oddsquare
{1: 1, 3: 9, 5: 25, 7: 49, 9: 81, 11: 121, 13: 169, 15: 225, 17: 289, 19: 361, 21: 441}
>>> len(oddsquare)
11
>>> all(oddsquare)
True
>>> v={}
>>> any(v)
False
>>> 
