# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

# Define these functions in main.py:
#1: greet: takes a name and returns a string in the format: 'Hello, Bob!'
def greet(name):
    return f"Hello, {name}!"
print(greet('Bob'))

#2: add: takes three numbers (integers or floats) and returns their sum. Example:
def add(num1,num2,num3):
    return num1 + num2 + num3
print("------------")
print(add(5,3,2))

#3: positive: takes a number (integer or float) and returns whether or not it is 
#   positive in the form of a boolean. You do not have to handle the case where 
#   the argument is not an int or a float. Examples:
def positive(num):
    return num > 0
print("------------")
print(positive(50))
print(positive(-33))
print(positive(0))

#4: negative: takes a number (integer or float) and returns whether or not 
#   it is negative in the form of a boolean. You do not have to handle the 
#   case where the argument is not an int or float. Examples:
def negative(num):
    return num < 0
print("------------")
print(negative(5))
print(negative(-5))
print(negative(0))

