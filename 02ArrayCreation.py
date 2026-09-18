#np.zeros()-----------------------------------------------------------------------------------------
#zeros() creates an array where every value is 0.
import numpy as np
a = np.zeros(5)
print(a) #output: [0. 0. 0. 0. 0.]
print(a.ndim) #output: 1
print(a.shape) #output: (5,)
print(a.size) #output: 5
print(a.dtype) #output: float64

#Creating a 2D zero array
import numpy as np
b = np.zeros((3,4))
print(b) 
#output : [[0. 0. 0. 0.]
#          [0. 0. 0. 0.]
#          [0. 0. 0. 0.]]
print("dimension is=", b.ndim) #dimension is= 2
print("shape is =", b.shape) #shape is = (3, 4)
print("size is=", b.size) #size is= 12
print("datatype is=", b.dtype) #datatype is= float64

#100 students
#3 values per student
c=np.zeros((100,3))
print(c)
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
dimension is= 2
shape is = (3, 4)
size is= 12
datatype is= float64
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]"""


#np.ones()-----------------------------------------------------------------------------------------
#np.ones() creates an array where every value is 1
import numpy as np
a = np.ones(5)
print(a) #[1. 1. 1. 1. 1.]

#2D
import numpy as np
b= np.ones((2,3))
print(b)
#[[1. 1. 1.]
# [1. 1. 1.]]
print(b.ndim) #2
print(b.shape) #(2, 3)
print(b.size) #6
print(b.dtype) #float64


#Creating integer zeros/ones
import numpy as np
a = np.zeros((2,5),dtype=int)
print(a)
#[[0 0 0 0 0]
# [0 0 0 0 0]]
b = np.ones(5,dtype=int)
print(b) #[1 1 1 1 1]
print(a.dtype)#int64
print(b.dtype)#int64



#np.arange()---------------------------------------------------------------------------------------
#arange() works somewhat like Python's range()
import numpy as np
a = np.arange(5)
print(a) #[0 1 2 3 4]

b=np.arange(2,8)
print(b) #[2 3 4 5 6 7]

#Start, stop and step
import numpy as np
c = np.arange(1,11,2)
print(c) #[1 3 5 7 9]

d = np.arange(5,31,5)
print(d) #[ 5 10 15 20 25 30]

e = np.arange(2,20,4)
print(e) #[ 2  6 10 14 18]



#np.linspace()---------------------------------------------------------------------------------
import numpy as np
a = np.linspace(0,10,2)
print(a) #[ 0. 10.]

b = np.linspace(0,10,5)
print(b) #[ 0.   2.5  5.   7.5 10. ]



#Random arrays--------------------------------------------------------------------------------------------
import numpy as np
rng = np.random.default_rng()
a = rng.random(5)
print(a) #[0.5313975  0.88086381 0.85487311 0.28250387 0.69812988]

#random 2D array
import numpy as np
rng = np.random.default_rng()
a=rng.random ((3,5))
print(a)
#[[0.07869265 0.38929994 0.32406853 0.88757307 0.07966938]
# [0.43024899 0.30644442 0.12736004 0.7507535  0.64842354]
# [0.95178413 0.38252152 0.32569277 0.77595002 0.09622367]]
print(a.ndim) #2
print(a.shape) #(3, 5)
print(a.size) #15
print(a.dtype) #float64

#Random integers
import numpy as np
rng = np.random.default_rng()
a = rng.integers(1,10,size=5)
print(a) #[9 6 4 9 3]

#Random integer matrix
import numpy as np
rng = np.random.default_rng()
a = rng.integers(1,5,size=(3,3))
print(a)
#[[2 2 3]
# [4 2 1]
 #[3 1 1]]


#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------Exercises-------------------------------------------------------------
#Exercises 1 : Create an array containing 6 zeros. Print the array, ndim, shape, size, and dtype.
import numpy as np
a = np.zeros(6)
print(a)#[0. 0. 0. 0. 0. 0.]
print(a.ndim) #1
print(a.shape) #(6,)
print(a.size) #6
print(a.dtype) #float64


#Exercises 2 : Create a 3 × 4 array filled with ones. Print its shape and size.
import numpy as np
a = np.ones((3,4))
print(a)
#[[1. 1. 1. 1.]
 #[1. 1. 1. 1.]
 #[1. 1. 1. 1.]]
print(a.shape) #(3, 4)
print(a.size) #12


#Exercises 3 : Create this sequence using arange():0 5 10 15 20 25 30
import numpy as np
a = np.arange(0,31,5)
print(a) #[ 0  5 10 15 20 25 30]


#Excercise 4 : Create this sequence using arange():10 20 30 40 50
import numpy as np
a = np.arange(10,60,10)
print(a) #[10 20 30 40 50]


#Excersise 5 :Use linspace() to create 6 evenly spaced numbers from 0 to 100.
import numpy as np
a = np.linspace(0,100,6)
print(a) # [  0.  20.  40.  60.  80. 100.]


#Excersise 6 : Create a random integer array representing:
#5 students
#3 subjects
#marks between 40 and 100
#also print array,dimension,shape,size,data type,number of students and number of subjects
import numpy as np
rng = np.random.default_rng()
a = rng.integers(40,100,size=(5,3))
print(a)
"""[[55 43 42]
 [49 75 54]
 [77 45 68]
 [58 87 86]
 [92 93 82]]"""
print("dimension =",a.ndim) #dimension = 2
print("shape =",a.shape) #shape = (5, 3)
print("size =",a.size) #size = 15
print("data type =",a.dtype) #data type = int64
print("number of students=",a.shape[0]) #number of students= 5
print("number of subjects=",a.shape[1]) #number of subjects= 3A


#Excersise 7 :Create a random dataset X containing 10 samples and 4 features, with integer values from 0 through 100.
"""
ndim     = 2
shape    = (10, 4)
size     = 40
samples  = 10
features = 4"""

import numpy as np
x = np.random.default_rng()
x = x.integers(0,100,size=(10,4))
print(x)
"""[[21 40 67 91]
 [54 67 49 10]
 [66 96  6 20]
 [49 47 87 67]
 [31 72 97 97]
 [20 91 14 85]
 [45 40 87  9]
 [72  4 83 85]
 [71 91 10 40]
 [92 18 56 33]]
"""
print(x.ndim)
print(x.shape)
print(x.size)
print(x.shape[0])
print(x.shape[1])