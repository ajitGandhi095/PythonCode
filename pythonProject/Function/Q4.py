# Program for generating mul table for a given number by using function

def multable(n):
    if(n<=0):
        print("{} is Invalid Input".format(n))
    else:
        print("*"*50)
        print("Muliple table for: {}".format(n))
        print("*"*50)
        for i in range(1,11):
            print("{} * {} = {}".format(n,i,n*i))

# main program
multable(int(input("Enter a number for generating mul table: ")))