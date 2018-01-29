#1/23/18
a = [1,3,5,6,8,10]

print(a[0]) #prints 1 

print(a[2:]) #prints from index 2 onward

print(a[-3]) #prints third from last

print(a[-3:]) #prints third from last to the end of the list

print(a[0:1]) #prints first index

#delete and insert at the same time
#a[0:2] = [23,45,51]#adds 51 because we are only replacing indexes 0 and 1
print(a)

a[len(a):] = [23,47,96] #basically appends or adds those to the end of the list
print(a)




b = [ 1, 3, ['a','b','c', ["Hello"]], 23.0, 4 ]

#print(b[2][3][0]) #prints the hello


#using the map function
c = [2,1,6,-10,15,26,-4]

c.sort()
print(c)
print(list(reversed(c)))


iterVar = map(abs,[-1,4,5,3])

for i in iterVar :
	print(i)

d = "This is the python programming class"
doutput = [i for i in d]
print(d)

#Dictionaries
dictionaryVar = {0: 'Python', 1: 'Course' } 

for i in dictionaryVar :
	print(i)