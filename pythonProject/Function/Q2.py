# Program for finding sum and average of list of values by using function

def readValues():
    nov= int(input("Enter how many values sum & average u want to find: "))

    if(nov<=0):
        return [] # returning empty list or return list()
    else:
        lst=[]
        for i in range(1,nov+1):
            val= float(input("Enter {} values: ".format(i)))
            lst.append(val)
        return lst

def findSumAvg():
    if(len(lst)==0):
        print("No values present-- can't find sum and average")

    else:
        sum=0
        for val in lst:
            sum=sum+val
        else:
            print("-----------------------------")
            print("Given list of elements={}".format(lst))
            print("Sum= {}".format(sum))
            print("Average= {}".format(sum/len(lst)))
            print("-----------------------------")

#main program

lst= readValues()  # function call
findSumAvg()  # function call