#question4(a)
def calculate_bonus(salary, years_of_service):
    bonus = 0
    if years_of_service > 4:
        bonus = salary * 0.08
    elif years_of_service == 3:
        bonus = salary * 0.05
    net_salary = salary + bonus
    return bonus, net_salary

def main():
        salary = float(input("Enter your salary: "))
        years_of_service = int(input("Enter your years of service: "))

        if salary < 0 or years_of_service < 0:
            print("Please enter valid salary and years of service.")
            return

        bonus, net_salary = calculate_bonus(salary, years_of_service)

        print("Net bonus amount:", bonus)
        print("Net salary amount:", net_salary)


if __name__ == "__main__":
    main()



#question 4 (b)
def saccoWITU():
    accountBalance = 0

    while True:
        print("\nWelcome, WITU Sacco.")
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')

        userChoice = input("Enter your selection (1, 2, or 3): ")

        if userChoice == '1':
            depositAmount = int(input("\nEnter amount to be deposited: "))
            if depositAmount < 1000:
                print('\nMinimum deposit is 1000')
            else:
                accountBalance += depositAmount
                print(f'You have deposited {depositAmount:,} and your new account balance is {accountBalance:,}')

        elif userChoice == '2':
            withdrawAmount = int(input("\nEnter amount to be withdrawn: "))
        
            if withdrawAmount < 500:
                print("Minimum amount is 500")

        elif userChoice == '3':
            print(f'Your account balance is {accountBalance:,}')

        else:
            print("Invalid! Please select 1, 2, or 3\n")
            continue

        run = input("Enter 1 to continue or any other key to quit: ")
        if run != '1':
            break

saccoWITU()




#QUESTION 4 (c)
import math
X1 = 60
X2 = 30
Y1 = 160.5
Y2 = 97.7


d = math.sqrt((X1-X2) + (Y1-Y2))
print(d)









