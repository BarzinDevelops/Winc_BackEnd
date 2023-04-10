# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
import json
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }
    return passport

def add_stamp(passport, country):
    if 'stamps' in passport:
        if country not in passport['stamps']:
            passport['stamps'].append(country)
    else:
        passport['stamps'] = [country]
    return passport
    
def add_biometric_data(passport, name_biometric_data, value_biometric_data, date_biometric_data):
    if 'biometric' in passport:
        if name_biometric_data in passport['biometric']:
            passport['biometric'][name_biometric_data].update(
                {
                    "date":  date_biometric_data,
                    "value": value_biometric_data
                },
            )
        else:
            passport['biometric'][name_biometric_data] = { 
                    "date":  date_biometric_data,
                    "value": value_biometric_data
            }
    else:
        passport['biometric'] = { 
            name_biometric_data : {
                "date":  date_biometric_data,
                "value": value_biometric_data
            }
        } 
    return passport

if __name__ == "__main__":
    countries = get_countries()
    omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
    omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
    omari = add_biometric_data(omari, "eye_color_right", "green", "2020-05-05")
    fingerprint_data = {
        "left_pinky": "2378945",
        "left_ring": "2349081",
        "left_middle": "132890",
        "left_index": "9823234",
        "left_thumb": "0924131",
        "right_thumb": "6234923",
        "right_index": "13249734",
        "right_middle": "34023784",
        "right_ring": "12332538",
        "right_pinky": "32458970",
    }
    omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
    print(f"{json.dumps(omari, indent=4)}\n{'--'*30}")
