'''

# print(f"""
#      type(3) -> {type(3)}
#      type(3.14) -> {type(3.14)}
#      type('pi') -> {type('pi')}
# """)

# some_number = 5
# another_number = 9.81
# some_string = 'Hello world'

# print(f"""
#      some_number -> {type(some_number)}
#      another_number -> {type(another_number)}
#      some_string -> {type(some_string)}
# """)

# print(f" 5 + 45 => {5 + 45}")
# 'I like ' + 3.14
# print(f" 5 + some_string => {5 + 'some_string'}")
# 42 + ' is the answer'

# print('this is "double quote" within single quote.')
# print("this is 'single quote' within double quote.")
# print("""this is escape character: \\
#       (you can only show it whe u use two '\\\\')
#       This way you actually escape \\ char by putting extra backslash before it.""")


# print(chr(2192))
# chr(2192)

# def initials(name):
#     first = name[:name.find(' ')].capitalize()
#     last = name[name.find(' ')+1:].capitalize()
#     return f'{first} {last} '

# print(initials('barzin frozandehfar'))
# print(initials('b ghaVIM'))
'''

# --------------------------------------------
"""

Weather
    rainy
    sunny
    windy
    neutral

Time of day
    day
    night

Cow milking status
    Need milking: True
    Don't need milking: False

Location of the cows
    pasture
    cowshed

Season
    winter
    spring
    summer
    fall

Slurry tank
    Full: True
    Not full: False

Grass status
    Long: True
    Short: False

"""

# --------------------------------------------------------

party_location =    'inside' if 1 + 2 == 5 or 3 ** 3 == 9\
                    else 'yard' if bool(2//5) is True else\
                    False if True else 'restaurant'

# print(f"party_location = ", party_location)

tryThis = f"""  this is line 1
                \bsome \bthis is line 2
                how are these printed now?"""

print(f"tryThis => {tryThis}")