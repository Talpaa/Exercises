#1. Create a Playlist:

"""Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
    The function should return a dictionary with the playlist name and a set of songs. Call the function with different numbers of songs to demonstrate flexibility.
    Example: create_playlist("Road Trip", {"Song 1", "Song 2"})
    Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False). 
    This function should return an updated dictionary.
    Example: add_like(dictionary, “Road Trip”, liked=True)"""

def create_playlist(name: str, song_titles: list)->dict:

    song_titles = set(song_titles)

    song_titles = list(song_titles)

    libreria: dict = {name: song_titles}
    
    return libreria

def add_like(libreria: dict,name: str,liked: bool)->dict:

    libreria.update({"liked": liked})
    
    return libreria



libreria: dict = create_playlist("Road Trip", ["Song 1", "Song 2"])
print(libreria)

libreria = add_like(libreria, "Road Trip", liked = True)
print(libreria)
