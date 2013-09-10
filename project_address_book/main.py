# From "A Byte of Python"
# Source: http://files.swaroopch.com/python/byte_of_python.pdf


class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hello, how are you? My name is ', self.name)


p = Person('Valera')
print(p)
p.sayHi()
