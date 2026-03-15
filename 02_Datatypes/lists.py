chai = ["green", 'black', 'white', 'masala']
print("Start")
'''
>>> chai = ["green", 'black', 'white', 'masala']
>>> chai[0]
'green'
>>> chai[1:]
['black', 'white', 'masala']
>>> chai
['green', 'black', 'white', 'masala']
>>> chai[1:2]= []
>>> chai
['green', 'white', 'masala']
>>> chai[1:2] = ['BLACK']
>>> chai 
['green', 'BLACK', 'masala']
>>> chai[2:2] = ['white']
>>> chai
['green', 'BLACK', 'white', 'masala']
>>> chai.pop()
'masala'
>>> chai
['green', 'BLACK', 'white']
>>> chai.append('white']
  File "<stdin>", line 1
    chai.append('white']
                       ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> chai.append('white')
>>> chai
['green', 'BLACK', 'white', 'white']
>>> chai.insert(0,'pokemon')
>>> chai
['pokemon', 'green', 'BLACK', 'white', 'white']
>>> chai.delete(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai.delete(0)
    ^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'delete'
>>> chai.remove(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai.remove(0)
    ~~~~~~~~~~~^^^
ValueError: list.remove(x): x not in list
>>> chai.remove("pokemon")
>>> chai
['green', 'BLACK', 'white', 'white']
>>> chai.delete("white")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai.delete("white")
    ^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'delete'
>>> chai
['green', 'BLACK', 'white', 'white']
>>>
>>> 
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> ^Z
'''

print('End')