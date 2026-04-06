#If possible run this file in shell
# open 05_Iteration_BTS in integrated terminal

'''  Method -1
f = open('chai.py')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
'''

''' #Method -2 (RAW)
f = open('chai.py')
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
'''

'''#Method-3 (Best and clean)

for line in open('chai.py'):
    print(line)

'''


#Method 5 (Using While loop)
'''
f = open('chai.py')
while True:
    line = f.readline()
    if not line:
        break
    else:
        print(line, end = '')
'''



#------------------------------------------------------------------------------------------
#Diff. of iter() in list vs files

#List
l1 = [1,2,3,4]
#print(l1.__next__())       #Wont work until iter() is used, ie its not iterable by default we have to make it iterable using iter() method
L1 = iter(l1) #Now next() method can work on it.


print(L1) #Points to memory location of first element
print(id(l1[0])) #The memory loc and adress are diff. things

print(L1.__next__())   #Now it returns 1
print(L1.__next__())  # Now it returns 2
print(L1.__next__())   #Now it returns 3
print(L1.__next__())  # Now it returns 4
#print(L1.__next__())   #Now it returns "StopIteration" error




#Files
f = open('chai.py')
print(f.__next__()) #Works without using iter() as file is always iterable hence iter() method works by default
# In terminal, 1. cd 05_Iteration_BTS      2.python chai2.py  Then this will run. No reason just VS code glitch

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
#print(f.__next__()) #Stop iteration error


f1 = iter(f)
print(f1)
print(f1.__next__()) #Works in continuity to print(f.__next__()) ie f and iter(f) are same

#Checking: 
if L1 is l1:
    print("True OP")
else:
    print("False OP")

#Returns False for list


if f1 is f:
    print("True OP")
else:
    print("False OP")
#Returns True for list

#--------------------------------------------------------------------------------------------

#Summary:
# Normal list & iter(list) are different entities which tells us that lists can be iterable as well as non-iterable.
# Normal file.txt and iter(file.txt) are same, which tells files are always iteratable
