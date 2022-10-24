mylist = [1,3,5,7,8,3]
print(mylist)


mylist.sort() #updates the list means remove the repeated numbers

mylist.reverse() #updates the list by reversing the numbers

mylist.append(4) #update my list and adds 8 at the end of the list

mylist.insert(6,4) #this will add 8 at 3 index

mylist.pop(3) #will delete the value at index 2 and returns the value

mylist.remove(3)#remove 3 from the mylist

#tuples in python 
# A tuple is an immutable data (cannot change) type in python

x= () #empty tuple

print(x)

y=(1,) #tuple with only one element needs comma

print(y)


z=(1,7,5) #tuple with more than one element

print(z)


#tuples method
b=(2,2,3,3,3,4,5,)


b.count(3) #b.count[3] will return number of times 3 occur in b

c=(4,5,6,5,4,4,5)

c.index(2) #c.index(2) will return the index of first occurence of 2 in c

