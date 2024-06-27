"""Write a program to accept two inputs from the keyboard and find the greatest of two number"""

a,b=[int(x) for x in input("Enter two numbers from the keyboard::").split(",")]
if a > b:
    print("{} is greater than {}".format(a,b))
else:
    print("{} is greater than {}".format(b,a))
