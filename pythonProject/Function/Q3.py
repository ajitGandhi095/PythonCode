# Program for finding sum and average of list of values by using function

def readValues():
    nov=int(input("Enter how many values sum & avg u want to find: "))

    if(nov<=0):
        return [] # returning empty list
    else:
        lst=[]
        for i in range(1,nov+1):
            val= float(input("Enter {} value: ".format(i)))
            lst.append(val)
        return lst

def findSumAvg():
    lstobj= readValues()
    if(len(lstobj)==0):
        print("No value present-- can't find")
    else:
        sum=0
        for val in lstobj:
            sum=sum+val
        else:
            print("----------------------------")
            print("Given List of Values={}".format(lstobj))
            print("Sum={}".format(sum))
            print("Average={}".format(sum/len(lstobj)))
            print("----------------------------")

#main Program

findSumAvg()  # Function call