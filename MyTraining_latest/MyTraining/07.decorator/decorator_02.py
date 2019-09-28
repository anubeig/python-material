"""
Sample 1 - Adding $ to the return value from price() function
If we want a function that does prefix '$', the decorator can help us:
"""


def dollar(fn):
    def new(*args):
        return '$' + str(fn(*args))

    return new


@dollar
def price(amount, tax_rate):
    return amount + amount * tax_rate


print price(100, 0.1)
"""
Output:

$110
The dollar decorator function takes the price() function, and returns enhanced the output from the original price() after modifying the inner working.
Note that the decorator enables us to do it without making any changes on the price() function itself.

So, decorator works as a wrapper, modifying the behavior of the code before and after a target function execution,
without the need to modify the function itself, enhancing the original functionality.
"""