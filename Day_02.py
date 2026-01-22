str = "hamza khan pathan"
print(len(str))

if "hamza" in str:
    print("yes")


#slicing
# from 7th to 15
print(str[6:15])
# from 0 to 10
print(str[:10])
#from 11 to last
print(str[10:])

#slicing from negative
#ab ham last side se gineingy jahan pe 10 elements poorry hojayn os se ly kr start tak print kar leingy
print(str[:-10])
#aab bi ham last se gineingy par jahan 10 poory hojayn wahan se ly kr akhri tak print kar leingy
print(str[-10:])

#upper case
print(str.upper())
print(str.lower())

#replacing string
print(str.replace("p", "P"))

#split
print(str.split(" "))

#string concantenation
a = "address"
c = a + " " + str
print(c)

#f string
age = 22
text = f"i am {age} years old"
print(text)

print(f"multiplying 2 and 3 = {2*3}")

#f string by print point value

print(f"point value {age:.4f}")

#escap characters
print("we are \"proud\" to say")
print("we are \'proud\' to say")
print("we are \\ proud to say")



