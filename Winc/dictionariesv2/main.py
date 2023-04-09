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

if __name__ == "__main__":
    countries = get_countries()
    myPassport = create_passport("barzin", "1982-08-29","Teheran", 1.70, "Netherlands")
    print(myPassport)