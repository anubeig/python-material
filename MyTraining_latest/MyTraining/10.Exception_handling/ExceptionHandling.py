try:
    a = 5/0
except Exception as e:
    print(e)

try:
    a = 5/0
except Exception as e:
    print(e)
finally:
    print("Final block")

#If use return in try block ,except block wont execute but final block get execute
def exam():
    try:
        a = 5/0
        return 0
    except Exception as e:
        print(e)
    finally:
        print("Final block of Exam")
exam()

#if we use exit() function in try block, then finally block wont execute as well as except block also.
def exam02():
    try:
        a= 5/0
        exit()
    except Exception as e:
        print(e)
    finally:
        print("Final block of Exam02")

#In python u can give except class in any manner but in java first Arithmetic excpetion follows Exception,
# we cannot give Excption class follows Arithemetic Exception
try:
    a = 5/0
except Exception as e:
    print(e)
except ArithmeticError as e:
    print(e)


#Nested Exception

try:
    try:
        pass
    except:
        pass
    a = 5/0
except Exception as e:
    print(e)

#raise exception You can explicitly throw an exception in Python using ?raise? statement.
# raise will cause an exception to occur and thus execution control will stop in case it is not handled.
try:
    raise Exception("Hello")
except Exception as e:
    print(e)


try:
    raise Exception("Hello")
except Exception as e:
    print(e)
else:
    print("else")

#Exception propagation
#An exception is first thrown from the top of the stack and if it is not caught, it drops down the call stack to the previous method,If not caught there,
# the exception again drops down to the previous method, and so on until they are caught or until they reach the very bottom of the call stack.
# This is called exception propagation.

#Example 01

def Exam():
    raise Exception("Hello")

try:
    Exam()
except Exception as e:
    print(e)


#Example 02

def Exam01():
    raise Exception("Hello")

def Exam02():
    Exam01()
    print("bye")     # This line wont print because execption is caught so control jump to except block of the Exam03

def Exam03():
    try:
        Exam02()
    except Exception as e:
        print(e)


# else block after try ,except block but before finall block , if execption doesnt occur then else block get executed
try:
    a = 5/1
except Exception as e:
    print(e)
else:
    print("Ok")
finally:
    print("Final block")
