Python's *.py file is just a text file in which you write some lines of code. When you try to execute this file using say "python filename.py"

This command invokes Python Virtual Machine. Python Virtual Machine has 2 components: "compiler" and "interpreter". Interpreter cannot directly read the text in *.py file, so this text is first converted into a byte code which is targeted to the PVM (not hardware but PVM). PVM executes this byte code. *.pyc file is also generated, as part of running it which performs your import operation on file in shell or in some other file.

If this *.pyc file is already generated then every next time you run/execute your *.py file, system directly loads your *.pyc file which won't need any compilation(This will save you some machine cycles of processor).

Once the *.pyc file is generated, there is no need of *.py file, unless you edit it.