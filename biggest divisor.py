n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))

difference = 0
if(n1 > n2):
    difference =  n1 - n2
else:
   difference = n2 - n1

for i in range(difference, 1, -1):
    if n1 % i == 0 and n2 % i == 0:
        print(f"Biggest Divisor is {i}")
        break