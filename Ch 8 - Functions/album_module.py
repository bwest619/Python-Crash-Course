# Making a practice module for album.py
# Importing to imports.py as practice

def make_album(name, album):
    """Returning a dictionary containing an artist's name and album title"""
    album_dict = {'artist' : name.title(), 'title' : album.title()}
    return album_dict

music_album = make_album('tool', 'lateralus')
print(music_album)
