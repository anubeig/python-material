def fun():
    return 10,20
    pass
res = fun()
print type(res)

"""
output;
sh-4.3$ python main.py
<type 'tuple'>
"""

def fun(*args,**kargs):
    print type(args)
    print type(kargs)
    pass

fun(10,20)

"""
output:-
sh-4.3$ python main.py
<type 'tuple'>
<type 'tuple'>
<type 'dict'>
"""
