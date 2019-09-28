import sys

print type(sys.argv)
print sys.argv[0]

"""
sh-4.3$ python main.py
<type 'list'>
main.py  
"""

#raw_input always return string where as input returns integer if value is not inserted in quotes.
name = raw_input("what is your name ?")

print type(name)

age = raw_input("what is your age ?")

print type(age)

age = input("what is your age ?")

print type(age)


"""
sh-4.3$ python main.py
<type 'list'>
<type 'tuple'>
what is your name ?anu
<type 'str'>
what is your age ?8
<type 'str'>
what is your age ?8
<type 'int'>
"""