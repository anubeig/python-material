## Example 2: Using recursion
def fib(n):
    a, b = 1, 1
    for i in range(n+1):
        print(i);
        a, b = b, a + b
    return a


print(fib(5));