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


if __name__ == '__main__':
    # wait(3)
    # print(my_sin(46))
    print(iso_now())