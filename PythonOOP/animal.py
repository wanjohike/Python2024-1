# Inheritance example for behavior of different animal
# single inheritance  - only inherit one base class
#  multiple inheritance - inherits multiple base classes
    # must be inside brackets, separated by comma
    # Class derivedClass(baseClass1, baseClass2)
# Multi-level inheritances - class inherits a base class and anther class inherits the previously derived class
    # parent, child, grandchild relationship
# Hierarchical inheritance - only have one class one base class inherited by multiple classes
# hybrid - blend of all the above

import math


class Animal(): # this is our base/super class
    def eat(self):
        print('I can Eat')
    def sleep(self):
        print('I can sleep')
    def sound(self):
        print("Animal sound")

animal = Animal()
animal.sound()

# derive a class Dog
class Dog(Animal):
    def bark(self):
        print('I can bark')

# create a dog object that accesses all members of the Animal class
simba = Dog()
simba.bark()
simba.eat()
simba.sleep()

#  create a new class for a cat that inherits the behaviour of Animals
# try accessing the behaviour of dog
class Cat(Animal):
    def meow(self):
        print('I can meow')
    

nyau = Cat()
nyau.meow()
nyau.sleep()
nyau.sound()

class GermanShepard(Dog):
    def protect():
        print('I am a protector')

bruno = GermanShepard()
bruno.bark()
bruno.sleep()
bruno.eat()

class Example:
    def multiply(self, a, b, c=1):
        print(a*b*c)
    
example = Example()
example.multiply(5,10)
example.multiply(2,5,6)
example.multiply(math.pi, 34)