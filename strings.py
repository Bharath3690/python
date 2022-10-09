#strings

#uppercase

x = "Good morning friends"

print(x.upper())

print(x.lower())  # lower case 

#remove white spaces

x = "    complete our work"
print(x.strip())

x='Hunting fish'
print(x.replace('H','A'))


x = 'I love my country'
print(x.split())

#slicing

x='I read an article '
y=x.split()
print(y[2])
print(y[2:5])

#negativty
print(y[-3])
print(y[-3:-5])


x="my world"
y="is you"

z=x+" "+y
print(z)

#boolean function

print(bool(20)) #if their is any value in bool function then it is always true if there is false or an empty spaces none or o type then it shows false
print(bool(True))
# these show true

print(bool())
print(bool(None)) #these shows false 
print(bool(0))
print(bool(False))

#list
myList=['bharath',10,20,40,'moulipavan']
myList[1:3]=[200,300]
print(myList)
print(myList[2])
print(type(myList))
print(len(myList))
print(myList[2:5]) # (search starting from index 0 and then 0,1,2,.... so on but it cant exclude the last index what we given)


#extend(add files from another list to current list )
list1 = [10,20,30,40,50]
list2 = [60,70,80,90,100]
list1.extend(list2) 
print(list1)
print(list2[-3])
print(list1[2])

#replace
list6 = [10,20,30]
list6[1:3] = ["love","hate"]
print(list6)

#insert items
list7 = [20,50,70]
list7.insert(30,40)
print(list7)

#append(adding items at end of list)
list8 = [80,90,10,40]
list8.append(50)
print(list8)

#Remove list
#remove a specified item
list3 = ["guava","grapes","pineapple"]
list3.remove("grapes")
print(list3)
print(list3[1])

list9 = ["john","peter","robin"]

list9.pop(1)  #pop
list9.pop() #(if we cant indicate any index on pop then it will remove last item )
print(list9)

myList1 = ["john","manoj","pavan","mouli"]
del myList1 #delete
print(myList1)


list5 = ['hello',"github","123","love"]
list5.clear() #clear 
print()










