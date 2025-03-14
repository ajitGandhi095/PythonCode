# Define a Function for adding of two numbers

def SumOp(a,b):
    c=a+b
    return c

# main program
print("Type of SumOp=", type(SumOp))

#Get two values from keyboard
a=float(input("Enter First value: "))
b=float(input("Enter Second Value: "))
res= SumOp(a,b)
print("Sum({},{})= {}".format(a,b,res))