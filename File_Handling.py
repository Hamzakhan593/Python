# file = open("mast.txt", "r")
# data = file.read()
# print("data of te file  is: ", data)

# # find word live in certificate txt
# certificate  = open("certificate.txt", "r")
# wordlive = certificate.read().lower()
# if "live" in wordlive:
#     print("word 'live' present in the certifficate")
# else:
#     print("NOT present")


# # what happend we want to open non existing file
# # it ll generate error not exist


# # open a file in write mode
# filewrite = open("Name.txt", "w")
# filewrite.write("hamzaa khan")
# # append will add content wile write will overwrite it
# filewrite = open("Name.txt", "a")
# filewrite.write(" \n or bi add karo \n hamza khaaaan")
# # we must close file
# filewrite.close()


# if we use with then we dont need to close the file
with open("certificate.txt", "r") as f:
    data = f.read()
    print("file data: ",data)


# line by line execution
with open("Name.txt", "r") as name:
    line1 = name.readline()
    line2 = name.readline()
    line3 = name.readline()
    print("line 1", line1)
    print("line 2", line2)
    print("line 3", line3)
with open("Name.txt", "r") as n:
    lines = n.readlines()
    print(lines)
    print(len(lines))
    


    


