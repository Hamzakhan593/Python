file = open("mast.txt", "r")
data = file.read()
print("data of te file  is: ", data)

# find word live in certificate txt
certificate  = open("certificate.txt", "r")
wordlive = certificate.read().lower()
if "live" in wordlive:
    print("word 'live' present in the certifficate")
else:
    print("NOT present")


# what happend we want to open non existing file
# it ll generate error not exist


# open a file in write mode
filewrite = open("Name.txt", "w")
filewrite.write("hamzaa khan")
# append will add content wile write will overwrite it
filewrite = open("Name.txt", "a")
filewrite.write(" \n or bi add karo \n hamza khaaaan")
# we must close file
filewrite.close()




