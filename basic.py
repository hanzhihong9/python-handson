'''
>>> it= (i for i in range(1,3))
>>> it
<generator object <genexpr> at 0x0000000004D36438>
>>> it.next()
1
>>> it.next()
2
>>> it.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> it= [i for i in range(1,4)]
>>> it
[1, 2, 3]


>>> it= [i for i in range(1,4)]
>>> m = [[x*y for y in it] for x in it ]
>>> m
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]



>>> it= (i for i in range(1,4))
>>> m = [[x*y for y in it] for x in it ]
>>> m
[[2, 3]]

'''


'''
https://blog.sideci.com/about-style-guide-of-python-and-linter-tool-pep8-pyflakes-flake8-haking-pyling-7fdbe163079d
5 different tools which are
pep8, pyflakes, flake8, haking, Pylint.

it is better to user Pycharm , Elipse , VS code, so you do no need to care about the tools.
they should already includ these tools
'''

'''
>>> l
[1, 2, 2]
>>> def ss(lll):
...   lll=[1,4,5]
...
>>> ss(l)
>>> l
[1, 2, 2]  ## not change
'''

'''
>>> def ss(lll):
...   lll.append(12)
...
>>> l = []
>>> ss(l)
>>> l
[12]  ###### changed !!!!!
>>>

'''
