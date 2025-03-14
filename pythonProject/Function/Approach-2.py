# Define a function for substracting of two numbers

def subOp():
    # Take Input
    a=float(input("Enter first Value: "))
    b=float(input("Enter Second Value: "))

    #Process
    c= a-b

    #Display the Result
    print("Sub({},{})= {}".format(a,b,c))

#Main program
subOp()  # Function Call