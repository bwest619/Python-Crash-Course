# Try it yourself, page 146

print("\n")
def make_album(name, album):
    """Returning a dictionary containing an artist's name and album title"""
    album_dict = {'artist' : name.title(), 'title' : album.title()}
    return album_dict


music_album = make_album('paul mccartney', 'band on the run')
print(music_album)

music_album = make_album('blink 182', "what's my age again")
print(music_album)

music_album = make_album('tool', 'lateralus')
print(music_album)

###################################################################################################

# Same program, this time adding tracks as a possibility
print("\n")
def make_album(name, album, tracks=0):
    """Returning a dictionary containing an artist's name and album title"""
    album_dict = {'artist': name.title(), 'title': album.title()}

    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


music_album = make_album('paul mccartney', 'band on the run', 10)
print(music_album)

music_album = make_album('blink 182', "what's my age again")
print(music_album)

music_album = make_album('tool', 'lateralus', 13)
print(music_album)