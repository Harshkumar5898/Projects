import datetime
import re
import time

# Total function give total expance of the month by adding the amount attached with Amount: and print it at the end of the month


def Total():
    prev = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    breaker = input(
        "Type (Total) to print total of last mounth or date(yyyy-mm) of the log file you want to print : ")
    if breaker == 'Total':

        with open(f"{prev.strftime('%Y-%m')}.txt", 'r') as f:
            doc = f.read()
        results = re.findall(r"Amount:[0-9]+", doc)
        total = 0
        amountlist = []
        for i in results:
            amountlist.append(i.split(":"))

        for i, amount in amountlist:
            total += int(amount)

        with open(f"{prev.strftime('%Y-%m')}.txt", 'a') as f:
            f.write(f"\nTotal expance of this month = {total}\n")
        print(
            "You have succesfully added total expance of the last mounth to the log file\n")
        print(f"Total expance of this month = {total}\n")

    else:

        with open(f"{breaker}.txt", 'r') as f:
            doc = f.read()
        results = re.findall(r"Amount:[0-9]+", doc)
        total = 0
        amountlist = []
        for i in results:
            amountlist.append(i.split(":"))

        for i, amount in amountlist:
            total += int(amount)

        with open(f"{breaker}.txt", 'a') as f:
            f.write(f"\nTotal expance of this month = {total}\n")
        print(
            f"You have succesfully added total expance of {breaker} to the log file\n")
        print(f"Total expance of {breaker} = {total}\n")

    time.sleep(3)


def Bills():
    print('''  --  Which bill have paid
  - 1 > Elctricity Bill
  - 2 > Piped Gas Bill
  - 3 > Water Bill
  - 4 > Milk Bill
  - 5 > Paper Bill
  - 6 > Other
   ''')

    typeOfBill = input("Enter your Choice : ")
    if typeOfBill == '1':
        typeOfBill = 'Electricity Bill'

    elif typeOfBill == '2':
        typeOfBill = 'Piped Gas Bill'

    elif typeOfBill == '3':
        typeOfBill = 'Water Bill'

    elif typeOfBill == '4':
        typeOfBill = 'Milk Bill'

    elif typeOfBill == '5':
        typeOfBill = 'Paper Bill'

    elif typeOfBill == '6':
        typeOfBill = input("Enter your bill : ")

    Amount = float(input(f"Enter the amount you pay for {typeOfBill} : "))
    with open(f'{month}.txt', 'a') as f:
        f.write(f"{date} : {typeOfBill} is paid of Amount:{Amount}\n")

    print(
        f"You have succesfully added {typeOfBill} with amount of {Amount} to your log file\n")
    time.sleep(3)


def Grocry():
    print(''' -- Which type of Grocry you buy
  - 1 > Vegitables
  - 2 > Fruit
  - 3 > Other(leave it blank for other than Vegitables or Fruit)
    ''')
    typeOfGrocry = input("Enter your Choise : ")
    if typeOfGrocry == '1':
        typeOfGrocry = 'Vegetables '

    elif typeOfGrocry == '2':
        typeOfGrocry = 'Fruits '

    elif typeOfGrocry == '3':
        typeOfGrocry = ''

    thing = input("Enter exactly you buy : ")
    Amount = float(input(f"Enter the amount you pay for {thing} : "))
    with open(f'{month}.txt', 'a') as f:
        f.write(f"{date} : {typeOfGrocry}{thing} of Amount:{Amount}\n")
    print(
        f"You have succesfully added {thing} with amount of {Amount} to your log file\n")

    time.sleep(3)


def Shoping():
    print(''' - Select source of shoping
  - 1 > Online
  - 2 > Offline
    ''')
    Source = input()
    if Source == '1':
        Source = 'online'
    elif Source == '2':
        Source = 'market'

    thing = input("Enter what you buy : ")
    Amount = int(input(f"Enter the amount you pay for {thing} : "))
    with open(f'{month}.txt', 'a') as f:
        f.write(f"{date} : Buy {thing} from {Source} of Amount:{Amount}\n")
    print(
        f"You have succesfully added {thing} with amount of {Amount} to your log file\n")

    time.sleep(3)


def Recharge():
    print('''  --  Which thing recharge you done
  - 1 > Mobile Recharge
  - 2 > DTH Recharge
  - 3 > FASTag Recharge
  - 4 > Google Play Recharge
  - 5 > Other
    ''')

    thingRecharge = input()
    if thingRecharge == '1':
        thingRecharge = 'Mobile Recharge'

    elif thingRecharge == '2':
        thingRecharge = 'DTH Recharge'

    elif thingRecharge == '3':
        thingRecharge = 'FASTag Recharge'

    elif thingRecharge == '4':
        thingRecharge = 'Google Play Recharge'

    elif thingRecharge == '5':
        thingRecharge = input("Enter which recharge you have done : ")

    Amount = float(input(f"Enter the amount you paid for {thingRecharge} : "))
    with open(f'{month}.txt', 'a') as f:
        f.write(f"{date} : {thingRecharge} of Amount:{Amount}\n")

    print(
        f"You have succesfully added {thingRecharge} of amount {Amount} to your log file\n")
    time.sleep(3)


def LoanRepayment():
    print('''  --  Select Loan you paid
  - 1 > Home Loan
  - 2 > Car Loan
  - 3 > Education Loan
  - 4 > Other
    ''')

    Loan = input()
    if Loan == '1':
        Loan = 'Home Loan'

    elif Loan == '2':
        Loan = 'Car Loan'

    elif Loan == '3':
        Loan = 'Education Loan'

    elif Loan == '4':
        Loan = input("Enter Loan you paid : ")

    Amount = float(input(f"Enter the amount you paid for {Loan} : "))
    with open(f'{month}.txt', 'a') as f:
        f.write(f"{date} : Pay {Loan} of Amount:{Amount}\n")

    print(
        f"You have succesfully added {Loan} of amount {Amount} to your log file\n")
    time.sleep(3)


def Education():
    print('''  --  Select your option
  - 1 > School Fee
  - 2 > Tuition Fee
  - 3 > Collage Fee
  - 4 > Something you buy for your Education
  - 5 > Other
    ''')

    Education = input()
    if Education == '1':
        Education = 'School Fee'

    elif Education == '2':
        Education = 'Tuition Fee'

    elif Education == '3':
        Education = 'Collage Fee'

    elif Education == '4':
        Education = input("Enter what you buy : ")

    elif Education == '5':
        Education = input("Enter what you buy or some ones fee : ")

    Amount = float(input(f"Enter the amount you paid for {Education} : "))

    if Education == 'School Fee' or Education == 'Tuition Fee' or Education == 'Collage Fee':
        with open(f'{month}.txt', 'a') as f:
            f.write(f"{date} : Pay {Education} of Amount:{Amount}\n")

    else:
        with open(f'{month}.txt', 'a') as f:
            f.write(f"{date} : Buy {Education} of Amount:{Amount}\n")

    print(
        f"You have succesfully added {Education} of amount {Amount} to your log file\n")
    time.sleep(3)


def OtherExpance():
    Other = input("Enter What you buy : ")
    Amount = int(input(f"Enter amount of {Other} : "))
    with open(f'{month}.txt', 'a') as f:
        f.write(f"{date} : Purches {Other} of Amount:{Amount}\n")

    print(
        f"You have succesfully added {Other} of amount {Amount} to your log file\n")
    time.sleep(3)


def printLog():
    print(" -- Select 1 to print this month log file or 0 for last month log file or Enter the month(yyyy-mm) of log file you want to print -- ")
    a = input()
    if a == '1':
        with open(f'{month}.txt', 'r') as f:
            print(f.read())

    elif a == '2':
        prev = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
        with open(f"{prev.strftime('%Y-%m')}.txt", 'r') as f:
            print(f.read())

    else:
        with open(f"{a}.txt", 'r') as f:
            print(f.read())

    time.sleep(5)


if __name__ == '__main__':
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    month = datetime.datetime.now().strftime("%Y-%m")
    print(f" * DATE - {date}\n")
    while True:
        print('''  --  Select Type Of Expance --  
        - 1 > Bills
        - 2 > Grocry Expence
        - 3 > Shoping (Online/Offline)
        - 4 > Recharge
        - 5 > Loan Repayment 
        - 6 > Education Expance
        - 7 > Other Expance
        - 8 > Get total expance of last mounth or other month
        - 9 > To print this mounth or last mounth log file or other month log
        - q > Type q to quit program
        ''')

        time.sleep(2)

        Expance = input("Select your option : ")

        if Expance == "1":
            Bills()

        elif Expance == "2":
            Grocry()

        elif Expance == "3":
            Shoping()

        elif Expance == "4":
            Recharge()

        elif Expance == "5":
            LoanRepayment()

        elif Expance == '6':
            Education()

        elif Expance == '7':
            OtherExpance()

        elif Expance == "8":
            Total()

        elif Expance == "9":
            printLog()

        else:
            print("\n We are exiting the program...")
            time.sleep(3)
            quit()
