import os

with open("sample.txt", "w") as fd:
    fd.write("Hello")

if os.path.exists("sample.txt"):
    print "Exist"

if not os.path.exists("s.txt"):
    print "does not exist"

print os.path.getsize("sample.txt")

print os.path.isfile("sample.txt")

print os.path.isfile("smple.txt")

print os.path.dirname("sample.txt")

print os.path.isdir("/home/cg/root")

print os.path.realpath(__file__)
print os.getcwd()

filedir = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "baig"))

print os.getcwd()

print filedir

for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        print file
    if os.path.isdir(file):
        print file

print os.getpid()

os.mkdir("sam2")

print os.listdir(os.getcwd())

os.rmdir("sam2")

print os.listdir(os.getcwd())

os.rename("sam1", "sam3")

print os.listdir(os.getcwd())

os.system("your command here")

"""

sh-4.3$ python main.py
Exist
does not exist
5
True
False

True
/home/cg/root/main.py
/home/cg/root
/home/cg/root
/home/cg/root/baig
main.py
.cg_conf
sample.txt
anu
sam
sam3
62
['main.py', '.cg_conf', 'sample.txt', 'anu', 'sam', 'sam3', 'sam2']
['main.py', '.cg_conf', 'sample.txt', 'anu', 'sam', 'sam3']
Traceback (most recent call last):
  File "main.py", line 47, in <module>
    os.rename("sam1", "sam3")
OSError: [Errno 2] No such file or directory
"""