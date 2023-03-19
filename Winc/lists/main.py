# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# 1:
def alphabetical_order(film_names):
    return sorted(film_names)

# 2:
golden_globe_films = ["Jaws", "Star Wars: Episode IV - A New Hope", "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]

new_golden_globe_films = []

def won_golden_globe(film_name):
    for film in golden_globe_films:
        new_golden_globe_films.append(film.lower())
    return True if film_name.lower() in new_golden_globe_films else False
 
tot_album = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between", "Toto XIV", "Old Is New"]

# 3:
album = ['Test', "Toto XX", "Falling in Between", "Jaws","The Seventh One", "War Horse"]
def remove_toto_albums(album):
    if tot_album[0] in album : album.remove(tot_album[0])
    if tot_album[1] in album : album.remove(tot_album[1])
    if tot_album[2] in album : album.remove(tot_album[2])
    if tot_album[3] in album : album.remove(tot_album[3])
    if tot_album[4] in album : album.remove(tot_album[4])
    if tot_album[5] in album : album.remove(tot_album[5])
    return album

print(remove_toto_albums(album))