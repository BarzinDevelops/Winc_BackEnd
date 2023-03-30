from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
def shortest_names(countries):
    shortest_countries = [] 
    shortest_len = len(countries[0])
    for country in countries:
         if len(country) < shortest_len:
             shortest_len = len(country) 
    
    for country in countries:
        if len(country) == shortest_len:
            shortest_countries.append(country)
            
    return shortest_countries

def most_vowels(countries):
    vowels = ["a", "e", "i", "o", "u"]
    counted_vowels_list = []    
    most_vowels_list = []
    for country in countries:
        count_vowel = 0
        for char in country:
            if char.lower() in vowels:
                count_vowel += 1
        counted_vowels_list.append([count_vowel, country]) 
    counted_vowels_list2 = counted_vowels_list
    for item in counted_vowels_list:
        for country in counted_vowels_list2:
            if country[0] > item[0]: 
                if country not in most_vowels_list:
                    most_vowels_list.append(country) 
    sorted_list = sorted(most_vowels_list, reverse=True)[:3]
    # sorted_list = sorted(most_vowels_list, reverse=True)
    # print(f"sorted list -> {sorted_list}")
    return [vowel[1] for vowel in sorted_list]



# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    print(most_vowels(countries))
    # most_vowels(countries)
    
