# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# --Part 1--

# 1
player1 = 'Ruud Gullit'
player2=  'Marco van Basten'

# 2
goal_0 = 32
goal_1 = 54

# 3
scorers = player1 + " " + str(goal_0) + ", " + player2 + " " + str(goal_1)

# 4
report = f"""{player1} scored in the {goal_0}nd minute
{player2} scored in the {goal_1}th minute"""



# --Part 2--

# 1: Choose a player that played in the soccer match and store his name as a string in the variable player
player = "Sergey Gotsmanov"


# 2: use slicing and the find-method to isolate and store the player's first name.
first_name = player[:player.find(' ')]


# 3: last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name_len = len(player[player.find(' ') + 1:])
last_name = player[-last_name_len: ]

# 4: name_short: isolate and store the player's name in this format: S. Gotsmanov
name_short = first_name[:1]+'. '+last_name
#solution winc: name_short = f"{player[0]}.{player[player.find(' '):]}"


""" 5: chant: this is what the crowd chants when it looks like your player is going to 
    score a goal -- their first name plus an exclamation mark(!), x-times, 
    where x is the number of characters in their first name. Because 
    Gut has 3 letters in his name, we repeat his name 3 times. Make sure the last character 
    of this string is not a space! For our example player:    Sergey! Sergey! Sergey!
"""
chant_with_space = f"{first_name}! " * len(first_name)
chant = chant_with_space[:-1]


print(f"{chant }")

""" 6: good_chant: Make super-sure the last character of chant is not a space by using 
the inequality operator (!=). This variable needs to be a boolean, not a string. 
You can create the value for this variable by comparing the last character of chant with a space character. 
Try this in your REPL for an example: print(2 != 3). Also try: print(2 != 2).

"""   

good_chant = chant[-1:] != ' '



