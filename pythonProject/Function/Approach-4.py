#Define a function for divide two numbers

def divOp():
    # taken input from keyboard
    a=int(input("Enter First value: "))
    b=int(input("Enter Second Value: "))

    #Process input
    c=a/b

    return a,b,c
#Main program

a,b,c=divOp() # function call with multiple assignment
print("Div({},{})= {}".format(a,b,c))

print("------------------OR------------------")
res=divOp() #function call with single argument
print("div({},{})= {}".format(res[0],res[1],res[2]))
print("-----------------------OR------------------------")
print("div({},{})= {}".format(res[-3],res[-2],res[-1]))

