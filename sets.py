#python
#sets

#creating my set with my values

myset = {1, 67, 78, 34}
myset.add(65)
myset.add(1)  #duplicates are not allowed in set 
myset.add("1") #here 1 taken as string not as integer then length of the string changes
print(myset)
myset.remove(67)
myset.add(98)
print(myset.pop())
print(myset)
print(len(myset))

#input, output, import

Name = input("enter Name: ") #input function uses when i typed the str function stored in the variable name then i print it will be printed
print(Name)

Number = input("Enter the number: ")
print(Number)

#type function uses to tells us the what the function we uses 

Number = input("number: ")
print(type(Number))

Number1 = 7.8
print(type(Number1))

#convert strings to integers and floats

number = int(input("Enter a number: "))
print(type(number))


 #strings to floats

number3 = float(input("enter a number: "))
print(type(number3))

