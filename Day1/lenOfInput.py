
print( len( input("What is your name: ") ) )


# using function
def length():
    x = len(input("What is your name: "))
    # print("length of name is " + x)   # with this i will get error as TypeError: can only concatenate str (not "int") to str
    print("length of name is " + str(x))  #using str() to convert int to string
length()
