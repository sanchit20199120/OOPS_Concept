# class object
# Methods = Function
# instance Object
# instance Variable

class Person:   # defining class object
    def set_details(self, name, age):   # method
        self.name = name  # self.name-instance Variable , # name - parameter
        self.age= age
    def display(self):
        print('I am', self.name)
    def greet(self):
        if self.age <80:
            print('Hello, How are you doing?')
        else:
            print('Hello')


p1 = Person()       # definition Instance object P1
p2 = Person()       # definition Instance object P2
print(id(Person))   # class object ID - 140673101658944
print(type(p1))     # <class '__main__.Person'>
print(type(p2))     # <class '__main__.Person'>
print(id(p1))       # P1 instance Object  ID 4510699776
print(id(p2))       # P2 instance Object  ID  4433973312


p1.set_details('sanchit', 20)
p2.set_details('ankit', 90)

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

p1.display()
p1.greet()
p2.display()
p2.greet()