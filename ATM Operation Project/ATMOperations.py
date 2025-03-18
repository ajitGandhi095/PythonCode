#ATMOperations.py <---- File Name and Module Name
from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal= 500.00   #Global Variable
def Deposit():
    damt=int(input("Enter Your Deposit Amount: "))   #Implicitly raises ValueError in the case of alnums, strs and symbols
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal= bal + damt
        print("Your Account xxxxxxxxx086 Credited with INR:{}".format(damt))
        print("Now Your Current Bal in xxxxxxxxx086 INR:{}".format(bal))
def Withdraw():
    global bal
    wamt=int(input("Enter Your Withdraw Amount: "))  #Implicitly raises ValueError in the case of alnums, strs and symbols
    if(wamt<=0):
        raise WithdrawError
    elif(wamt+500>bal):
        raise InSuffFundError
    else:
        bal= bal - wamt
        print("Your Account xxxxxxxxx086 Debited with INR:{}".format(wamt))
        print("Now Your Current Bal in xxxxxxxxx086 INR:{}".format(bal))
def Balenq():
    print("Now Your Current Bal in xxxxxxxxx086 INR:{}".format(bal))