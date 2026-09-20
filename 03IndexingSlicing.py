#1D indexing and slicing


#Exercise 1--------------------------------------------------------------------------------------------------------------
import numpy as np
scores = np.array([60,65,78,71,80])
print(scores) #[60 65 78 71 80]
print(scores[1]) #65
print(scores[4]) #80
print(scores[-1]) #80
print(scores[0]) #60

#Exercise 2------------------------------------------------------------------------------------------------------------------------
#Print array
#The first temperature.
#The third temperature.
#The last temperature, using a positive index
temp = np.array([65,70,52,98,60])
print(temp[0]) #65
print(temp[2]) #52
print(temp[4]) #60

#Exercise 3---------------------------------------------------------------------------------------------------------------------------
#The prediction for the second house.
#The prediction for the fourth house.
#The prediction for the last house, calculating its positive index using .size.
house = np.array([32,35,37,38,31])
print("second house",house[1]) #second house 35
print("fourth house",house[3]) #fourth house 38
print("last house",house[house.size-1]) #last house 31

#Exercise 4 negative indexing.--------------------------------------------------------------------------------------------------------------------------
#The last score.
#The second-last score.
#The first score.
score = np.array([90,80,85,99,92])
print(score[-1]) #92
print(score[-2]) #99
print(score[-5]) #90

#Exercise 5 slicing---------------------------------------------------------------------------------------------------------------------------------------------
numbers = np.array([10,20,30,40,50])
print(numbers[1:4]) #[20 30 40]
print(numbers[2:5]) #[30 40 50]
#select the first three elements
print(numbers[0:3]) #[10 20 30]
#code using [:stop] to select only the first two elements
print(numbers[:2]) #[10 20]
#code using [start:] to select:[20 30 40 50]
print(numbers[1:]) #[20 30 40 50]
print(numbers[3:]) #[40 50]

#Excersise 6 slicing with a step--------------------------------------------------------------------------------------------------------
a = np.array([1,2,3,4,5,6,7])
print(a[0:5:2]) #[1 3 5]
print(a[::2]) #[1 3 5 7]
print(a[::3]) #[1 4 7]
print(a[::-1]) #[7 6 5 4 3 2 1]
print(a[::-2]) #[7 5 3 1]

#Excersise 7 modifying an element using indexing---------------------------------------------------------------------------------------------------------------
a = np.array([2,4,6,8,10])
a[0] = 1
print(a) #[ 1  4  6  8 10]

b = np.array([20,32,35,31,37,36])
b[0] = 17
b[-1] = 18
print(b) #[17 32 35 31 37 18]
# change 32,35 and 31 as 0
b[1:4] = 0
print(b) #[17  0  0  0 37 18]

#[10 21 31 41 50]
#The slice contains three positions, so we provide three replacement values:
# Index 1 receives 21
# Index 2 receives 31
# Index 3 receives 41
c = np.array([10,21,31,41,50])
print(c) #[10 21 31 41 50]
c[1] = 21
c[2] = 31
c[3] = 41
print(c) #[10 21 31 41 50]

d = np.array([1,2,3,4,5])
print(d) #[1 2 3 4 5]
d[1:4] = 6,7,8
print(d) #[1 6 7 8 5]



original = np.array([10,20,30,40,50])
part = original[1:4]
print(original) #[10 20 30 40 50]
part[0] = 60
print(part) #[60 30 40]

#.copy()
import numpy as np
original = np.array([10, 20, 30, 40, 50])
part = original[1:4].copy()
part[0] = 60
print(part) #[60 30 40]
print(original) #[10 20 30 40 50]

#TASK----------------------------------------------------------------------------------------------------------------------------------------
#[72, 75, 78, 200, 81, 84, 87]
#Print the first prediction using positive indexing.
#Print the latest prediction using negative indexing.
#Print the first three predictions using slicing.
#Print every second prediction using slicing.
#Change 200 to 80 using indexing.
#Create an independent copy of the last three predictions.
#Change the first value in the copied array to 100.
#Print both the copied array and the original array to prove that the original was not affected by step 7.
import numpy as np
prediction = np.array([72,75,78,200,81,84,87])

print(prediction[0]) #72

print(prediction[-1]) #87

print(prediction[0:3]) #[72 75 78]

print(prediction[0:7:2]) #[72 78 81 87]
#or
print(prediction[::2])

prediction[3] = 80
print(prediction) #[72 75 78 80 81 84 87]

last3 = prediction[4:7].copy()
print(last3) #[81 84 87]
#or
last3 = prediction[-3:]
print(last3)

last3[0] = 100
print(last3) #[100  84  87]

print(prediction) #[72 75 78 80 81 84 87]
print(last3) #[100  84  87]
