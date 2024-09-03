# def greeting(name):
#     def hello():
#         return 'Hello, ' , name, '!'
#     return hello

# greet = greeting('Atlantis')
# print(greet()) # prints "Hello, Atlantis!"

# python decorators
# is a fuction that takes a in a fucntion and returns it by adding some
# functionality
#  ant object that implements the special __call__ method is termed as a calable
# A decotar is thus a callable that returns a callable
# def make_pretty(func):
#     def inner():
#         print('I got decorated')
#         func()
#     return inner()
    
# def ordinary():
#     print('I am ordinary')

# decorated_func = make_pretty(ordinary)
# decorated_func

# the @symbol with decorator
# decorating fuctions with parameters
# if we pass y as 0, we get an error.
# make a decorator to check if this is the case

def check_div(func):
    def checkDivide(x, y):
        if y == 0:
            print('You are trying to divide with zero')
            return
        
        return func(x,y)
    return checkDivide


@check_div
def divide(x,y):
    return x/y

divide(2,0)