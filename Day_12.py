n = int(input("How many Fibbonacci Number Do you want: 12"))

previous = 0
after = 1
result = 0
print(previous)
print(after)
for i in range(n, 0, -1):
    result = previous + after
    print(result)
    previous = after
    after = result