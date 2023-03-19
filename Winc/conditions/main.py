# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

# def farm_action(weather, time_of_day, cow_milk_stat, loc_cows, season, slurry_tank, grass_stat):

#     action = 'wait'

#     if (loc_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy')):
#         action = 'take cows to cowshed'
#         return action

#     elif (cow_milk_stat == True):
#         if (loc_cows == 'pasture'):
#             action = 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
#         else:
#             action = 'milk cows'
#         return action
#     elif (slurry_tank == True and weather != 'sunny' and weather != 'windy'):
#         if (loc_cows == 'pasture'):
#             action = 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'
#         else:
#             action = 'fertilize pasture'
#         return action
#     elif (grass_stat == True and season == 'spring' and weather == 'sunny'):
#         if (loc_cows == 'pasture'):
#             action = 'take cows to cowshed\nmow grass\ntake cows back to pasture'
#         else:
#             action = 'mow grass'
#         return action

#     return action

# print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
# print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
# print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
# print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
# ----------------------------------------------

def farm_action(weather, time_of_day, cow_milking_status, location_cows, season, slurry_tank, grass_status):
    action = "wait"
    if location_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy'):
        action = "take cows to cowshed"

    elif cow_milking_status:
        if location_cows == 'cowshed':
            action =  "milk cows"
        if location_cows == 'pasture':
            action = f"take cows to cowshed\nmilk cows\ntake cows back to pasture"
        
    elif slurry_tank:
        if location_cows != 'cowshed':    
            action = "take cows to cowshed"
        if (weather != 'sunny' and weather != 'windy' ):
            action =  "fertilize pasture"
    
    elif grass_status and (season == 'spring' and weather == 'sunny'):
        if location_cows != 'pasture':
            action = 'mow grass'
        else:
            action = 'take cows to cowshed\nmow grass\nake cows back to pasture'
                 
    return action    
    
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))