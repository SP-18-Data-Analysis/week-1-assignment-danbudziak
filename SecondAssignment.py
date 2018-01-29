#-------------
#Daniel Budziak 
#Assignment 2
#Working with a matrix
#Due: February 1, 2018
#-------------

#Import numpy
import numpy as np

#Create a random matrix with 3 columns and five numbers
a = np.random.rand(3,5)

#Print out the matrix
print("Value of Matrix a: \n",a)

print(" ")
print(" ")

#Print out each individual column in the matrix
print("Here is the first column:")
print(a[0,:])
print("Here is the second column:")
print(a[1,:])
print("Here is the third column:")
print(a[2,:])
