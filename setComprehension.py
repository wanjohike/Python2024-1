# allow you to creat new sets by iterating over an existing iterable set
# syntax - '[expression for item in iterable if condition]'

# creating a list of unique even numbers from an existing list

nums = [12, 2, 3, 4, 5, 6, 8, 8, 9, 10, 22, 2, 24]
unique_even = {x for x in nums if x % 2 == 0}
print(unique_even)

# create a set of unique vowels from the string "Hello world"
str = 'HEELLO, WOLRD'
vowels = {char.lower() for char in str if char.lower() in 'aeiou'}
print(vowels)

# Create a set of prime numbers from range 2, 20
prime_nums = {n for n in range(2,20) if all (n % i !=0 for i in range(2, int(n**0.5) + 1) ) }
print(prime_nums)