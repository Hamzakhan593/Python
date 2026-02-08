#tupple

x = ("apple", "banana", "mango")
print(x)
# from tuple to list
y = list(x)
print(type(y))
y.append("kuch or")
print(y)
x = tuple(y)
print(x)

# add tupple to a tupple
thistpple = ("a","b", "m")
x = x + thistpple
print(x)

# unpacking of a tupple
(a, b, m) = thistpple
print(a)
print(b)
print(m)



# set --->unique elements
myset = {1,2,3,4}
print(myset)
myset.add("hamza")
print(myset)
myset.update(x)
# for i in myset:
#     print(i)
myset.discard("hamza")
print(myset)

#union
set1 = {"a", "b", "c", 4}
set2 = {1,2,3,4,"c"}
set3 = set1.union(set2) #instead of union we can use | operator
print(set3)


# Set Methods
# Python has a set of built-in methods that you can use on sets.

# Method	Shortcut	Description
# add()	 -	Adds an element to the set
# clear() - Removes all the elements from the set
# copy() -  Returns a copy of the set
# difference() - Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns True if all items of this set is present in another set
#  	<	Returns True if all items of this set is present in another, larger set
# issuperset()	>=	Returns True if all items of another set is present in this set
#  	>	Returns True if all items of another, smaller set is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others





# dictionary
thisdict = {
    1 : "awais",
    2 : "hamza",
    4 : "jahangir"
}

print(thisdict)
print(thisdict[4])
# return all the keys
print(thisdict.keys())
# return all the values
print(thisdict.values())

#adding new element
thisdict[5] = "Iqra"
print(thisdict)

# retrun values in key pair form
print(thisdict.items())

# pop() removve value in dictionary with specified key
# thisdict.pop(2)

# loop through dictionary
for x in thisdict:
    print(thisdict[x])

for x in thisdict:
    print(x)

for x in thisdict.values():
    print()

for x in thisdict.keys():
    print(thisdict[x])


#copy a dictionary
xdict = dict(thisdict)
print(xdict)

ydict = thisdict.copy()
print(ydict)


# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary



#takiing input
input_day = input("Enter Days: ")
day = int(input_day)

# print(f"your name is: {day}")

# match statement
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")

    case _:
        print("you enter wrong day")
