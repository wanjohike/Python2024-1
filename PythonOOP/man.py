# import person
# #  create an object man from person
# man = person.Person() # qualify the object we want to create from class
# print(man.species)
# print(man.isAlive)

# # modify the alive status of man to false
# person.Person.isAlive = False
# print(man.isAlive)

# # give the man a name
# man.name = "Broston"
# man.surname = "Loni"
# print(man.name, man.surname)

class sample_class:
    def __init__(self, course):
        self.course = course
    
    def display(self):
        print(self.course)

object1 = sample_class("Python")
object1.display()