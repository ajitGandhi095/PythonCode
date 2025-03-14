# IterableObjectwithFunctionEx1

def displayValues(obj):
    print("Type of obj= ",type(obj))
    print("Number of values= {}".format(len(obj)))
    print("------------------------------")
    if(type(obj)== dict):
        for key, val in obj.items():
            print("\t{}----> {}".format(key, val))
    else:
        for val in obj:
            print(val)
    print("-------------------------")

#main program
lst=[10, "Rossum", True, 2+3j, 34.56]
displayValues(lst)

tpl= (10,"Travis", True, 34.56, 2+3j)
displayValues(tpl)

st={10, "Rossum", 34.56, True, 2+3j}
displayValues(st)
displayValues(())
displayValues([])
displayValues({})
displayValues(set())
print("------------------------")
d= {10:"Python", 20:"Numpy", 30:"Pandas", 40:"Matplotlib", 50:"DJango"}
displayValues(d)