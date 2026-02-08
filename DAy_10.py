n = 123456
arr = []
str1 = ""
reminder = 0
while n > 0:
    reminder = n % 10
    str1 += str(reminder)
    arr.append(reminder)
    n = n // 10

print(arr)
print(int(str1))