# introduction to __init__ method- instead of set_details method we replaced with __init__ method,
# so that everytime we don't need to call the set_details method before to run any other method as
# other method is using instance variable of set parameters otherwise it will rais ean error

class Person:   # defining class object
    def __init__(self, name, age):   # method
        self.name = name  # self.name-instance Variable , # name - parameter
        self.age= age
    def display(self):
        print('I am', self.name)
    def greet(self):
        if self.age <80:
            print('Hello, How are you doing?')
        else:
            print('Hello')

p1 = Person('Sanchit', 20)
p2 = Person('Ankit', 39)
p1.display()
p1.greet()

p2.display()
p2.greet()
