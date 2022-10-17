a = [50,30]

b = [50,30]

c = a

print(a is c)#it returns true if both the variables are the same object pointing to same memory location

print(b is c)#it returns false although they have same values but not printing to same memory location

#not operator returns true if both variables are not the samme object

print(a is not c) #it returns false because a is same object as c

print(b is not c) #it returns true because b is not the same object as c

print(a!=b) #it returns false because a is equal to b


#membership operators

#These operators are used to test if a sequence is present or not in an object

x =[40,89,60,46,79]

print(60 in x)#in-->returns true if a sequence is present in an object

print(60 not in x)#not in-->it is false because not in operations is it returns true if a sequence is not present in an object





