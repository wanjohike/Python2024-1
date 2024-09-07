# class Computer
# __before the variable name creates a private variable
class Computer():
    def __init__(self): # We used the __inti__ method to store the max price
        self.__maxprice = 900 # This price is only accessed inside the computer method.
    def sell(self):
        print('Selling Price: {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer() # creating an obejct of the class Computer
c.sell() #accessing the sell Function under Computer

# modify the price
c.__maxprice = 1000 #this selling price is not seen by our function since it is outside score
c.sell()

c.setMaxPrice(1000)
c.sell()

# Encapsulation - data hiding
# Private attributes
# We use a single or double underscore to identify a private attribute


# Polymorphism -many forms
# same entity(method, operator or object) performing different operations
# different scenarios
class Polygon(): # this is our superclass
    # create a method to render a shape
    def render(self):
        print('Rendering a polygon....')

# create a class to create a square out of the polygon
class Square(Polygon):
    # render the square
    def render(self):
        print('Rendering a square...')
    
#  class to create a circle out of the polygon
class Circle(Polygon):
    # render the circle
    def render(self):
        print('Rendering a circle...')
    
# create an object of the square and assign render
s1 = Square()
s1.render()

# create an object of the circle and assign render
s1 = Circle()
s1.render()



