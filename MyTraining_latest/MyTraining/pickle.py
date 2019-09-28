#https://pythontips.com/2013/08/02/what-is-pickle-in-python/
"""
In this post i am going to tell you about pickle. It is used for serializing and de-serializing a Python object structure.
Any object in python can be pickled so that it can be saved on disk.
What pickle does is that it “serialises” the object first before writing it to file.
Pickling is a way to convert a python object (list, dict, etc.) into a character stream.
The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.

So lets continue:

1. First of all you have to import it through this command:

import pickle
pickle has two main methods. The first one is dump, which dumps an object to a file object and the second one is load, which loads an object from a file object.

2. Prepare something to pickle:
Now you just have to get some data which you can pickle. For the sake of simplicity i will be pickling a python list. So just read the below code and you will be able to figure it out yourself.
"""
import pickle

a = ['test value','test value 2','test value 3']
a
['test value','test value 2','test value 3']

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name,'wb')

# this writes the object a to the
# file named 'testfile'
pickle.dump(a,fileObject)

# here we close the fileObject
fileObject.close()
# we open the file for reading
fileObject = open(file_Name,'r')
# load the object from the file into var b
b = pickle.load(fileObject)
b
['test value','test value 2','test value 3']
a==b
True


"""Another Example:-
import pickle
list1 = ["a",1,2,3]
with open("sample.txt","w") as f:
    pickle.dump(list1,f)

with open("sample.txt","r") as f:
    list2 = pickle.load(f)
print type(list2)
print list2
"""