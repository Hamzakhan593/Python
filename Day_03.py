# boolean values

a = 10
b = 13
if a > b:
    print("a is greater")
elif a == b:
    print("both are equal")
else:
    print("b is greater")

#List in python

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(len(thislist))
print(type(thislist))
print(thislist[-2])
print(thislist[-1])
print(thislist[2:5])
print(thislist[0])
print(thislist[:6])
print(thislist[3:])

#negative indexing
print(thislist[-2:-6:-1])

newlist = ["hamza", "jahanzeb", "shahzeb"]
newlist[0] += " khan"
print(newlist)
newlist[0] = "hamza khan"
print(newlist)
newlist[0:2] = ["hamzachange", "jahanzebchange"]
print(newlist)


#inserting value at specified location in the list
newlist.insert(2, "insertingvalue")
print(newlist)

#inserting value at the end of the list
newlist.append("insert end")
print(newlist)

#inserting value from one list to anoother
extendlist = ["one", "two"]
extendlist.extend(newlist)
print(extendlist)

#inserting tuple value into list also uses extend keyword
tuplelist = ("tuple1", "tuple2")
extendlist.extend(tuplelist)
print(extendlist)

#remove keyword remove the specified element like tuple1 from list
# extendlist.remove("tuple1")

#pop remove the specific index otherwisse remove last element
# extendlist.pop(2)

#del also remove specified index value or delete the complete list
# del extendlist[4]

#clear empities the list but not a list
# extendlist.clear()

#loop on a list
for x in extendlist:
    print(x)

for i in range(len(extendlist)):
    print(i)

i = 0
while i < len(extendlist):
    print(extendlist[i])
    i = i + 1

#sorting list
extendlist.sort()
print(extendlist)
#sorting in reverse order
extendlist.sort(reverse=True)
print(extendlist)


# reversse method is used to reversse the list

#copying a list using copy() keyword
copylist = []
copylist = extendlist.copy()
print(copylist)

#copying list using list keyword
copylist2 = []
copylist2 = list(extendlist)
print(copylist2)

#copy a list using slice operator
copylist3 = []
copylist3 = thislist[:]
print(copylist3)

#join or concantenation os list
# method one ---> newlist = list1 + list2
# method two ---> use looping
# method three ---> extend() keyy word


numArr = [1,2,3,4,5,6,7]
for i in range(len(numArr)):
    print(numArr[i])


# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
