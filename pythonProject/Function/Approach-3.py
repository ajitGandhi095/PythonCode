#Define a function for multiplying two numbers

def mulOp(a,b):
    #Process the input
    c=a*b
    print("Mul({},{})= {}".format(a,b,c))

#main Program

#get the value from keyboard
a=int(input("Enter First value: "))
b=int(input("Enter Second Value: "))
mulOp(a,b)
