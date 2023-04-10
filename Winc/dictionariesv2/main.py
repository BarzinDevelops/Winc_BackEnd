# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
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
        print(f"stamps exists already in passport!")
        if country not in passport['stamps']:
            print(f"But '{country}' doesn't yet exist as a stamp in the 'stamps'.\nAdding {country}....")
            passport['stamps'].append(country)
            print(f"{country} stamp added to passport!\n{'--'*30}")
            print(f"Now this is the new passport 'stamps' values: {passport['stamps']}")
        else:
            print(f"{country} stamp already exists in passport stamps!")
    else:
        print(f"Current passport items -> {passport}\n{'--'*30}")
        print("creating 'stamps' key in passport...")
        passport['stamps'] = [country]
        print(f"{country} stamp added to passport!\n{'--'*30}")
        print(f"Passport items after adding the 'stamps' key and value -> {passport}")
    return passport
    


if __name__ == "__main__":
    countries = get_countries()
    myPassport = create_passport("Glenn", "1990-04-19","Frankfurt", 1.80, "Germany")
    add_stamp(myPassport, 'France')

    