#ATM.py<--- File Name and Module Name(Package)
from ATMMenu import Menu
from ATMExcept import DepositError,WithdrawError,InSuffFundError
from ATMOperations import Deposit,Withdraw,Balenq
def project():
    while(True):
        Menu()
        try:
            ch=int(input("Enter Your Choice: "))
            match(ch):
                case 1:
                    try:
                        Deposit()
                    except ValueError:
                        print("\tDon't try to deposit alnums, strs, symbols and float amount--Invalid Deposits--try again")
                    except DepositError:
                        print("\tDon't try to deposit Negative and Zero Amount--try again")
                case 2:
                    try:
                        Withdraw()
                    except ValueError:
                        print("\tDon't try to deposit alnums, strs, symbols and float amount--Invalid Deposits--try again")
                    except WithdrawError:
                        print("\tDon't try to withdraw Negative and Zero Amount--try again")
                    except InSuffFundError:
                        print("\tYour Account xxxxxxxxx086 does not sufficient Funds--try again")
                case 3:
                    Balenq()
                case 4:
                    print("Thx for using this program")
                    break
                case _:
                    print("Your selection of operation is wrong--try again")
        except ValueError:
            print("\tDon't enter alnums, strs, symbols and floats as choice")

