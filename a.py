# import b #Imports the whole module

# from c import divide
# # We want to use spam
# b.spam('This is spam')
# b.spam2()

# divide(3,4)

# # a is top level file. it only contains statements to be executed
# from b import func
# from c import func

# import b
# import c

# b.func()
# c.func()

from b import func as bFunc
from c import func as cFunc

bFunc()
cFunc()