# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
#1: import a module that prints the Zen of Python(opens in a new tab)

# import this

#2: write function wait(seconds) that utilizes time module to wait a given time
import time
def wait(seconds):
    time.sleep(seconds)

#3: Implement a function my_sin that takes one float as an argument and 
#   returns the sine of that float. Use the math module.
import math
def my_sin(some_float):
    return math.sin(some_float)

#4: Implement a function iso_now that takes no arguments and returns a string 
# containing the current date and time up to the minute in the 
# ISO 8601(opens in a new tab) format.
from datetime import datetime as dt
def iso_now():
    currentDateAndTime = dt.now()
    date_formated = currentDateAndTime.strftime('%Y-%m-%dT%H:%M')
    return date_formated

#5: Implement a function platform that takes no arguments and returns a 
# string that shows which platform we are on.
def platform():
    import sys
    return sys.platform

#6: Create a new file greet.py, and in that file implement a function supergreeting 
# that takes a name as an argument (str) and returns a string of the form 'Hellooo...ooo, Bob!'. 
# Then import this function in main.py and write a function supergreeting_wrapper that takes the 
# exact same type of argument, calls supergreeting with it and returns the result.

def supergreeting_wrapper(name):
    from greet import supergreeting as sg
    return sg(name)
    



if __name__ == '__main__':
    # wait(3)
    # my_sin(46)
    # iso_now()
    # platform()
    print(supergreeting_wrapper('barry'))