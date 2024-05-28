#if we prefix wiith single underscore  before a method name or instance variable name then we can  access directly
class Product:
    def __init__(self):
        self.data1 =10
        self._data2 =20
    def methodA(self):
        pass
    def _methodB(self):
        pass
p = Product()

print(p.data1)
print(p._data2)

# if we prefix double underscore  before a method name or instance variable name then we can not access
# directly, we need to access indirectly- first checking the name using dir command  and call it explicitly
class Product:
    def __init__(self):
        self.data1 =10
        self.__data2 =20
    def methodA(self):
        pass
    def __methodB(self):
        pass



print(dir(p))
p._Product__methodB()