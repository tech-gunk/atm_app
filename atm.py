cardsPinsAndBalance = {'123456': {'pin': '1234', 'balance': 100}, '234567': {'pin': '2345', 'balance': 200}, '345678': {'pin': '3456', 'balance': 300}, '456789': {'pin': '4567', 'balance': 400}, '567890': {'pin': '5678', 'balance': 500}}

class Atm:
    def __init__(self, atm_card_number, pin):
        self.atm_card_number = atm_card_number
        self.pin = pin
        if (self.atm_card_number in cardsPinsAndBalance) and (self.pin == cardsPinsAndBalance[self.atm_card_number]['pin']):
            self.balance = cardsPinsAndBalance[self.atm_card_number]['balance']
            self.takeInput()
        else:
            print('Invalid card number or pin')


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print('Withdrawal successful')
        else:
            print('Insufficient funds')

    def deposit(self, amount):
        self.balance += amount
        print('Deposit successful')

    def checkBalance(self):
        print('Your balance is', self.balance)

    def changePin(self, new_pin):
        oldPin = self.pin
        oldPinInput = input('Enter old pin: ')
        if oldPin == oldPinInput:
            self.pin = new_pin
            print('Pin changed')
        else:
            print('Enter the old pin correctly')

    def takeInput(self):
        print('1. Withdraw')
        print('2. Deposit')
        print('3. Check balance')
        print('4. Change pin')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            amount = int(input('Enter amount: '))
            self.withdraw(amount)
            self.takeInput()
        elif choice == '2':
            amount = int(input('Enter amount: '))
            self.deposit(amount)
            self.takeInput()
        elif choice == '3':
            self.checkBalance()
            self.takeInput()
        elif choice == '4':
            newPin = input('Enter new pin: ')
            self.changePin(newPin)
            self.takeInput()
        elif choice == '5':
            print('Thank you for using our ATM')
        else:
            print('Invalid choice')
            self.takeInput()

cardInput = input('Enter card number: ')
pinInput = input('Enter pin: ')
atmObject = Atm(cardInput, pinInput)
