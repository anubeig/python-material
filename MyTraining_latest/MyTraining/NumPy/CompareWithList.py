"""
We use python numpy array instead of a list because of the below three reasons:

1)Less Memory
2)Fast
3)Convenient
"""
import numpy as np

import time
import sys

list1 = [i for i in range(100000)]
print(list1)

"Comparing size"
print(sys.getsizeof(list1))
print(sys.getsizeof(np.arange(100000)))

"Comparing time"
SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [x+y for x, y in zip(L1, L2)]
print((time.time() - start) * 1000)
#print(result)

start = time.time()
result = A1 + A2
print((time.time() - start) * 1000)
#print(result)

"""
In the above code, we have defined two lists and two numpy arrays. 
Then, we have compared the time taken in order to find the sum of lists and sum of numpy arrays both. 
If you see the output of the above program, there is a significant change in the two values. 
List took 380ms whereas the numpy array took almost 49ms. Hence, numpy array is faster than list. 
Now, if you noticed we had run a ‘for’ loop for a list which returns the concatenation of both the lists 
whereas for numpy arrays, we have just added the two array by simply printing A1+A2. 
That’s why working with numpy is much easier and convenient when compared to the lists.

Therefore, the above examples proves the point as to why you should go for python numpy array rather than a list!

Moving forward in python numpy tutorial, let’s focus on some of its operations.
"""