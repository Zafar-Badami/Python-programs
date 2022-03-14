name = input("Name: ")
balance = 100.50

#Method 1:
print(name+" has $"+str(balance))

#Method 2:
print("%s has $%f"%(name,balance))
print("%-10s has $%.2f"%(name,balance))

#Method 3:
print("{} has ${}".format(name,balance))
print("{} has ${:.2f}".format(name,balance))
print("{:<10} has ${:.2f}".format(name,balance))
print("{:>10} has ${:.2f}".format(name,balance))
print("{:^10} has ${:.2f}".format(name,balance))
print("{:*^10} has ${:.2f}".format(name,balance))

------------------------
#List is a collection of data of different types
#list is ordered
#list is indexed
#list is changeable 
#list allows duplicates

#Create a list
mylist = ["Tom",25,250.5]
list2 = list(["bank","account"])

#Print a list
print(mylist)
print(list2)

#Length of a list
length = len(mylist)
print("My list length = "+str(length))


#Access list elements
print("First: "+mylist[0])
print("Last: "+str(mylist[length-1]))

#Modify list elements
mylist[length-1] = 88.5
mylist[1] = "$"
print(mylist)

#Add elements to a list
mylist.insert(1,"has")
mylist.append("AUD")
print(mylist)

copylist = mylist.copy()
print(copylist)

newlist = copylist + list2
print(newlist)

newlist.remove("account")
print(newlist)
newlist.pop()
print(newlist)
newlist.pop(1)
print(newlist)
del newlist[len(newlist)-1]
print(newlist)

del newlist
try:
    print(newlist)
except NameError:
    print("list no longer exists")
