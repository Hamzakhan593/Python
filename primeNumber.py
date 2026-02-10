n = int(input("Enter a Number: "))

for x in range(2, n+1):
    for j in range(2, x):
        if j < x:
           if x % j == 0:
              break
    else:
        (f"{x} is a prime number")
        