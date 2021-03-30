from datetime import datetime
name = input('What is your name? \n')
listOfNames = ['Jennifer', 'Chidera','Ganiru']
listOfPasswords = ['passwordJennifer', 'passwordChidera', 'passwordGaniru']
if name in listOfNames:
    password = input('Enter Password: \n')
    indexOfNames = listOfNames.index(name)
    if password == listOfPasswords[indexOfNames]:
        print('You are logged in! Welcome', name + '!.')
        dateAndTime = datetime.now()
        print(dateAndTime)
        
        print('please Enter your preferred option: ')
        print('1. Withdrawal.')
        print('2. Deposit.')
        print('3. complaint.')
        
        option = int(input('Enter your preferred option: \n'))
        if option == 1:
            amountToWithdraw = int(input('How much would you like to withdraw? \n'))
            print('Take your cash!')
        elif option == 2:
            amountToDeposit = int(input('How much would you like to deposit? \n'))
            initialBal = 100
            print('Your current bal is:', amountToDeposit + initialBal,'USD.')
        elif option == 3:
            complaint = input('What issue would you like to report? \n')
            print('Thank you for contacting us!')
        else:
            print('Enter a preferred option from 1 - 3 and try again!')
    else:
        print('Enter a valid password and try again!')
else:
    print('Enter a valid name and try again!!')