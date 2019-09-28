"""
You can use .apply to send a single column to a function.

"""
import pandas as pn
import numpy as np
rectangles = [
    { 'height': 40, 'width': 10 },
    { 'height': 20, 'width': 9 },
    { 'height': 3.4, 'width': 4 }
]


rectangles_df = pn.DataFrame(rectangles)
"Appliying single column"
print(rectangles_df.apply(np.sum))
    
"Sending each row"
rectangles_df['sumOfRow'] = rectangles_df.apply(np.sum,axis=1)
print(rectangles_df)