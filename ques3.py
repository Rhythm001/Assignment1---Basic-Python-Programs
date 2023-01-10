#Program to find the square root.

n = float(input("Enter the number here: "))

if(n<0):
    print("Square root of negative number is not possible.")
else: 
    a = n**(1/2)
    print("The square root of", int(n), "is:", a)