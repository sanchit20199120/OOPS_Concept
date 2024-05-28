
#Practice Exercise -1

#Make a class that represents a bank account. Create four methods named set_details, display, withdraw and deposit.

#In the set_details method, create two instance variables : name and balance.
# The default value for balance should be zero. In the display method, display the values of these two instance variables.

#Both the methods withdraw and deposit have amount as parameter. Inside withdraw, subtract
#the amount from balance and inside deposit, add the amount to the balance.

#Create two instances of this class and call the methods on those instances.




class Bank_Account:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance
    def display(self):
        print("name =", self.name)
        print("balance =", self.balance)
    def withdraw(self, amount):
        self.amount= amount
        self.balance -= self.amount
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        self.display()

p1 = Bank_Account()
p2 = Bank_Account()
p1.set_details('Sanchit')
p1.display()
p1.withdraw(100)
p1.display()
p1.deposit(300)

p2.set_details('Ankit')
p2.display()
p2.withdraw(1000)
p2.display()
p2.deposit(10000)




