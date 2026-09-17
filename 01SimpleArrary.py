## Exercise 1: 1D Array
import numpy as np
arr = np.array([10,24,55,70,84])
print(arr)
#output : [10 24 55 70 84]

#now printing the dimension,shape,size and type of the array

print("dimension of the array is:",arr.ndim)
#output : dimension of the array is: 1

print("shape of the array is:",arr.shape)
#output : shape of the array is: (5,)

print("size of the array is:",arr.size)
#output : size of the array is: 5

print("the data type of the array is:",arr.dtype)
#output : the data type of the array is: int64


#Exercise 2: Student Marks------------------------------------------------------------------------------------------------
#            Math   Physics   CS

#Student 1     80      75     90
#Student 2     70      85     88
#Student 3     92      89     95
#now printing the array,dimentions,shape ,size and type of the array

import numpy as np
a = np.array(([80,70,90],
              [70,85,88],
              [92,89,95]))
print(a)
#output : [[80 70 90]
#          [70 85 88]
#          [92 89 95]]

print("dimension of the array is:",a.ndim)
#output : dimension of the array is: 2

print("shape of the array is:",a.shape)
#output : shape of the array is: (3, 3)

print("size of the array is:",a.size)
#output : size of the array is: 9

print("the data type of the array is:",a.dtype)
#output : the data type of the array is: int64


#Exercise 3: 5 x 2 Array------------------------------------------------------------------------------------------------
import numpy as np
b=np.array(([10,20],
            [30,40],
            [50,60],
            [70,80],
            [90,100]))
print(b)
print(b.ndim) # output:2
print(b.shape)# output:(5, 2)
print(b.size)# output:10
print(b.dtype)# output:int64

#Exercise 4: 4 x 3 Array-------------------------------------------------------------------------------------------------
"""[10, 15, 20],
    [25, 30, 35],
    [40, 45, 50],
    [55, 60, 65]"""
#1. x.ndim = ?
#2. x.shape = ?
#3. x.size = ?
#4. x.dtype will probably be what type?
#5. number of rows = ?
#6. number of columns = ?
import numpy as np
x = np.array(([10,15,20],
              [25,30,35],
              [40,45,50],
              [55,60,65]))
print("x.ndim:",x.ndim) #output: x.ndim: 2
print("x.shape:",x.shape) #output: x.shape: (4, 3)
print("x.size:",x.size) #output: x.size: 12
print("x.dtype will probably be what type:",x.dtype) #output: x.dtype will probably be what type: int64
print("number of rows:",x.shape[0]) #output: number of rows: 4
print("number of columns:", x.shape[1]) #output: number of columns: 3
