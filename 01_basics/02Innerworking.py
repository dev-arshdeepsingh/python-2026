#Make sure to not name modules starting with no., Below was 01hello but was giving errors and hence changed to hello.py
from intro import chai
chai("Ginger tea")

'''
Python's innerworking-
1. Normal python file is converted(or compiled(just a jargon)) to a bytecode file.
2. A bytecode file is an intermediate low level(not machine code) file which is platform 
independent i.e it can run on any machine(windows, mac,linux, android etc) which has a
python virtual machine(VM).
3. Bytecode file is mostly hidden file it is only visible only in certain cases like while
 importing methods from another files.
4. Bytecode runs fster, its extension is .pyc(compiled python) which involves frozen
 binaries(no idea)
5. Bytecode files are hidden and stored in folders with names starting with double under-
-score(like __pycache__), these underscores displays that its some inner python stuff.
6. Now if we create multiple files which involves __pycache__ then only the new updates will be pushed
in pycache, while the non-changed stuff remains the same just like github.
7. Example of bytecode: hello.cpython-314.pyc
hello is file name, cpython is standard python version, 314 is python version(3.14)
8. Nowadays, these .pyc files are only created for imported files not in top level files.
'''

#PVM:-
