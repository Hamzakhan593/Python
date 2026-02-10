number = int(input("Enter Any Number to check Armstrong Number: "))
n = number
arr = []
i = 0
while n > 0:
    temp = n % 10
    arr.append(temp)
    i += 1
    n = n // 10

result = 0
length = len(arr)
temporary = 0


for x in arr:
    # result += x ** length
    result += pow(x,length)
print(result)


#[3,5,1]
# for x in arr:
#     length = len(arr)
#     temporary = 1

#     while length > 0:
#         temporary *= x          # 1*3, 3*3, 9*3 = 27 // 1*5, 5*5, 5*25 = 125
#         length = length - 1
#         print(f"temporary: {temporary}")
#         if(length == 0):
#             result = result + temporary     # 27 + 75 + 1 = 103,
#             print(f"result: {result}")


            

if(number == result):
    print(f"{number} is Armstrong Number")
else:
    print(f"{number} is  not an Armstrong Number")




