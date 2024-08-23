# Dictionary is ordered collection of items
# it stores element in key/value parts
# keys - uniques identifier associate with each value

# dictionary named capital_cities to store the country and its capital
capital_cities = {'kenya':'Nairobi','Uganda':'Kampala'}
print(capital_cities)

# retrieve the capital cites
# we use keys to retrieve the values. We cant use values to retrieve keys
# get the capital city of Kenya
print(capital_cities['kenya'])
# print(capital_cities["Kampala"]) #this returns a keyError since we cannot acess a key value.

# Different ways of creating a dictionary
# Create a dictionary
a = dict(Kenya = 'Nairobi', Uganda = 'Kampala')
b = {'Kenya':'Nairobi','Uganda':'Kampala'}
c = dict(zip(['Kenya', 'Uganda'], ['Nairobi', 'Kampala']))
d = dict([('Kenya', 'Nairobi'), ('Uganda', 'Kampala')])
e = dict({'Kenya':'Nairobi', 'Uganda': 'Kampala'})

print(a==b==c==d==e) #Checking if they are one and the same thing