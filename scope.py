# def m_function():
#     test = 1 #this is within the local scope of our function
#     print('This is my function', test)

# test = 0 #this is within the global scope
# m_function()
# print('test for global function', test)

# LEGB - Local, enclosing, Global, Built-in

# if a variable is assigned inside a def, it is local to that function
#if a variable is assigned in an enclosing def, it is nonLocal to nested function
# If a variable is assigned outside all defs, it is global to the current file(module)
# x = 99
# def function1():
#     x = 88

# def outer():
#     test = 1 #outer scope
#     def inner():
#         test = 2 #inner scope
#         print('Inner', test)

#         inner()
#     print('Outer', test)

# test = 0 #global scope
# outer()
# print('global', test)

# global and nonLocal Statement
# def outer():
#     test = 1
#     def inner():
#         nonlocal test
#         test = 2 #nearest enclosing scope
#         print('inner', test)

#     inner()
#     print('outer', test)
# test = 0
# outer()
# print('global', test)
print("This is an example of scope Usage")
def lib():
    Lib_Name = "Ahmed's Library"
    # create a section for books eg action
    def section():
        # Enclosing scope
        section_name = 'action'
        # function to hold the book details
        def book():
            # Local Scope
            book_title = 'Maze Runner'
            print(f'Book Title: {book_title}')
            print(f'Section Name: {section_name}')
            print(f'Library: {Lib_Name}')
        book()
    section()
lib()
