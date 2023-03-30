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

# --------------------------------------------


""" 
from helpers import get_countries



# Leave this untouched. Wincpy uses it to match this assignment with the
# tests it runs. 

__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


# Write your functions here.
def shortest_names(countries):
    shortest_countries = [] 
    shortest_len = len(countries[0])
    for country in countries:
        if len(country) < shortest_len:
            shortest_countries.append(country)
    return shortest_countries


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    # Write the calls to your functions here.
# 1.

print(f"len(countries) -> {len(countries)}")
# print(shortest_names(countries))
print(f"len(shortest_names(countries)) -> {len(shortest_names(countries))}")

"""

""" def most_vowels(countries):
    vowels = ["a", "e", "i", "o", "u"]
    counted_vowels_list = []
    most_vowels_list = []
    for country in countries:
        count_vowel = 0
        for char in country:
            if char in vowels:
                count_vowel += 1
        counted_vowels_list.append([count_vowel, country]) 
    for item in counted_vowels_list:
        if most_vowels_list == []:
            most_vowels_list.append(item)
        elif  most_vowels_list != []:
            for index, vowel_item in enumerate(most_vowels_list):
                if item not in most_vowels_list:
                    if item[0] > vowel_item[0]:
                        most_vowels_list[index] = item
    most_vowels_country = [most_vowels_list[0][1]]
    return most_vowels_country   """
    




""" juist result moet zijn:

['South Georgia and the South Sandwich Islands', 'United States Minor Outlying Islands', 'Micronesia, Federated States of']

"""