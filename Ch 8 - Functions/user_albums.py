# Try it yourself, page 146

def make_album(artist, title, tracks=0):
    """Dictionary containing info on an album"""
    album_dict = {'artist' : artist.title(), 'title' : title.title()}

    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


print("(enter 'q' at any time to quit)")
while True:


    artist = input("\nArtist: ")
    if artist == 'q':
        break

    title = input("Album title: ")
    if title == 'q':
            break

    album = make_album(artist, title)
    print(album)
