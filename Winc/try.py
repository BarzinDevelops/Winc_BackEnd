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
def farm_action(weather, time_of_day, cow_milk_stat, loc_cows, season, slurry_tank, grass_stat):

    action = 'wait'

    if (loc_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy')):
        action = 'take cows to cowshed'
        # return action

    elif (cow_milk_stat == True):
        if (loc_cows == 'pasture'):
            action = 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
        else:
            action = 'milk cows'
        print("ACTION ==>> ", action, "\n-----------------")
        return action
    elif (slurry_tank == True and weather != 'sunny' and weather != 'windy'):
        if (loc_cows == 'pasture'):
            action = 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'
        else:
            action = 'fertilize pasture'
        # return action
    elif (grass_stat == True and season == 'spring' and weather == 'sunny'):
        if (loc_cows == 'pasture'):
            action = 'take cows to cowshed\nmow grass\ntake cows back to pasture'
        else:
            action = 'mow grass'
        # return action

    return action

print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
