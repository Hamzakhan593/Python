def my_func(name):
    print(f"Name: {name}")

#if youu dont know how many argument wwiil be paassed in function
def my_func1(*name):
    print(f"Name ---> {name}")


def my_func2(name):
    for x in name:
        print(f"Name: {x}")

def my_func3(x):
    return(3 * x)


my_func("hamza")
my_func("umar")
my_func("hirra")
my_func("hassan")

my_func1("jahanzeb", "bilal", "awais")

name = {"hamza", "umar", "bilal", "jahanzeb"}
my_func2(name)

print(my_func3(3))
print(my_func3(1000))
print(my_func3(23632))
