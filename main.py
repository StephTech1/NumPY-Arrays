#create a 1d array of numbers from 0-9
import numpy as np
print("A one dimensional array of numbers between 0 and 9")
onedim_array = np.arange(10)
print (onedim_array)
#create a 3x3 NumPy array of all True's 
import numpy as np
print("A 3 x 3 array")
array = np.array([1,2,3,4,5,6,7,8,9])
newArray = array.reshape(3,3)
print(newArray)
#Extract all off numbers from an array of 1-10

#subtract 1 from each of the numbers in the above array 
#convert a 1d array to a 2d array with 2 rows
#create two array a and b, stackthese two arrays vertically use the np.dot and np.sum to calculate totals