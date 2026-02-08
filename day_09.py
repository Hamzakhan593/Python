import math


n = (input("how many Natural numbers do you want: "))
# for x in range(1, n+1):
#     print(x)
# print("\n")
# for i in range(n, 0, -1):
#     print(i)

# print("\n")

# for p in range(2, int(math.sqrt(n)) + 1):
#     if n % p == 0:
#         print("not a prime")
#         break
# else:
#     print("prime number")

# res = 1
# for f in range(n, 0  , -1):
#     res *= f
# print(res)


# fibbonaci series
# prev = 0
# after = 1
# res = 0
# for i in range(0,n):
#     if(i == 0):
#         print(i)
#     elif(i == 1):
#         print(i)
#     res = prev + after
#     prev = after
#     after = res
#     if(res >= 1):
#         print(res)

reverseN = n[::-1]
if(reverseN != n):
    print("string is not palindrome")
else:
    print("string is palindrome")

j = len(n)-1
for x in n:
    if(x != n[j]):
        print("Not Palindrom")
        break
    j -= 1
else:
    print("palindrom")