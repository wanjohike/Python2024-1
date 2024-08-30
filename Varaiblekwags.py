def func(**kwargs):
    print(kwargs)

#  all calls equivalant. they print out {a:1, b:42}
func(a=1, b=24)
func(**{'a':1, 'b':42})
func(**dict(a=1, b=42))
# all the above return the same value.
# adding ** in front of the paramenter name in the function definition 
# tells python to use that name to collect a variable number keyword parameter