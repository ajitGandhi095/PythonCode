def decideType(value):
    if(type(value)== int):
        print("{} is int type value".format(value))
    elif(type(value)== float):
        print("{} is float type value".format(value))
    elif(type(value)== bool):
        print("{} is bool type value".format(value))
    elif(type(value)== complex):
        print("{} is complex type value".format(value))
    elif(type(value)== str):
        print("{} is str type value".format(value))
    elif(type(value)== bytes):
        print("{} is bytes type value".format(value))
    elif(type(value)== bytearray):
        print("{} is bytearray type value".format(value))
    elif(type(value)== range):
        print("{} is range type value".format(value))
    elif(type(value)== list):
        print("{} is list type vaue".format(value))
    elif(type(value)== tuple):
        print("{} is tuple type value".format(value))
    elif(type(value)== set):
        print("{} is set type value".format(value))
    elif(type(value)== frozenset):
        print("{} id frozenset type value".format(value))
    elif(type(value)== dict):
        print("{} is dict type value".format(value))
    elif type(value) not in [int, float, bool, complex, str, bytes, bytearray, range, list, tuple, set, frozenset, dict]:
        print("{} is None type value".format(value))

# main program
decideType(10)
decideType(2+3j)
decideType([10,20,30])
decideType(10.56)
decideType("Python")
decideType(range(10,20,2))
decideType(bytes([10,20,30]))
decideType(bytearray([10,20,30]))
decideType(("Python", "Function"))
decideType({10:"Python", 20:"Numpy", 30:"Pandas", 40:"Matplotlib"})
decideType({10,30,40,60})
decideType(frozenset({10,30,70}))
decideType(None)
print("---------------------------")